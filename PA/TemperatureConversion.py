# WRITE YOUR CODE HERE
def fahrenheit_to_celsius(temp_in_fahrenheit):
    x = (temp_in_fahrenheit - 32) * 5 / 9
    return x

def celsius_to_fahrenheit(temp_in_celsius):
    y = (temp_in_celsius * 9 / 5) + 32
    return y

tem_f = float(input("Enter a temperature in fahrenheit: "))
tem_fc = fahrenheit_to_celsius(tem_f)
print(tem_f, "degree fahrenheit =", tem_fc, "celsius")
tem_c = float(input("Enter a temperature in celsius: "))
tem_cf = celsius_to_fahrenheit(tem_c)
print(tem_c, "degree celsius =", tem_cf, "fahrenheit")