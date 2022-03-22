def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """

    """ for ltr in word.upper():
        if ltr == letter.upper():
            count+=1
            
    return count"""

    letters = [ltr for ltr in word if ltr.upper() == letter.upper()]
    return len(letters)

    """count function for strings "word".lower().count(letter.lower()) //checks how many times the letter repeats
    """