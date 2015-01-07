# Absolute import (the default in a future Python release) resolves
# the collections import as the Python standard collections module
# rather than this module of the same name.
from __future__ import absolute_import
from collections import (Iterable, defaultdict)


def is_nonstring_iterable(obj):
    """
    :param obj: the object to check
    :return: whether the given object is a non-string iterable object
    """
    return isinstance(obj, Iterable) and not isinstance(obj, str)


def to_series(items, conjunction='and'):
    """
    Formats the given items as a series string.

    Example:

    >>> to_series([1, 2, 3])
    '1, 2 and 3'

    :param items: the items to format in a series
    :param conjunction: the series conjunction
    :return: the items series
    :rtype: str
    """
    if not items:
        return ''
    prefix = ', '.join([str(i) for i in items[:-1]])
    suffix = str(items[-1])
    if not prefix:
        return suffix
    else:
        return (' ' + conjunction + ' ').join([prefix, suffix])

def nested_defaultdict(factory, levels=0):
    """
    Makes a defaultdict for the given factory and number of levels, e.g.::

        >> from qiutil.collections import nested_defaultdict as dd
        >> dd(list, 0)[1]
        []
        >> dd(dict, 2)[1][2][3]
        {}

    Note that the default levels parameter value 0 is synonymous with the
    standard Python collections defaultdict, i.e.::

        dd(list)

    is the same as::

        dd(list, 0)

    or::

        from collections import defaultdict
        defaultdict(list)
    
    Thus, this ``nested_defaultdict`` function can serve as a drop-in
    replacement for ``defaultdict``.

    :param factory: the 0th level defaultdict factory.
    :param levels: the number of levels
    """
    # The recursive nested dictionary generator, where f is the factory
    # and n is the number of levels.
    dd = lambda f, n: defaultdict((lambda: dd(f, n - 1)) if n else f)

    return dd(factory, levels)


class ImmutableDict(dict):

    """
    ImmutableDict is a dictionary that cannot be changed after creation.

    An ImmutableDict is *not* hashable and therefore cannot be used as a dictionary
    key or set member. See http://www.python.org/dev/peps/pep-0351 for the rationale.
    """

    def __init__(self, *args, **kwargs):
        super(ImmutableDict, self).__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        """
        :raise NotImplementedError: always
        """
        raise NotImplementedError("The dictionary is immutable: %s" % self)

EMPTY_DICT = ImmutableDict()
"""
An immutable empty dictionary.
This constant serves as an efficient method return default value.
"""
