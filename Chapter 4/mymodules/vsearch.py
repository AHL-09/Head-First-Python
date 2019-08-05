def search4vowels(word: str) -> set:
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return found


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    found = set(letters).intersection(set(phrase))
    return found


print (search4letters(letters='a', phrase='ary'))