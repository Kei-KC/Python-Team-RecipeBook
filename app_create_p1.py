import tkinter as tk
from tkinter import *
import os
import json_db as db
import subprocess as sub
from tkmacosx import Button as button

# NEW WINDOW
def view():
    c_root = tk.Tk()
    c_root.title('Pythonees Recipe Book')
    c_root.resizable(False, False) # WINDOW NOT RESIZABLE
    canvas = tk.Canvas(c_root, height = "700", width = "700", bg = "#e3e398")
    canvas.pack()
    frame = tk.Frame(c_root, bg = "#FFF")
    frame.place(relheight = 0.7, relwidth = 0.7, relx = 0.5, rely = 0.5, anchor = CENTER) 

    msg = tk.Label(frame, text = "Create your own!",
                    fg = "#000", bg = "#e3e398", 
                    font = ("Consolas 15", 25, 'bold'))
    msg.place(anchor = CENTER, relx = 0.5, rely = 0.1)

    # USER INPUT (NAME)
    create_msg = tk.Label(frame, text = "Recipe Name", fg = "#000", bg = "#fff", 
                          font = ("Consolas 15", 20))
    create_msg.place(anchor = CENTER, relx = 0.5, rely = 0.2)
    to_create_name = tk.Entry(frame)
    to_create_name.place(anchor=CENTER, height=40, relx=0.5, rely=0.3)

    # USER INPUT (INGREDIENTS)
    ingr_msg = tk.Label(frame, text = "Ingredients (Add one each line)",
                        fg = "#000", bg = "#fff", font = ("Consolas 15", 20))
    ingr_msg.place(anchor = CENTER, relx = 0.5, rely = 0.4)
    # to_create_ingr = tk.Entry(frame)
    to_create_ingr = Text(frame, font=('Consolas 15', 14))
    to_create_ingr.place(anchor=CENTER, relwidth=0.4, relheight=0.1,relx=0.5, rely=0.5)

    # USER INPUT (INSTRUCTIONS)
    inst_msg = tk.Label(frame, text = "Instructions (Add one each line)",
                        fg = "#000", bg = "#fff", font = ("Consolas 15", 20))
    inst_msg.place(anchor = CENTER, relx = 0.5, rely = 0.6)
    to_create_inst = Text(frame, font=('Consolas 15', 14))
    to_create_inst.place(anchor=CENTER, relwidth=0.4, relheight=0.1, relx=0.5, rely=0.7)

    def inputs_to_list(input, delimiter):
        string = ""
        for each in input:
            string += each + delimiter
        res = [string]
        return res

    def new_recipe():
        n = to_create_name.get()
        # igr = to_create_ingr.get(1.0, END)
        igr_split = to_create_ingr.get(1.0, END).split('\n')
        igr_to_list = inputs_to_list(igr_split,",")
        # print(igr_to_list[:-1])
        # inst = to_create_inst.get(1.0, END)
        inst_split = to_create_inst.get(1.0, END).split('\n')
        inst_to_list = inputs_to_list(inst_split,";")
        db.recipe_creation(n, igr_to_list[:-1], inst_to_list[:-1])
        from app_recipe_created import recipe_created
        recipe_created(n)


    # TRIGGERED ON BUTTON CLICK
    # def get_input():
    #     return show.show_recipe(to_search.get().lower())

    # SUBMIT INPUT
    submit = button(frame, text="Add!", padx=5, pady=5, borderless=1,
                    fg="#000", bg="#ecf2c7", font=('Consolas 15', 14),
                    command=new_recipe)
    submit.place(anchor=CENTER, relx=0.5, rely=0.85)

    # BACK TO START
    def prev(): 
        c_root.destroy()
        import app
        app.root.deiconify()
        
    prev = button(canvas, text = "Previous", padx = 5, pady = 5, borderless = 1,
                        fg="#000", bg="#fff", font=('Consolas 15', 14), 
                        command = prev)
    prev.place(anchor = CENTER, relx= 0.5, rely=0.9)
