import tkinter as tk
from tkinter import *
import os
import print_db
from tkmacosx import Button as button

# NEW WINDOW
def view(data):
    v_root = tk.Tk()
    v_root.title('Pythonees Recipe Book')
    v_root.resizable(False, False) # window not resizable
    canvas = tk.Canvas(v_root, height = "700", width = "700", bg = "#e3e398").pack()
    frame = tk.Frame(v_root, bg = "#FFF")
    frame.place(relheight = 0.7, relwidth = 0.7, relx = 0.5, rely = 0.5, anchor = CENTER) 

    menu_msg = tk.Label(canvas, text = "Pythonees Menu", bg = "#e3e398",
                        fg = "#000", font = ("Consolas 15", 25, 'bold'))
    menu_msg.place(anchor = CENTER, relx = 0.5, rely = 0.1)
    select_msg = tk.Label(frame, text = "Select one to view the recipe!", bg = "#fff",
                          fg = "#000", font = ("Consolas 15", 20, 'bold'))
    select_msg.place(anchor = CENTER, relx = 0.5, rely = 0.1)

    # SHOW RECIPE
    def show_recipe(recipe):
        v_root = tk.Tk()
        v_root.title('Pythonees Recipe Book')
        v_root.resizable(False, False) 
        canvas = tk.Canvas(v_root, height = "700", width = "700", bg = "#e3e398")
        canvas.pack()
        frame = tk.Frame(v_root, bg = "#FFF")
        frame.place(relheight = 0.7, relwidth = 0.7, relx = 0.5, rely = 0.5, anchor = CENTER) 
        
        names, ingredients, instructions = print_db.print_whole(menu_list[0])
        name = tk.Label(frame, text = names,
                    fg = "#000", bg = "#e3e398", 
                    font = ("Consolas 15", 25, 'bold'))
        name.place(anchor = CENTER, relx = 0.5, rely = 0.1)

    # PRINT ALL MENU
    menu_list = list(data.values()) # list of menus
    m_bg = "#fff"
    m_font_color = "#000"
    m_font_style = ("Consolas 15", 25, 'bold')
    menu1 = tk.Label(frame, text = menu_list[0].capitalize(), 
                     bg = m_bg, fg = m_font_color, font = m_font_style)
    menu1.place(anchor = CENTER, relx = 0.5, rely = 0.3)
    # menu1.bind("<Button>", show_recipe(menu_list[0]))

    menu2 = tk.Label(frame, text = menu_list[1].capitalize(), 
                     bg = m_bg, fg = m_font_color, font = m_font_style)
    menu2.place(anchor = CENTER, relx = 0.5, rely = 0.4)

    menu3 = tk.Label(frame, text = menu_list[2].capitalize(), 
                     bg = m_bg, fg = m_font_color, font = m_font_style)
    menu3.place(anchor = CENTER, relx = 0.5, rely = 0.5)

    menu4 = tk.Label(frame, text = menu_list[3].capitalize(), 
                     bg = m_bg, fg = m_font_color, font = m_font_style)
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

