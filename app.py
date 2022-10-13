import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import subprocess as sub
import os
import print_db
from threading import Thread
import webbrowser

root = tk.Tk()
root.title('Pythonees Recipe Book')
root.resizable(False, False) # FIXED WINDOW SIZE

canvas = tk.Canvas(root, height = "700", width = "700", 
                        bg = "#EFE6D5")
canvas.pack()

# LOAD IMAGE
img = ImageTk.PhotoImage(Image.open("canvas-bg.png"))
# ADD IMAGE
canvas.create_image(700/2, 700/2, anchor = CENTER,image = img)

frame = tk.Frame(root, bg = "#FFF")
frame.place(relheight = 0.7, relwidth = 0.7, 
                relx = 0.5, rely = 0.5, anchor = CENTER) 

# WELCOME MESSAGE
welcomeMsg = tk.Label(canvas, text = "Welcome to the Pythonees Recipe Book!", 
                        fg = "#000", bg = "#e3e398", font = ("Consolas 15", 20, 'bold'))
welcomeMsg.place(anchor = CENTER, relx = 0.5, rely = 0.1)

# VIEWALL
def viewall_btn_nextPg():
    root.withdraw()
    import app_viewall_p1
    print_db.print_all_menu()
    
viewAll = tk.Button(frame, text = "View All Menu", padx = 5, pady = 5, 
                    fg = "#000", bg = "gray", font = ('Consolas 15', 14),
                    command = viewall_btn_nextPg)
viewAll.place(anchor = CENTER, relx = 0.5, rely =0.2)

# SEARCH
def search_btn_nextPg():
    root.withdraw()
    import app_search_p1 
search = tk.Button(frame, text = "Search Recipe", padx = 5, pady = 5, 
                        fg = "#000", bg = "gray", font = ('Consolas 15', 14),
                        command = search_btn_nextPg)
search.place(anchor = CENTER, relx= 0.5, rely=0.4)

# CREATE 
def create_btn_nextPg():
    root.withdraw()
    import app_create_p1
create = tk.Button(frame, text = "Create Recipe", padx = 5, pady = 5, 
                    fg="#000", bg="gray", font=('Consolas 15', 14),
                    command = create_btn_nextPg)
create.place(anchor = CENTER, relx= 0.5, rely=0.6)

# USER GUIDE 
def guide_btn_nextPg():
    webbrowser.open_new("https://pythonees-recipe-book.atlassian.net/l/cp/rLSbF7WG")
create = tk.Button(frame, text = "User Guide", padx = 5, pady = 5, 
                    fg="#000", bg="gray", font=('Consolas 15', 14),
                    command = guide_btn_nextPg)
create.place(anchor = CENTER, relx= 0.5, rely=0.8)

# EXIT 
def exit():
    root.destroy()
exit = tk.Button(canvas, text = "Close Book", padx = 5, pady = 5, 
                fg = "#000", bg = "gray", font = ('Consolas 15', 14),
                command = exit)
exit.place(anchor = CENTER, relx = 0.5, rely = 0.9)
    
root.mainloop()