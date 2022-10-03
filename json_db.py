import json
import pandas 

def recipe_creation(name, ingredients, instructions):
    df = pd.read_csv('recipe_book.csv')
    if name in df['name'].values:
        return
    recipe = {'name':name,'ingredients':ingredients,'instructions':instructions}
    df.append(recipe)
    df.to_csv('recipe_book.csv')

def recipe_search(search_term):
    df = pd.read_csv('recipe_book.csv')
    if search_term in df['name'].values:
        return df.query('name' == search_term)
    return False;