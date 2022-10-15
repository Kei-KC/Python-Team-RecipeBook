import tkinter as tk
from tkinter import *
from tkmacosx import Button as button

def recipe_created(new_recipe):
    root = tk.Tk()
    root.title('Pythonees Recipe Book')
    root.resizable(False, False) # WINDOW NOT RESIZABLE
    canvas = tk.Canvas(root, height = "700", width = "700", bg = "#e3e398")
    canvas.pack()
    frame = tk.Frame(root, bg = "#FFF")
    frame.place(relheight = 0.7, relwidth = 0.7, relx = 0.5, rely = 0.5, anchor = CENTER) 

    msg = tk.Label(frame, text = new_recipe.capitalize() + "\nhas been successfully created!",
                    fg = "#000", bg = "#e3e398", 
                    font = ("Consolas 15", 25, 'bold'))
    msg.place(anchor = CENTER, relx = 0.5, rely = 0.5)