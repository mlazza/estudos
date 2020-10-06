#print_models.py

def print_models(unprinted, completed):
	"""Simulation of design printing"""
	while unprinted:
		current_design = unprinted.pop()

		print('Printing model:' + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the printed models"""
	print("\nThe following models have been printed: ")
	for complete in completed:
		print(complete)


