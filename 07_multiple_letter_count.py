def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    # return {letter:  for letter in phrase}

    """    for letter in phrase:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1

    return counter """

    {letter:phrase.count(letter) for letter in phrase}






