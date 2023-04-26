def count(nums):
    x = 0
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            x += 1
    return x

print(count([4, 9, -7, 0, 1]))