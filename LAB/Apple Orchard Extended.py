def apple_orchard(tree_map):
	sum_apples = []
	for row in range(len(tree_map[0])): #TODO: FIX THE FOR LOOP
		apples_one_row = 0
		for col in range(len(tree_map)):
			ripe_apples = tree_map[col][row]
			apples_one_row += ripe_apples
		sum_apples.append(apples_one_row) #TODO: FILL IN THE ARGUMENT FOR APPEND
		
	return sum_apples

tree_map = [[5, 10, 2], 

     [4, 1, 12], 

 [31, 3, 8]] # TODO: copy the value for tree_map from a given example in the description
print(apple_orchard(tree_map))