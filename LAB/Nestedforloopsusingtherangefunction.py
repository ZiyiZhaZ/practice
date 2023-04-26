def apple_orchard(tree_map):
	sum_apples = []
	for row in range(len(tree_map)): #TODO: FIX THE FOR LOOP
		apples_one_row = 0
		for col in range(len(tree_map[row])):
			ripe_apples = tree_map[row][col]
			apples_one_row += ripe_apples
		sum_apples.append(apples_one_row) #TODO: FILL IN THE ARGUMENT FOR APPEND
		
	return sum_apples

tree_map = [[16, 21, 32, 12], 

 [31, 10, 12, 17], 

 [19, 13, 18, 23]] # TODO: copy the value for tree_map from a given example in the description
print(apple_orchard(tree_map))