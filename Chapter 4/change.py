def search4letters(phrase: str, letters: str) -> set:
    """Return any vowels found in a supplied phrase."""
    found = set(letters).intersection(set(phrase))
    return found
