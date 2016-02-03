import os
import glob
from nose.tools import assert_equal
from qiutil.cd import cd


class TestCd(object):
    """cd unit tests."""
    
    def test_cd(self):
        prevdir = os.getcwd()
        ctxtdir = os.path.dirname(__file__)
        with cd(ctxtdir):
            currdir = os.getcwd()
            assert_equal(currdir, ctxtdir, "Context directory is incorrect: %s" %
                                           currdir)
        currdir = os.getcwd()
        assert_equal(currdir, prevdir, "Restored directory is incorrect: %s" %
                                       currdir)
    
    def test_cd_without_context(self):
        prevdir = os.getcwd()
        ctxtdir = os.path.dirname(__file__)
        cd(ctxtdir)
        currdir = os.getcwd()
        assert_equal(currdir, prevdir, "cd without a context resets the directory")

if __name__ == "__main__":
    import nose
    nose.main(defaultTest=__name__)
