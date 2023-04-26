def sum_arithmetic_seq(start, difference, num_elements): 
    x = start
    for item in range(num_elements - 1):
        start += difference 
        x += start
    return x