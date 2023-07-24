def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    res = ''
    for char in phrase:
        if to_swap.islower() and char.isupper() and char.lower() == to_swap:
            res += char.lower()
        elif to_swap.isupper() and char.islower() and char == to_swap.lower():
            res += char.upper()
        elif to_swap.isupper() and char.isupper() and char == to_swap:
            res += char.lower()
        elif to_swap.isupper() and not char.isupper() and char == to_swap.lower():
            res += char.upper()
        elif to_swap.islower() and char.islower() and char == to_swap:
            res += char.upper()
        else:
            res += char
    print(res)


flip_case('Aaaahhh', 'A')
flip_case('Aaaahhh', 'a')
flip_case('Aaaahhh', 'h')
