def sum_of_ends(x):
    if len(x) == 0:
        return 0
    return x[0] + x[-1]

print(sum_of_ends([]))
print(sum_of_ends([3]))