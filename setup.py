import os
import re
import subprocess
import glob
from setuptools import (setup, find_packages)
from setuptools.command.install import install

# Note - this setup does not install Git dependencies, due to the
# following Python install bug:
# * pip install -e does not support Git requirements.
# The work-around is to run pip install twice:
#     pip install -e .
#     pip install -r requirements.txt
#
# Note - the Install class below is one of many attempts to workaround
# the pip install bug. Unfortunately, Install.run() is not executed
# even when the following is added to the setup config:
#     cmdclass={'install': Install}
# This is perhaps another pip install bug.
#
# class Install(install):
#     """Extend setup install to install Git dependencies."""
# 
#     RQMTS = os.path.abspath(os.path.join(os.path.dirname(__file__), 'requirements.txt'))
#     """The requirements file."""
# 
#     CMD = "echo pip install -r %s" % RQMTS
#     """The install command."""
# 
#     def run(self):
#         install.run(self)
#         subprocess.call(CMD.split())
#
# TODO - refactor qiutil as follows:
# * Split out the xnat stuff into qixnat
# * Move dicom stuff (incl. project and *hierarchy) and which
#   back to qipipe
# * Retain only the core utility helpers in qiutil,
#   specifically command, logging, config and collection.

VCS_RQMT_PAT = re.compile('^\w+\+\w+:')
"""
The pattern for detecting a VCS requirement spec, e.g.
``git+git://...``.
"""

def version(package):
    """
    Return package version as listed in the `__init.py__` `__version__`
    variable.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def requires():
    """
    @return: the ``requirements.txt`` package specifications
    
    :Note: ``pip`` supports VCS package specifications, but
       setup.py does not. Therefore, this method filters out
       the VCS requirements in ``requirements.txt``. The VCS
       dependencies must be installed separately as described
       in the User Guide **Installation** section.
    """
    with open('requirements.txt') as f:
        rqmts = f.read().splitlines()
        return [rqmt for rqmt in rqmts if not VCS_RQMT_PAT.match(rqmt)]
        

def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name = 'qiutil',
    version = version('qiutil'),
    author = 'OHSU Knight Cancer Institute',
    author_email = 'loneyf@ohsu.edu',
    packages = find_packages(),
    data_files=[('config', glob.glob('conf/*.cfg'))],
    scripts = glob.glob('bin/*'),
    url = 'http://quip1.ohsu.edu/8080/qiutil',
    description = 'Quantitative imaging helper utilities.',
    long_description = readme(),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires = requires()
)
