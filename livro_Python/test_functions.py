#test_functions.py

def what_my_age():
	"""Showing the user age"""
	bday = int(input('Which your birth year?'))
	year = 2020
	age = year - bday

	print("You have " + str(year-bday) + " years old.")
