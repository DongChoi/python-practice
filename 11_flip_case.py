def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    """result = letter.swapcase() if letter.upper() == to_swap.upper() else letter
    return "".join(result)"""

    result = ""
    for letter in phrase:
        if letter.upper() == to_swap.upper():
            result.join(letter.swapcase())
    return result


    #    return lst[-1] if lst else None