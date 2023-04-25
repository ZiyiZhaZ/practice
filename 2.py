# define your function here!
def simple_greeting():
    #fill in your function here!
    print("Welcome to CSE 8A!")
# call your function here!
simple_greeting()



# define your function here!
def simple_greeting(name):
    #fill in your function here!
    print("Hello, " + name + ". " + "Welcome to CSE 8A!")
# call your function here!
# TODO: edit this line to accept the argument "Yasmine"
output = simple_greeting("Yasmine")
# TODO: store the result of your function call to a vairable named output
print(output)



# define your function here!
def simple_greeting(name):
    #fill in your function here!
    return("Hello, " + name + ". " + "Welcome to CSE 8A!")
# call your function here!
# TODO: edit this line to accept the argument "Yasmine"
output = simple_greeting("Yasmine")
# TODO: store the result of your function call to a vairable named output
print(output)
# TODO: copy your code from 2.2 here, 
#       and change the print function call to be a return statement (see instructions)



def number_information(num):
    message = "even"
    # FILL_ME
    if num % 2 == 0:
        return message
    else:
        return "odd"
# TODO: obtain an integer from user input. Remember: type casting!
x = float(input("Enter an integer: "))
# TODO: call number_information with the integer you obtained and print the return value of the function
print("Your number is", number_information(x))



def number_information(num):
    if num % 2 == 0:
        messege_1 = "even"
    else:
        messege_1 = "odd"
    if num > 0:
        messege_2 = "positive"
    else:
        messege_2 = "non-positive"
    return (messege_1 + " and " + messege_2)

x = float(input("Enter an integer: "))
print("Your number is", number_information(x))