def sum_arithmetic_seq(start, difference, num_elements): 
    x = 0
    for i in range(num_elements):
        x += start
        start += difference 
    return x

print(sum_arithmetic_seq(1, 2, 3))
print(sum_arithmetic_seq(3, 5, 2))
print(sum_arithmetic_seq(0, 2, 4))
print(sum_arithmetic_seq(0, -3, 4))
print(sum_arithmetic_seq(1, 3, 0))