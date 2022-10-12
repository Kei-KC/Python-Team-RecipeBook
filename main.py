import json
import json_db as db
import pandas as pd
import os # for clearing the terminal
import print_db
from tabulate import tabulate

def clear_terminal():
	os.system("cls||clear")
	return

# USER INPUTS INGREDIENTS DURING CREATE
#   accepts a delimiter
#   for ingredients, ","
#   for instructions, ";"
def inputs_to_list(delimiter):
	string = ""
	user = input("")
	while(user != "DONE"):
		string += user + delimiter
		user = input("")
	res = [string]
	return res

def main():
	cmd = ""
	while(cmd != "exit"):
		print_db.border("""
		Welcome To Pythonees Recipe Book.

		Please select from the following:
		* View Recipes (cmd: viewAll)
		* Seach Recipe (cmd: search)
		* Create Recipe (cmd: create)
		* Exit (cmd: exit)""")
		cmd = input("Enter a command: ")

		# CMD : VIEWALL
		if (cmd == 'viewAll' or cmd == 'viewall'):
			clear_terminal()
			# TODO :
			#	pull all recipes from CSV file and loop over recipe names
			#	print recipe names in terminal
			#	prompt user to select a recipe
			print_db.border("All Recipes")
			print_db.print_all_menu()

			query = input("\nNow select a menu to view recipe! ")
			recipe = db.recipe_search(query)

			if (isinstance(recipe, pd.DataFrame)):
				clear_terminal()
				print_db.print_whole(recipe)
				print_db.step_by_step(recipe)

			else:
				print_db.not_found(query)

		# CMD : SEARCH
		elif (cmd == 'search'):
			clear_terminal()
			print_db.border("Please enter a recipe name.")
			query = input("")
			clear_terminal()

			fuzzy_match = db.fuzzy_search(query) # FUZZY SEARCH
			#ingr_match = db.ingredient_search(query) # INGREDIENT SEARCH
			#print(ingr_match)

			if (len(fuzzy_match) == 1): # RECIPE FOUND, PRINT RECIPE
				print_db.border("Recipe found for {}!\n".format(fuzzy_match[0]))
				# TODO: 
				#	print recipe whole
				#	prompt user to view step by step or exit
				print_db.print_whole(db.recipe_search(fuzzy_match[0]))
				print_db.step_by_step(db.recipe_search(fuzzy_match[0]))

			elif (len(fuzzy_match) >= 2): # MULTIPLE RECIPES FOUND, CHOOSE RECIPE
				# TODO: 
				#   print list of recipes that match
				#   prompt user to choose from the list
				print_db.border("The following recipes matched your search for {}:".format(query))
				for recipe in fuzzy_match:
					print(recipe)
				print_db.border("Please enter the recipe you would like to view.")
				choice = input("")
				clear_terminal()

				print_db.print_whole(db.recipe_search(choice))
				print_db.step_by_step(db.recipe_search(choice))

			else: # RECIPE NOT FOUND
				print_db.not_found(query)

		# CMD : CREATE
		elif (cmd == 'create'):
			# TODO: 
			#	call to db.recipe_creation() 
			#	prompt user to input name, ingredients and instructions
			#	ingredients separated by ","
			#	instructions separated by ";"
			clear_terminal()
			print_db.border("To create a new recipe, enter your recipe's name.")
			name = input("")

			# GET INGREDIENTS
			print_db.border("""
				Enter your recipe's ingredients.
				When finished, type 'DONE'.""")
			ingr = inputs_to_list(',')

			# GET INSTRUCTIONS
			print_db.border("""
				Enter your recipe's instructions step by step.
				
				For example: 
				1. combine eggs and milk
				2. stir thoroughly

				When finished, type 'DONE'.""")
			inst = inputs_to_list(';')

			db.recipe_creation(name, ingr, inst)
			#clear_terminal()
			print_db.border("New recipe for {} has been created!".format(name))
			print_db.print_whole(db.recipe_search(name))

		# CMD : EXIT
		elif (cmd == 'exit'):
			clear_terminal()	
			print_db.border("Thank you for using Pythonees Recipe Book.")
			continue

		else: 
			print_db.border("No valid command entered. Press any key to return to menu.")
			input("")

		clear_terminal()

	exit();

main()