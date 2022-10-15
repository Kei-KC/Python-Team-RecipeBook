import tkinter as tk
from tkinter import *
import os
import print_db
from tkmacosx import Button as button


def show_recipe(recipe):
    v_root = tk.Tk()
    v_root.title('Pythonees Recipe Book')
    v_root.resizable(False, False)
    canvas = tk.Canvas(v_root, height="700", width="700", bg="#e3e398")
    canvas.pack()
    frame = tk.Frame(v_root, bg="#FFF")
    frame.place(relheight=0.7, relwidth=1,
                relx=0.5, rely=0.5, anchor=CENTER)

    names, ingredients, instructions = print_db.get_recipe(recipe)

    # print recipe name
    for key in names:
        recipe_name = key.capitalize() + " Recipe"
    name = tk.Label(frame, text=recipe_name, fg="#000", bg="#e3e398",
                    font=("Consolas 15", 25, 'bold'))
    name.place(anchor=CENTER, relx=0.5, rely=0.1)

    # print ingredients
    i = 1
    ingredient_all = ""
    while i <= len(ingredients):
        for key in ingredients.keys():
            ingredient_all += str(i) + ". " + key + "\n"
            i += 1
    ingredient = tk.Label(frame, text="[ Ingredients ]\n" + ingredient_all,
                          fg="#000", bg="#fff", font=("Consolas 15", 18, 'bold'))
    ingredient.place(anchor=CENTER, relx=0.5, rely=0.4)

    # print instructions
    i = 1
    instruction_all = ""
    while i <= len(instructions):
        for key in instructions.keys():
            instruction_all += key + "\n"
            i += 1
    instruction = tk.Label(frame, text="[ Instructions ]\n" + instruction_all,
                           fg="#000", bg="#fff", font=("Consolas 15", 18, 'bold'))
    instruction.place(anchor=CENTER, relx=0.5, rely=0.7)

    ask = tk.Label(frame, )
