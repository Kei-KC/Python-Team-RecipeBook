import json
import json_db as db
import pandas as pd

# PRINT ENTIRE RECIPE 
def print_whole(recipe):
	name = recipe["name"].values[0]
	ingr_arr = recipe["ingredients"].values[0].split(",")
	inst_arr = recipe["instructions"].values[0].split(";")

	# print name
	print("Recipe Name: {}\n".format(name))

	# print ingredients
	print("Ingredients:")
	for ingr in ingr_arr: 
		print("{}".format(ingr))
	print("\n")

	# print instructions
	print("Instructions:")
	for inst in inst_arr: 
		print("{}".format(inst))
	print("\n")

	return

# PRINT RECIPE STEP-BY-STEP
def step_by_step(recipe):
	return