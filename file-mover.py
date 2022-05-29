import os
import shutil
import tkinter as tk
from tkinter import filedialog

root_window = tk.Tk()

canvas = tk.Canvas(root_window, width=650, height=100)
canvas.grid(columnspan=3, rowspan=3)

instructions = tk.Label(root_window, text="Browse to a folder and press the Move button to move all files in subfolders to the root of that folder", font="Raleway")
instructions.grid(columnspan=2, column=0, row=1)

def open_folder():
    browse_text.set("Loading...")
    #root_window.withdraw()
    open_folder.selected_folder = filedialog.askdirectory(initialdir = "C:/Users/Derek/Desktop/")
    #root_window.deiconify()

    text_box = tk.Text(root_window, height=50, width=80, padx=5, pady=5)

    files = os.listdir(open_folder.selected_folder)
    for file in files:
        text_box.insert(1.0, " - " + file + "\n")
    text_box.insert(1.0, open_folder.selected_folder + ":" + "\n\n")
    text_box.grid(column=0, row=3, columnspan=2)
    browse_text.set("Browse")

def move_files():
    try:
        for root, dirs, files in os.walk(open_folder.selected_folder, topdown=False):
            for file in files:
                try:
                    shutil.move(os.path.join(root, file), open_folder.selected_folder)
                except OSError:
                    pass

        text_box = tk.Text(root_window, height=50, width=80, padx=5, pady=5)

        updated_files = os.listdir(open_folder.selected_folder)
        for updated_file in updated_files:
            text_box.insert(1.0, " - " + updated_file + "\n")
        text_box.insert(1.0, open_folder.selected_folder + ":" + "\n\n")
        text_box.grid(column=0, row=3, columnspan=2)
    except AttributeError:
        print("Click the Browse button and select a folder first")

browse_text = tk.StringVar()
browse_btn = tk.Button(root_window, textvariable=browse_text, command=lambda:open_folder(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=0, row=2)

move_text = tk.StringVar()
move_btn = tk.Button(root_window, textvariable=move_text, command=lambda:move_files(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
move_text.set("Move Files")
move_btn.grid(column=1, row=2)

root_window.mainloop()