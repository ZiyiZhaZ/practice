def sum_arithmetic_seq(start, difference, num_elements): 
    x = 0
    for item in range(num_elements):       
        x += start
        start += difference 
    return x

print(sum_arithmetic_seq(0, 2, 4))