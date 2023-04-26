# Define your function and parameter here
def passcode_checker(attempts):
    # Fill in your function body here
    # Remember to NOT use the range method
    x = 0
    for item in attempts:
        if item == 'failed':
            x = x + 1
    if x < 3:
        return 'Good memory!'
    elif x <= 4:
        return 'Enter passcode with caution!'
    return 'You should really remember your passcode!'

# Sample attempt list
attempts = ['failed', 'failed', 'succeeded', 'failed', 'succeeded']

# Call your function and print the output here
# Sample function call: passcode_checker(attempts)
print(passcode_checker(attempts))