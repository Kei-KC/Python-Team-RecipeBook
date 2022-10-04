import json
import json_db as db
import pandas as pd
import os # for clearing the terminal
import print_db

def main():
	cmd = ""
	while(cmd != "exit"):
		print("""
			Welcome To Pythonees Recipe Book.

			Current functionalities of the recipe book include:
			- View All Recipes (cmd: viewAll)
			- Seach For Recipe (cmd: search)
			- Create New Recipe (cmd: create)
			- Exit (cmd: exit)
			""")
		cmd = input("Enter a command: ")

		# CMD : VIEWALL
		if (cmd == 'viewAll' or cmd == 'viewall'):
			os.system("cls||clear")
			# TODO :
			#	pull all recipes from JSON file and loop over recipe names
			#	print recipe names in terminal
			#	prompt user to select a recipe
			print_db.print_all_names()
			input("Press Enter to return to menu...")

		# CMD : SEARCH
		elif (cmd == 'search'):
			os.system("cls||clear")
			query = input("Please enter your recipe name: ")
			recipe = db.recipe_search(query)

			if (isinstance(recipe, pd.DataFrame)): # RECIPE FOUND, PRINT RECIPE
				# TODO: 
				#	print recipe whole (DONE)
				#	prompt user to view step by step or exit
				print_db.print_whole(recipe)

			else: # RECIPE NOT FOUND
				print("{} does not exist in this recipe book.\n".format(query))

			input("Press Enter to return to menu...")

		# CMD : CREATE
		elif (cmd == 'create'):
			# TODO: 
			#	call to db.recipe_creation() 
			#	prompt user to input name, ingredients and instructions
			#	ingredients separated by ","
			#	instructions separated by ";"
			print("Sorry, this command is not currently available.")
			input("Press Enter to return to menu...")

		# CMD : EXIT
		elif (cmd == 'exit'):	
			print("Thank you for using Pythonees Recipe Book.")
			continue

		else: 
			print("No valid command entered.")
			input("Press Enter to try again...")

		os.system("cls||clear")

	exit();

main()