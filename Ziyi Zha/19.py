def reverse_list(words):
    new_list = []
    for i in range(len(words) - 1, -1, -1):
        new_list.append(words[i])
    return new_list

words = ['apple', 'orange', 'banana', 'pear']
print(reverse_list(words))
# TODO AFTER bugs are resolved: Remove the # at the beginning of the following lines
words2 = ['cat']
print(reverse_list(words2))
words3 = []
print(reverse_list(words3))