import tkinter as tk
from tkinter import *
import os
import print_db
import subprocess as sub
from PIL import Image,ImageTk
from tkmacosx import Button as button

# BASIC COMPONENTS
s_root = tk.Tk()
s_root.title('Pythonees Recipe Book')
s_root.resizable(False, False) # WINDOW NOT RESIZABLE
canvas = tk.Canvas(s_root, height = "700", width = "700", bg = "#e3e398")
canvas.pack()
frame = tk.Frame(s_root, bg = "#FFF")
frame.place(relheight = 0.7, relwidth = 0.7, relx = 0.5, rely = 0.5, anchor = CENTER) 

msg = tk.Label(frame, text = "Which recipe would you like to search?",
                fg = "#000", bg = "#e3e398", 
                font = ("Consolas 15", 25, 'bold'))
msg.place(anchor = CENTER, relx = 0.5, rely = 0.1)

# BACK TO START
def prev(): 
    s_root.destroy()
    import app
    app.root.deiconify()
    app.root.lift()
    app.root.focus_force()
    # img = ImageTk.PhotoImage(Image.open("canvas-bg.png"))
    # app.canvas.create_image(700/2, 700/2, anchor = CENTER,image = img)
     
prev = button(canvas, text = "Previous", padx = 5, pady = 5, bd = 0,
                    fg="#000", bg="#fff", font=('Consolas 15', 14), 
                    command = prev)
prev.place(anchor = CENTER, relx= 0.5, rely=0.9)
