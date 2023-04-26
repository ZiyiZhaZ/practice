def rainfall(rain_amounts):
    index = 0
    x = 0
    for i in rain_amounts:
        if i >= 0:
            index += 1
            x += i
    if index == 0:
        return ('No positive rainfall values')
    return float(x / index)

print(rainfall([0, 1, -3, 4, 7]))
print(rainfall([-3, -1, -12, -4, -2]))
print(rainfall([2, 4, 2, 4]))