import json
import json_db as db
import pandas as pd
import os # for clearing the terminal
from tabulate import tabulate
import textwrap

# CLEAR TERMINAL
def clear_terminal():
	os.system("cls||clear")
	return

# FORMAT BORDER AROUND TEXT
def border(text):
	table = [[textwrap.dedent(text)]]
	print(tabulate(table, tablefmt="grid", numalign="left"))

# PRINT ENTIRE MENU
def print_all_menu():
	df = pd.read_csv('recipe_book.csv')
	data = {}
	for idx, recipes in df.iterrows():
		name = recipes['name']
		print("Menu {}: {}".format(idx+1, name))
		data[idx+1]=name
	print("")

	return data

# PRINT ENTIRE RECIPE 
def print_whole(recipe):
	name = recipe["name"].values[0]
	print('recipe = ', recipe)
	print('name = ', name)
	ingr_arr = recipe["ingredients"].values[0].split(",")
	inst_arr = recipe["instructions"].values[0].split(";")

	# print name
	border("Recipe Name: {}\n".format(name))
	names = {}
	names[name] = ""
	print(names)
	
	# print ingredients
	print("Ingredients:")
	ingredients = {}
	for ingr in ingr_arr: 
		print("{}".format(ingr))
	ingredients[ingr] = "" # save instructions as key
	print("")

	# print instructions
	print("Instructions:")
	instructions = {}
	for inst in inst_arr: 
		print("{}".format(inst))
	instructions[inst] = "" # save instructions as key
	# print(instructions)
	print("")

	return names, ingredients, instructions

# PRINT RECIPE STEP-BY-STEP
def step_by_step(recipe):
	border("Would you like to view instructions step by step? (Y/N)")
	choice = input("").lower()
	
	if (choice == "y" or choice == "yes"): # step-by-step
		clear_terminal()
		border("""
			Viewing instructions for {}.
			Press any key to view next instruction.
			""".format(recipe["name"].values[0]))
		inst_arr = recipe["instructions"].values[0].split(";")

		for inst in inst_arr: 
			input("{}".format(inst))

		border("""
			Finished viewing instructions.
			Press any key to return to menu.""")
		input("")

	return

# RECIPE NOT FOUND
def not_found(query):
	border("{} does not exist in this recipe book.\nPress any key to return to menu.".format(query))
	input("")
	return




