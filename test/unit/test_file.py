import os
import glob
from nose.tools import assert_equal
from ..helpers.logging import logger
import qiutil
from test import ROOT

FIXTURES = os.path.join(ROOT, 'fixtures', 'file')
"""The test fixture configuration file."""


class TestFile(object):
    """file unit tests."""

    def test_open_non_gz(self):
        in_file = os.path.join(FIXTURES, 'simple.txt')
        with qiutil.file.open(in_file) as fp:
            line_cnt = len(fp.readlines())
        assert_equal(line_cnt, 2, "%s line count is incorrect: %d" %
                                  (in_file, line_cnt))

    def test_open_gz(self):
      in_file = os.path.join(FIXTURES, 'simple.txt.gz')
      with qiutil.file.open(in_file) as fp:
          line_cnt = len(fp.readlines())
          assert_equal(line_cnt, 2, "%s line count is incorrect: %d" %
                                    (in_file, line_cnt))

    def test_generate_file_name(self):
      fname = qiutil.file.generate_file_name('.txt')
      assert_equal(fname[-4:], '.txt', "The generated file name extension"
                                   " is incorrect: %s" % fname)
      assert_equal(len(fname[:-4]), 10, "The generated file base name is"
                                   " longer than ten characters without the"
                                   " extension: %s" % fname)

if __name__ == "__main__":
    import nose
    nose.main(defaultTest=__name__)
