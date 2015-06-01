from datetime import datetime 
from nose.tools import assert_equal
from qiutil import dates

class TestDates(object):
    """Date utilities unit tests."""

    def test_non_leap_anonymize(self):
        date = datetime(year=2015, month=6, day=4)
        expected = date.replace(month=7, day=1)
        actual = dates.anonymize(date)
        assert_equal(actual, expected, "Anonymized non-leap year date is"
                                       " incorrect: %s" % actual)

    def test_leap_anonymize(self):
        # 2016 is a leap year.
        date = datetime(year=2016, month=6, day=4)
        expected = date.replace(month=7, day=2)
        actual = dates.anonymize(date)
        assert_equal(actual, expected, "Anonymized leap year date is"
                                       " incorrect: %s" % actual)


if __name__ == "__main__":
    import nose
    nose.main(defaultTest=__name__)
