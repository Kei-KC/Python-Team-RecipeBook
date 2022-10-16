import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkmacosx import Button as button
import app_show_recipe as show

# NEW WINDOW
def view():
    s_root = tk.Tk()
    s_root.title('Pythonees Recipe Book')
    s_root.resizable(False, False)  # WINDOW NOT RESIZABLE
    canvas = tk.Canvas(s_root, height="700", width="700", bg="#e3e398")
    canvas.pack()
    frame = tk.Frame(s_root, bg="#FFF")
    frame.place(relheight=0.7, relwidth=1, relx=0.5, rely=0.5, anchor=CENTER)

    msg = tk.Label(frame, text="Which recipe would you like to search?",
                   fg="#000", bg="#fff",
                   font=("Consolas 15", 25, 'bold'))
    msg.place(anchor=CENTER, relx=0.5, rely=0.1)

    # USER INPUT
    to_search = tk.Entry(frame)
    to_search.place(anchor=CENTER, height=50, relx=0.5, rely=0.4)

    # TRIGGERED ON BUTTON CLICK
    def get_input():
        return show.show_recipe(to_search.get().lower())

    # SUBMIT INPUT
    submit = button(frame, text="Go!", padx=5, pady=5, borderless=1,
                    fg="#000", bg="#ecf2c7", font=('Consolas 15', 14),
                    command=get_input)
    submit.place(anchor=CENTER, relx=0.5, rely=0.6)

    # BACK TO START
    def prev():
        s_root.destroy()
        import app
        app.root.deiconify()
    prev = button(canvas, text="Previous", padx=5, pady=5, borderless=1,
                  fg="#000", bg="#fff", font=('Consolas 15', 14),
                  command=prev)
    prev.place(anchor=CENTER, relx=0.5, rely=0.9)
