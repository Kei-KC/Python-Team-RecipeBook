def main():
	print("""Welcome To Pythonees Recipe Book.
		Current functionalities of the recipe book include:
		1) View All Recipes (cmd: viewAll)
		2) Seach For Recipe (cmd: search)
		3) Exit (cmd: exit)
		""")

	cmd = input("Enter a command: ")
	while(cmd != "exit"): 

		# CMD : VIEWALL
		if (cmd == 'viewAll' || cmd == 'viewall' || cmd == 1):
			# TODO :
			#	pull all recipes from JSON file and loop over recipe names
			#	print recipe names in terminal
			#	prompt user to select a recipe

		# CMD : SEARCH
		else if (cmd == 'search' || cmd == 2):
			# TODO:
			#	prompt user for a recipe name 
			#	maybe implement fuzzy search

		cmd = input("Enter a command: ")
	exit();
main()