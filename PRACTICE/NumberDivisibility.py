def check_divisibility(num):
    if num % 2 == 0 and num % 3 == 0:
        print(num, "is divisible by 2 and 3!")
    elif num % 2 == 0:
        print(num, "is divisible only by 2!")
    elif num % 3 == 0:
        print(num, "is divisible only by 3!")
    else:
        print(num, "is not divisibe by 2 or 3!")

check_divisibility(12)
check_divisibility(25)