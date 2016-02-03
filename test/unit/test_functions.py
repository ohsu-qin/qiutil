from math import tan, atan, floor, pi
from nose.tools import (assert_true, assert_false, assert_equal)
from qiutil import functions


class TestFunctions(object):
    """function utilities unit tests."""
    
    def test_is_function(self):
        assert_true(functions.is_function(functions.is_function),
                    "Method is not recognized as a function: %s" %
                    functions.is_function)
        func = lambda x: x
        assert_true(functions.is_function(func),
                    "Lambda is not recognized as a function: %s" % func)
        assert_false(functions.is_function(2),
                     "Integer is incorrectly recognized as a function")

    
    def test_compose(self):
        ident = functions.compose(int, floor, tan, atan)
        actual = ident(pi)
        assert_equal(actual, 3, "The composed result is incorrect: %f" %
                                actual)


if __name__ == "__main__":
    import nose
    nose.main(defaultTest=__name__)
