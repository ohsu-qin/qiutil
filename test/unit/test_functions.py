from math import tan, atan, floor, pi
from nose.tools import assert_equal
from qiutil.functions import compose 


class TestFunctions(object):
    """function utilities unit tests."""

    def test_compose(self):
        ident = compose(int, floor, tan, atan)
        actual = ident(pi)
        assert_equal(actual, 3, "The composed result is incorrect: %f" %
                                actual)


if __name__ == "__main__":
    import nose
    nose.main(defaultTest=__name__)
