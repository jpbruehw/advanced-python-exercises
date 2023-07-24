def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    res = []
    for item in lst:
        if item:
            res.append(item)
    return res


print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
