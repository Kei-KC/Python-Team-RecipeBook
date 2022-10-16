import tkinter as tk
from tkinter import *
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

    def get_recipe(recipe):
        from json_db import recipe_search
        recipe_result = recipe_search(recipe)
        if recipe_result is not False:
            print("recipe", recipe)
            return recipe_result
        else:
            error = tk.Label(frame, text="Oops\n"+recipe+" does not exist!\nReturn to previous page to try again.", 
                        fg="#000", bg="#e3e398",
                        font=("Consolas 15", 25, 'bold'))
            error.place(anchor=CENTER, relx=0.5, rely=0.5)
            def prev():
                v_root.destroy()
            prev = button(canvas, text="Previous", padx=5, pady=5, borderless=1,
                  fg="#000", bg="#fff", font=('Consolas 15', 14),
                  command=prev)
            prev.place(anchor=CENTER, relx=0.5, rely=0.9)
        

    recipe_got = get_recipe(recipe)
    print("type", type(recipe_got))
    name = recipe_got["name"].values[0]
    names = {}
    names[name] = ""

    ingredient_arr = recipe_got["ingredients"].values[0].split(",")
    ingredients = {}
    for ingr in ingredient_arr:
        ingredients[ingr] = ""

    instruction_arr = recipe_got["instructions"].values[0].split(";")
    instructions = {}
    for inst in instruction_arr:
        instructions[inst] = ""    
    
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
    ingredient.place(anchor=CENTER, relx=0.5, rely=0.35)

    # print instructions
    i = 1
    instruction_all = ""
    while i <= len(instructions):
        for key in instructions.keys():
            instruction_all += key + "\n"
            i += 1
    instruction = tk.Label(frame, text="[ Instructions ]\n" + instruction_all,
                           fg="#000", bg="#fff", font=("Consolas 15", 18, 'bold'))
    instruction.place(anchor=CENTER, relx=0.5, rely=0.73)

    # def exit():
    #     v_root.destroy()
    # exit = button(canvas, text = "X", padx = 0, pady = 0, borderless = 1, borderwidth = 0,
    #                 fg = "#000", bg = "#fff", font = ('Consolas 15', 18),
    #                 command = exit)
    # exit.place(anchor = CENTER, relx = 0.5, rely = 0.9, relheight = 0.05)

    def prev():
        v_root.destroy()
        # import app
        # app.root.deiconify()
    prev = button(canvas, text="Previous", padx=5, pady=5, borderless=1,
                  fg="#000", bg="#fff", font=('Consolas 15', 14),
                  command=prev)
    prev.place(anchor=CENTER, relx=0.5, rely=0.9)
