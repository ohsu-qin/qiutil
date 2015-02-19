"""The Quantitative Imaging utility module cxvvcxv."""

__version__ = '2.1.8'
"""
The one-based major.minor.patch version based on the
`Fast and Loose Versioning <https://gist.github.com/FredLoney/6d946112e0b0f2fc4b57>`_
scheme. Minor and patch version numbers begin at 1.
"""

# Import collections, file and logging, since these are also
# standard Python libraries. This import allows the client to
# use the nested modules directly, e.g.:
#   with qiutil.file.open(...):
# rather than:
#   from qiutil import file
#   with file.open(...): # Misleading
#  or:
#   from qiutil import file as qifile
#   with qifile.open(...): # Awkward
from . import (collections, file, logging) 
