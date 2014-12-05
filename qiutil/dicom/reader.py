# Absolute import (standard in Python 3) imports dicom from pydicom
# rather than the parent module.
from __future__ import absolute_import
import os
import dicom
from dicom.filereader import InvalidDicomError
from .. import file_helper
from ..file_helper import FileIterator
from ..logging_helper import logger


def iter_dicom(*dicom_files):
    """
    Iterates over the DICOM data sets for DICOM files at the given locations.
    
    :param dicom_files: the DICOM files or directories containing DICOM files
    """
    return DicomIterator(*dicom_files)


def iter_dicom_headers(*dicom_files):
    """
    Iterates over the DICOM headers for DICOM files at the given locations.
    
    :param dicom_files: the DICOM files or directories containing DICOM files
    """
    return DicomHeaderIterator(*dicom_files)


class DicomIterator(FileIterator):
    """
    DicomIterator is a generator class for reading the pydicom data sets from
    DICOM files.
    """

    def __init__(self, *dicom_files, **opts):
        """
        :param dicom_files: the DICOM files to include
        """
        super(DicomIterator, self).__init__(*dicom_files)
        self.opts = opts

    def next(self):
        """
        Iterates over each DICOM data set.
        
        :yield: the next pydicom dicom object
        """
        for filename in super(DicomIterator, self).next():
            with file_helper.open_file(filename) as fp:
                try:
                    yield dicom.read_file(fp, **self.opts)
                except InvalidDicomError:
                    logger(__name__).info("Skipping non-DICOM file %s" % filename)


class DicomHeaderIterator(DicomIterator):
    """
    DicomHeaderIterator is a generator class for reading the pydicom non-pixel
    data sets from DICOM files.
    """

    OPTS = dict(defer_size=256, stop_before_pixels=True, force=False)

    def __init__(self, *dicom_files):
        super(DicomHeaderIterator, self).__init__(*dicom_files, **DicomHeaderIterator.OPTS)
