def multi_bracket_validation(string):
    """
    This function return True if brackets are all matched up in string, and \
    return False if there is unmatched brackets.
    """
    if not isinstance(string, str):
        raise TypeError('It\'s not a string.')

    brackets = {'{': 0, '}': 0, '[': 0, ']': 0, '(': 0, ')': 0}

    for i in string:
        for key, val in brackets.items():
            if i == key:
                brackets[key] += 1

    if brackets['{'] - brackets['}'] == 0 and\
        brackets['['] - brackets[']'] == 0 and\
       brackets['('] - brackets[')'] == 0:
        return True

    return False
