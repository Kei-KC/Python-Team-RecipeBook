import print_db
import tkinter as tk
from tkinter import *
from threading import Thread
from PIL import Image,ImageTk
import webbrowser # Open User Guide
from tkmacosx import Button as button # To reflect button color change on Mac OS

root = tk.Tk()
root.title('Pythonees Recipe Book')
root.resizable(False, False) # FIXED WINDOW SIZE

canvas = tk.Canvas(root, height = "700", width = "700", bg = "#EFE6D5")
canvas.pack()

frame = tk.Frame(root, bg = "#FFF")
frame.place(relheight = 0.7, relwidth = 0.7, 
                relx = 0.5, rely = 0.5, anchor = CENTER) 

# WELCOME MESSAGE
welcomeMsg = tk.Label(canvas, text = "Welcome to Pythonees Recipe Book!", 
                        fg = "#000", bg = "#e3e398", font = ("Consolas 15", 25, 'bold'))
welcomeMsg.place(anchor = CENTER, relx = 0.5, rely = 0.1)
# ----------
# VIEWALL
def viewall_btn_nextPg():
    root.withdraw()
    from app_viewall_p1 import view
    # data = print_db.print_all_menu()
    view()
    
viewAll = button(frame, text = "View All Menu", padx = 0, pady = 0, borderless = 1,
                    fg = "#000", bg = "#ecf2c7", font = ('Consolas 15', 18),
                    highlightbackground = "brown", borderwidth = 0, 
                    command = viewall_btn_nextPg)
viewAll.place(anchor = CENTER, relx = 0.5, rely = 0.2, relheight = 0.1, relwidth = 0.7)
# ----------
# SEARCH
def search_btn_nextPg():
    root.withdraw()
    from app_search_p1 import view
    view()
search = button(frame, text = "Search Recipe",
                    padx = 0, pady = 0, borderless = 1,
                    fg = "#000", bg = "#ecf2c7", font = ('Consolas 15', 18),
                    highlightbackground = "#EFE6D5",
                    command = search_btn_nextPg)
search.place(anchor = CENTER, relx = 0.5, rely = 0.4, relheight = 0.1, relwidth = 0.7)
# ----------
# CREATE 
def create_btn_nextPg():
    root.withdraw()
    from app_create_p1 import view
    view()
create = button(frame, text = "Create Recipe", padx = 0, pady = 0, borderless = 1,
                    fg="#000", bg="#ecf2c7", font=('Consolas 15', 18),
                    command = create_btn_nextPg)
create.place(anchor = CENTER, relx = 0.5, rely = 0.6, relheight = 0.1, relwidth = 0.7)
# ----------
# USER GUIDE 
def guide_btn_nextPg():
    webbrowser.open_new("https://pythonees-recipe-book.atlassian.net/l/cp/rLSbF7WG")
create = button(frame, text = "User Guide", padx = 0, pady = 0, borderless = 1,
                    fg="#000", bg = "#ecf2c7", font=('Consolas 15', 18),
                    command = guide_btn_nextPg)
create.place(anchor = CENTER, relx = 0.5, rely = 0.8, relheight = 0.1, relwidth = 0.7)
# ----------
# EXIT 
def exit():
    root.destroy()
exit = button(canvas, text = "X", padx = 0, pady = 0, borderless = 1, borderwidth = 0,
                fg = "#000", bg = "#fff", font = ('Consolas 15', 18),
                command = exit)
exit.place(anchor = CENTER, relx = 0.5, rely = 0.9, relheight = 0.05, relwidth = 0.1)
# ----------

root.mainloop()