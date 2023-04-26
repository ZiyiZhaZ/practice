#name your function find_element 
#with the two parameters described in the directions
def find_element(lst, element):
    for item in range(len(lst)):
        if lst[item] == element:
            return item 
    return -1

print(find_element([1, 5, 3, 9], 3))
print(find_element(['a', 'b', 'c'], 'a'))
print(find_element(["pig", "zebra", "elephant"], "dog"))