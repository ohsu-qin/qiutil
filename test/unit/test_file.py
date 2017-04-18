import os
from nose.tools import (assert_equal, assert_is_none)

import qiutil
from .. import ROOT

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

    def test_splitexts(self):
        base, exts = qiutil.file.splitexts('simple')
        assert_equal(base, 'simple',
                     "The splitexts base path is incorrect: %s" % base)
        assert_is_none(exts, "The splitexts extension is incorrect: %s" % exts)

        base, exts = qiutil.file.splitexts('./bar.txt')
        assert_equal(base, './bar',
                     "The splitexts base path is incorrect: %s" % base)
        assert_equal(exts, '.txt',
                     "The splitexts extension is incorrect: %s" % exts)

        base, exts = qiutil.file.splitexts('/tmp/foo.3/bar.txt.gz')
        assert_equal(base, '/tmp/foo.3/bar',
                     "The splitexts base path is incorrect: %s" % base)
        assert_equal(exts, '.txt.gz',
                     "The splitexts extensions is incorrect: %s" % exts)

    def test_splitboth(self):
        dir_path, base, exts = qiutil.file.splitboth('simple')
        assert_is_none(dir_path, "The splitboth directory path is"
                                 " incorrect: %s" % dir_path)
        assert_equal(base, 'simple',
                     "The splitboth base path is incorrect: %s" % base)
        assert_is_none(exts, "The splitboth extension is incorrect: %s" % exts)

        dir_path, base, exts = qiutil.file.splitboth('./bar.txt')
        assert_equal(dir_path, '.', "The splitboth directory path is"
                                 " incorrect: %s" % dir_path)
        assert_equal(base, 'bar',
                     "The splitboth base path is incorrect: %s" % base)
        assert_equal(exts, '.txt',
                     "The splitboth extension is incorrect: %s" % exts)

        dir_path, base, exts = qiutil.file.splitboth('/tmp/foo.3/bar.txt.gz')
        assert_equal(dir_path, '/tmp/foo.3', "The splitboth directory path is"
                                             " incorrect: %s" % dir_path)
        assert_equal(base, 'bar',
                     "The splitboth base path is incorrect: %s" % base)
        assert_equal(exts, '.txt.gz',
                     "The splitboth extensions is incorrect: %s" % exts)

    def test_generate_file_name(self):
      fname = qiutil.file.generate_file_name('.txt')
      assert_equal(fname[-4:], '.txt', "The generated file name extension"
                                   " is incorrect: %s" % fname)
      assert_equal(len(fname[:-4]), 10, "The generated file base name is"
                                   " longer than ten characters without the"
                                   " extension: %s" % fname)

    def test_finder_find(self):
        finder = qiutil.file.Finder('f*/*/*',
                                    'fixtures/fil./(?P<base>\w+)\.txt(\.gz)?$')
        # Test find.
        found = set(finder.find(ROOT))
        expected = {FIXTURES + '/simple.txt' + ext for ext in ['', '.gz']}
        assert_equal(found, expected, "Found files incorrect: %s vs %s" %
                                      (found, expected))

    def test_finder_match(self):
        finder = qiutil.file.Finder('f*/*/*',
                                    'fixtures/fil./(?P<base>\w+)\.txt(\.gz)?$')
        # Test the match variables.
        matched = [m.group('base') for m in finder.match(ROOT)]
        assert_equal(matched, ['simple'] * 2, "Matched files incorrect: %s" %
                                              matched)

    def test_finder_defaults(self):
        finder = qiutil.file.Finder()
        found = set(finder.find(FIXTURES))
        expected = {'/'.join((FIXTURES, fname)) for fname in os.listdir(FIXTURES)}
        assert_equal(found, expected, "Default found files incorrect: %s vs %s" %
                                      (found, expected))


if __name__ == "__main__":
    import nose
    nose.main(defaultTest=__name__)
