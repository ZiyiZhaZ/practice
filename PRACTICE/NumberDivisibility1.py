def check_divisibility(num):
    if num % 2 == 0 and num % 3 == 0:
        messege = "divisible by 2 and 3!"
    elif num % 2 == 0 and not num % 3 == 0:
        messege = "divisible only by 2!"
    elif not num % 2 == 0 and num % 3 == 0:
        messege = "divisible only by 3!"
    else:
        messege = "not divisibe by 2 or 3!"
    return messege

num = float(input("Enter your number: "))
print(num, "is", check_divisibility(num))