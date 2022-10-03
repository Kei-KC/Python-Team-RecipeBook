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
		elif (cmd == 'search' or cmd == 2):
			query = input("Please enter your recipe name: ")
			recipe = db.recipe_search(query)

			if (recipe == False): # RECIPE NOT FOUND
				print("{} does not exist in this recipe book.\n".format(query))

			else: # RECIPE FOUND, PRINT RECIPE
				# TODO: 
				#	print recipe whole (DONE)
				#	prompt user to view step by step or exit

				print(recipe)
				print_whole(recipe)

			input("Press Enter to return to menu...\n")
			return

		# CMD : CREATE
		#elif (cmd == 'create' or cmd == 3):
			# TODO: 
			#	call to db.recipe_creation() 
			#	prompt user to input name, ingredients and instructions
			#	ingredients separated by ","
			#	instructions separated by ";"

		os.system("cls||clear")
	exit();

main()
f.close()