import os
import glob
from nose.tools import assert_equal
from ..helpers.logging import logger
import qiutil
from test import ROOT

FIXTURE = os.path.join(ROOT, 'fixtures', 'file', 'simple.txt.gz')
"""The test fixture configuration file."""


class TestFile(object):
    """file unit tests."""

    def test_open_gz(self):
        with qiutil.file.open(FIXTURE) as fp:
          line_cnt = len(fp.readlines())
        assert_equal(line_cnt, 2, "%s line count is incorrect: %d" % (FIXTURE, line_cnt))


if __name__ == "__main__":
    import nose
    nose.main(defaultTest=__name__)
