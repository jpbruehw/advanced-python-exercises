def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    res = {}
    vowels = 'aeiou'
    for char in phrase:
        if char.lower() in vowels and char.lower() not in res:
            res[char.lower()] = 1
        elif char.lower() in vowels:
            res[char.lower()] += 1
    return res


print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!'))
