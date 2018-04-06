brackets = {'{': 0, '}': 0, '[': 0, ']': 0, '(': 0, ')': 0}


def multi_bracket_validation(string):
    for i in string:
        for key, val in brackets.items():
            if i == key:
                brackets[key] += 1
    if brackets['{'] - brackets['}'] == 0 and\
       brackets['['] - brackets[']'] == 0\
       and brackets['('] - brackets[')'] == 0:
        return True
    return False
