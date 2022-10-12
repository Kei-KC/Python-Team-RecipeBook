import json
import pandas as pd
import difflib

columns = ['name', 'ingredients', 'instructions']

def recipe_creation(name, ingredients, instructions):
    df = pd.read_csv('recipe_book.csv', names=columns)
    if name in df['name'].values:
        return
    recipe = {
        'name':name,
        'ingredients':ingredients,
        'instructions':instructions
    }
    df = pd.DataFrame(recipe)
    #print(df)
    df.to_csv('recipe_book.csv', mode='a', index=False, header=False)

def recipe_search(search_term):
    df = pd.read_csv('recipe_book.csv', names=columns)
    if search_term in df['name'].values:
        return df.query("name == @search_term")
    return False

def fuzzy_search(search_term):
    df = pd.read_csv('recipe_book.csv', names=columns)
    match = difflib.get_close_matches(search_term, df['name'].tolist(), n=4, cutoff=0.6)
    return match

def ingredient_search(ingredient):
    df = pd.read_csv('recipe_book.csv', names=columns)
    return df[ingredient in df['ingredients']]
