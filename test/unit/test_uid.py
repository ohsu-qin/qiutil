from nose.tools import (assert_equal, assert_not_equal)
from ..helpers.logging import logger
import qiutil


class TestUid(object):
    """uid unit tests."""

    def test_generate_uid(self):
      # Make ten UIDs in rapid-fire succession.
      uids = [qiutil.uid.generate_uid() for i in range(10)]
      first = uids.pop(0)
      for uid in uids:
        assert_not_equal(uid, first, "Duplicate uids: %d" % first)

    def test_generate_string_uid(self):
      uid = qiutil.uid.generate_string_uid()
      assert_equal(len(uid), 10, "The generated uid is not ten characters"
                                 " long: %s" % uid)

if __name__ == "__main__":
    import nose
    nose.main(defaultTest=__name__)
