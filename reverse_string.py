def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    res = ''.join(reversed(phrase))
    print(res)


reverse_string('phrase')
reverse_string('cake')
reverse_string('flower')
