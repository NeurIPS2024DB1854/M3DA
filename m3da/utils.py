from typing import Iterable, Union


def flatten(iterable: Iterable, iterable_types: Union[tuple, type] = None) -> list:
    """
    Taken from: https://github.com/neuro-ml/deep_pipe/blob/master/dpipe/itertools.py
    Recursively flattens an ``iterable`` as long as it is an instance of ``iterable_types``.

    Examples
    --------
    >>> flatten([1, [2, 3], [[4]]])
    [1, 2, 3, 4]
    >>> flatten([1, (2, 3), [[4]]])
    [1, (2, 3), 4]
    >>> flatten([1, (2, 3), [[4]]], iterable_types=(list, tuple))
    [1, 2, 3, 4]
    """
    if iterable_types is None:
        iterable_types = type(iterable)
    if not isinstance(iterable, iterable_types):
        return [iterable]

    return sum((flatten(value, iterable_types) for value in iterable), [])
