import tkinter as tk
from tkinter import *
import os
import print_db
from tkmacosx import Button as button

# BASIC COMPONENTS
def view(data):
    v_root = tk.Tk()
    v_root.title('Pythonees Recipe Book')
    v_root.resizable(False, False) # WINDOW NOT RESIZABLE
    canvas = tk.Canvas(v_root, height = "700", width = "700", bg = "#e3e398")
    canvas.pack()
    frame = tk.Frame(v_root, bg = "#FFF")
    frame.place(relheight = 0.7, relwidth = 0.7, relx = 0.5, rely = 0.5, anchor = CENTER) 

    menu_msg = tk.Label(frame, text = "Pythonees Menu",
                    fg = "#000", bg = "#e3e398", 
                    font = ("Consolas 15", 25, 'bold'))
    menu_msg.place(anchor = CENTER, relx = 0.5, rely = 0.1)
    select_msg = tk.Label(frame, text = "Select a menu to view recipe!",
                    fg = "#000", bg = "#e3e398", 
                    font = ("Consolas 15", 25, 'bold'))
    select_msg.place(anchor = CENTER, relx = 0.5, rely = 0.1)

    # PRINT ALL MENU
    menu_list = list(data.values()) # LIST OF MENUS
    menu1 = tk.Label(frame, text = menu_list[0].capitalize(), 
                     bg = "#fff", fg = "#000",
                     font = ("Consolas 15", 25, 'bold'))
    menu1.place(anchor = CENTER, relx = 0.5, rely = 0.3)

    menu2 = tk.Label(frame, text = menu_list[1].capitalize(), 
                     bg = "#fff", fg = "#000",
                     font = ("Consolas 15", 25, 'bold'))
    menu2.place(anchor = CENTER, relx = 0.5, rely = 0.4)

    menu3 = tk.Label(frame, text = menu_list[2].capitalize(), 
                     bg = "#fff", fg = "#000",
                     font = ("Consolas 15", 25, 'bold'))
    menu3.place(anchor = CENTER, relx = 0.5, rely = 0.5)

    menu4 = tk.Label(frame, text = menu_list[3].capitalize(), 
                     bg = "#fff", fg = "#000",
                     font = ("Consolas 15", 25, 'bold'))
    menu4.place(anchor = CENTER, relx = 0.5, rely = 0.6)

    # BACK TO START
    def prev(): 
        v_root.destroy()
        import app
        app.root.deiconify()
        
        
    prev = button(canvas, text = "Previous", padx = 5, pady = 5, borderless = 1,
                        fg="#000", bg="#fff", font=('Consolas 15', 14),
                        command = prev)
    prev.place(anchor = CENTER, relx= 0.5, rely=0.9)
