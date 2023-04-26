def reverse_list(lst):
    for i in range(int(len(lst) / 2)):
        temp = lst[i]
        #print(temp)
        lst[i] = lst[(len(lst) - 1) - i]
        #print(lst[i])
        lst[(len(lst) - 1) - i ] = temp
        #print(lst[(len(lst) - 1) - i])
        #prin(lst)
    return lst

print(reverse_list(["a", "b", "c", "d", "e"]))

#the problem is that when we do the assignment inside the loop, it repeats len(lst) times, 
#and this will result in the whole list reverse itself and then reverse back, since when it 
#repeat half of the len(lst), it already reversed itself (the assignment inside the loop changes 
#both side of the list, but not just one side). As a result, we could just make the repeat times 
#just equl to the half length (int(len(lst) / 2)).