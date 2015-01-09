import os
import glob
from nose.tools import (assert_equal, assert_raises, assert_true, assert_false)
from qiutil import collections as qicollections

class TestCollections(object):

    """collections unit tests."""

    def test_is_nonstring_iterable(self):
        assert_true(qicollections.is_nonstring_iterable(
            ['a', 'b']), "List is not recognized as a non-string collection")
        assert_false(qicollections.is_nonstring_iterable('a'),
                     "String is incorrectly recognized as a non-string collection")

    def test_to_series(self):
        assert_equal(qicollections.to_series([1, 2, 3]), '1, 2 and 3',
                     'Series formatter incorrect')
        assert_equal(qicollections.to_series([1, 2, 3], 'or'), '1, 2 or 3',
                     'Series formatter with conjunction incorrect')
        assert_equal(qicollections.to_series([1]), '1',
                     'Singleton series formatter incorrect')
        assert_equal(qicollections.to_series([]), '',
                     'Empty series formatter incorrect')

    def test_update_dict_nonrecursive(self):
        target = dict(a=1)
        sources = [dict(a=2), dict(b=3), dict(b=4, c=5)]
        qicollections.update(target, *sources)
        expected = dict(a=2, b=4, c=5)
        assert_equal(target, expected, "The updated target is incorrect: %s" %
                                       target)

    def test_update_dict_recursive(self):
        target = dict(a=dict(aa=1))
        sources = [dict(a=dict(aa=2)), dict(a=dict(ab=3))]
        qicollections.update(target, *sources, recursive=True)
        expected = dict(a=dict(aa=2, ab=3))
        assert_equal(target['a'], expected['a'], "The updated target is"
                                                 " incorrect: %s" % target)

    def test_update_list(self):
        target = [1, 2, 2, 5]
        sources = [set([3]), [6, 2], [5, 5, 1, 1, 4, 4]]
        qicollections.update(target, *sources)
        expected = [1, 2, 2, 5, 3,
         6, 4, 4]
        assert_equal(target, expected, "The updated target list is incorrect:"
                                       " %s" % target)

    def test_immutable_dict(self):
        dd = qicollections.ImmutableDict(foo='bar')
        assert_equal(dd['foo'], 'bar', 'Value was not set.')
        with assert_raises(NotImplementedError):
            dd['foo'] = 'baz'

    def test_nested_defaultdict(self):
        dd = qicollections.nested_defaultdict(list, 2)
        dd[1][2][3] = 'foo'
        assert_equal(dd[1][2][3], 'foo', 'Value incorrect.')
        with assert_raises(IndexError):
            dd[1][2][3][4]



if __name__ == "__main__":
    import nose
    nose.main(defaultTest=__name__)
