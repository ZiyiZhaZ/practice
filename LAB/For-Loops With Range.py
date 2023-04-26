def passcode_checker(attempts):
    # Remember to use the range method
    x = 0
    for item in range(len(attempts)):
        if attempts[item] == 'failed':
            x = x + 1
    if x < 3:
        return 'Good memory!'
    elif x <= 4:
        return 'Enter passcode with caution!'
    return 'You should really remember your passcode!'

attempts = ['failed', 'failed', 'succeeded', 'failed', 'failed', 'failed']

print(passcode_checker(attempts))