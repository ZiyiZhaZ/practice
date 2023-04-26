def get_emp_id(emp_info):
	emp_id = emp_info[0]
	return emp_id
print(get_emp_id((771, 80, 30)))

# TODO #2 and 3: Uncomment and run the code below
# Is this code correct? Why or why not? Fix if incorrect.
# No, since tuples are immutable.
def change_emp_id(emp_info, emp_id):
	new_emp_info = (emp_id, emp_info[1], emp_info[2]) 
	return new_emp_info

print(change_emp_id((771, 80, 30), 90))