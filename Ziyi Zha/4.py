passcode = "cse8a"
while True:
    answer = input("Enter the passcode: ")
    if answer == passcode:
        print("You entered the correct passcode! Welcome to CSE 8A!")
        break
    else:
        print("You entered an incorrect passcode! Try again!")