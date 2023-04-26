import random
secret_number = random.randint(1,100)
print('A random number between 1 and 100 (inclusive) has been generated.')
# DO NOT EDIT LINES 1-3
limits = int(input('How many attempts do you wish to have: '))
# WRITE YOUR CODE BELOW
guess = True
attempts = 1
while guess == True and attempts <= limits:
    z = input('Please guess a number between 1 and 100: ')
    if z == 'stop':
        guess = False
        continue
    x = int(z)
    if x < 1 or x > 100:
        print('Invalid number, try again!')
        continue
    if x == secret_number:
        print('You won!')
        break
    if x < secret_number:
        print('Guess higher!')
    if x > secret_number:
        print('Guess lower!')
    print('Remaining attempts =', limits - attempts)
    if attempts >= limits:
        print('You lost :(')
        print('Secret_number =', secret_number)
        break
    attempts += 1