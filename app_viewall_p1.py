import pandas as pd
import tkinter as tk
from tkinter import *
from tkmacosx import Button as button
import app_show_recipe as show

# NEW WINDOW
def view():
    v_root = tk.Tk()
    v_root.title('Pythonees Recipe Book')
    v_root.resizable(False, False)  # window not resizable
    canvas = tk.Canvas(v_root, height="700", width="700", bg="#e3e398")
    canvas.pack()
    frame = tk.Frame(v_root, bg="#FFF")
    frame.place(relheight=0.7, relwidth=1, relx=0.5, rely=0.5, anchor=CENTER)

    menu_msg = tk.Label(canvas, text="Pythonees Menu", bg="#e3e398",
                        fg="#000", font=("Consolas 15", 25, 'bold'))
    menu_msg.place(anchor=CENTER, relx=0.5, rely=0.1)
    select_msg = tk.Label(frame, text="Select to view the recipe!", bg="#fff",
                          fg="#000", font=("Consolas 15", 20, 'bold'))
    select_msg.place(anchor=CENTER, relx=0.5, rely=0.1)

    def get_menus():
        df = pd.read_csv('recipe_book.csv')
        data = {}
        for idx, recipes in df.iterrows():
            name = recipes['name']
            data[idx+1] = name
        menu_list = list(data.values())
        return menu_list

    # PRINT ALL MENU
    menu_list = get_menus()
    m_bg = "#fff"
    m_font_color = "#000"
    m_font_style = ("Consolas 15", 25, 'bold')

    menu1 = button(frame, text=menu_list[0].capitalize(), borderless=1,
                     bg=m_bg, fg=m_font_color, font=m_font_style,
                     command=show.show_recipe(menu_list[0])
                     )
    menu1.place(anchor=CENTER, relx=0.5, rely=0.3)

    menu2 = button(frame, text=menu_list[1].capitalize(), borderless=1,
                     bg=m_bg, fg=m_font_color, font=m_font_style,
                     command=show.show_recipe(menu_list[1])
                     )
    menu2.place(anchor=CENTER, relx=0.5, rely=0.4)

    menu3 = button(frame, text=menu_list[2].capitalize(), borderless=1,
                     bg=m_bg, fg=m_font_color, font=m_font_style,
                     command=show.show_recipe(menu_list[2])
                     )
    menu3.place(anchor=CENTER, relx=0.5, rely=0.5)

    menu4 = button(frame, text=menu_list[3].capitalize(), borderless=1,
                     bg=m_bg, fg=m_font_color, font=m_font_style,
                     command=show.show_recipe(menu_list[3])
                     )
    menu4.place(anchor=CENTER, relx=0.5, rely=0.6)

    # BACK TO START
    def prev():
        v_root.destroy()
        import app
        app.root.deiconify()

    prev = button(canvas, text="Previous", padx=5, pady=5, borderless=1,
                  fg="#000", bg="#fff", font=('Consolas 15', 14),
                  command=prev)
    prev.place(anchor=CENTER, relx=0.5, rely=0.9)
