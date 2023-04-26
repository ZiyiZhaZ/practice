# This method checks whether an input string, username, contains both at least one letter and at least one number
# and returns a Boolean

def letter_and_number(username):
    if username == '':
        return False

    # Initialize values of two Boolean variables, has_letter and has_number to keep track of whether we have
    # found a letter or number yet (we give them the initial value of False, and set them to True if found)
    has_letter = False
    has_number = False

    # Initialize an index variable to 0 to start at the first character in the string username,
    # and increment after each iteration of the while loop to move to the next character
    index = 0

    # While we have not yet found both a letter and a number, check the character at "index"
    while not has_letter or not has_number:
        if username[index].isalpha():
            has_letter = True
        elif username[index].isdigit():
            has_number = True
        
        # If we are currently on the last letter of the username, then break out of the while loop.
        # Else, increment index to move to the next letter in another iteration of the while loop
        # TODO #4: Write the if/else statement described above

        if index == len(username) - 1:
            break
        else:
            index += 1

        
    # Check if the conditions are satisfied, and return True or False accordingly
    if has_letter and has_number:
        return True
    else:
        return False

# This method checks if an input username is unique (does not exist) in the input usernames list, and returns a Boolean
# If it is unique, it returns True, but if it already exists in the list it returns False
def is_unique(username, usernames_list):
    if usernames_list.count(username) == 0:
        return True
    else:
        return False


def main():
    usernames_list = ["paul459", "rockstar857", "bob234"]

    username = input("Enter a valid username: ")

    while not(letter_and_number(username) and is_unique(username, usernames_list)):
        username = input("Username invalid. Enter a valid username: ")
    
    usernames_list.append(username)
    print("Success!")

    return usernames_list


print(main())