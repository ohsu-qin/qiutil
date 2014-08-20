import os
import glob
import shutil
from nose.tools import (assert_equal, assert_true)
from dicom import datadict as dd
from qiutil.dicom_helper import edit_dicom_headers
from qiutil.dicom_helper import iter_dicom
from test import ROOT
from test.helpers.logging_helper import logger

FIXTURE = os.path.join(ROOT, 'fixtures', 'helpers', 'edit_dicom')
"""The test fixture."""

RESULTS = os.path.join(ROOT, 'results', 'helpers', 'edit_dicom')
"""The test results directory."""


class TestEditDicom(object):

    """DICOM edit unit tests."""

    def setUp(self):
        shutil.rmtree(RESULTS, True)

    def tearDown(self):
        shutil.rmtree(RESULTS, True)

    def test_edit_dicom_files(self):
        # The tag name => value map.
        tnv = dict(PatientID='Test Patient', BodyPartExamined='HIP')

        # The tag => value map.
        tv = {dd.tag_for_name(name): value for name, value in tnv.iteritems()}

        # Edit the headers.
        files = set(edit_dicom_headers(RESULTS, FIXTURE, **tnv))

        # Verify the result.
        for ds in iter_dicom(RESULTS):
            assert_true(ds.filename in files)
            for t, v in tv.iteritems():
                assert_equal(v, ds[t].value)


if __name__ == "__main__":
    import nose
    nose.main(defaultTest=__name__)
