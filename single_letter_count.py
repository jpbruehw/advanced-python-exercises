def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    res = word.count(letter)
    print(res)


# test functions
single_letter_count('tomorrow', 't')
single_letter_count('tomorrow', 'r')
single_letter_count('Cayman Islands', 's')
