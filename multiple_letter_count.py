def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    res = {}
    for char in phrase:
        char_lower = char.lower()
        res[char_lower] = res.get(char_lower, 0) + 1

    print(res)


multiple_letter_count('yay')
multiple_letter_count('hello')
multiple_letter_count('bottle')
