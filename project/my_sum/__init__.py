#  Create __init_py file for my_sum folder
# This means that the my_sum folder can be imported as a module from the parent directory

def sum(arg):
	total = 0
	for val in arg:
		total += val
	return total
