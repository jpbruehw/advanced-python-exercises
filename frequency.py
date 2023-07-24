def frequency(lst, search_term):
    """Return frequency of term in lst.

        >>> frequency([1, 4, 3, 4, 4], 4)
        3

        >>> frequency([1, 4, 3], 7)
        0
    """
    res = lst.count(search_term)
    print(res)


frequency([1, 4, 3, 4, 4], 4)
frequency([1, 4, 3], 7)
