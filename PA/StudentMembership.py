def check_membership(cse8a, math20a, student):
    if student in cse8a and student in math20a:
        return student + ' is in both classes'
    elif student in cse8a:
        return student + ' is only in CSE 8A'
    elif student in math20a:
        return student + ' is only in Math 20A'
    return student + ' is not in either class'