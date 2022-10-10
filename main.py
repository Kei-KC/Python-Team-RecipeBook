import json
import json_db as db
import pandas as pd
import os # for clearing the terminal
import print_db
from tabulate import tabulate

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
			os.system("cls||clear")
			# TODO :
			#	pull all recipes from CSV file and loop over recipe names
			#	print recipe names in terminal
			#	prompt user to select a recipe
			print_db.print_all_menu()

			query = input("\nNow select a menu to view recipe! ")
			recipe = db.recipe_search(query)

			if (isinstance(recipe, pd.DataFrame)):
				os.system("cls||clear")
				print_db.print_whole(recipe)
			else:
				print("{} does not exist in this recipe book.\n".format(query))
			
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
			print_db.border("Thank you for using Pythonees Recipe Book.")
			continue

		else: 
			print_db.border("No valid command entered. Press any key to return to menu.")
			input("")

		os.system("cls||clear")

	exit();

main()