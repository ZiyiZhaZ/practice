def clear_row(lst, index):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if i == index:
                lst[i][j] = 0
    return lst

def clear_column(lst, index):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j == index:
                lst[i][j] = 0
    return lst

data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
print(clear_row(data, 1))

data1 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
print(clear_column(data1, 2))