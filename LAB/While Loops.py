def f(num):
    i = 1
    s = 0
    while i <= num:
        # You can put print statements throughout the loop body 
        # to examine the values of the variables
        
        s = s + i
        # or have a print statement HERE
        print(s)
        i = i + i
        # or have a print statement HERE
        print(i)
        print(num)
    return s

x = f(12)
print(x)