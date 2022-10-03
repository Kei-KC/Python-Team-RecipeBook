import json
import json_db as db
import os # for clearing the terminal


# PRINT ENTIRE RECIPE 
def print_whole(recipe):
	name = recipe["name"]
	ingredients_arr = recipe["ingredients"].str.split(",")
	instructions_arr = recipe["instructions"].str.split(";")
	print("{} Recipe\n".format(name))

	# print ingredients
	print("Ingredients:\n")
	for ing in ingredients_arr: 
		print("{}\n".format(ing))

	# print instructions
	print("Instructions:\n")
	for ins in instructions_arr: 
		print("{}\n".format(ins))

	return

# PRINT RECIPE STEP-BY-STEP
def step_by_step(recipe):
	return

def main():
	cmd = ""
	while(cmd != "exit"):
		print("""Welcome To Pythonees Recipe Book.
			Current functionalities of the recipe book include:
			1) View All Recipes (cmd: viewAll)
			2) Seach For Recipe (cmd: search)
			3) Exit (cmd: exit)
			""")
		cmd = input("Enter a command: ")

		# CMD : VIEWALL
		if (cmd == 'viewAll' or cmd == 'viewall' or cmd == 1):
			# TODO :
			#	pull all recipes from JSON file and loop over recipe names
			#	print recipe names in terminal
			#	prompt user to select a recipe
			return

		# CMD : SEARCH
		else if (cmd == 'search' || cmd == 2):
			# TODO:
			#	prompt user for a recipe name 
			#	maybe implement fuzzy search

		cmd = input("Enter a command: ")
	exit();

main()
f.close()