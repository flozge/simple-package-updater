#!/usr/bin/env python

from tkinter import *
from tkinter import messagebox, Menu
import os

def button_action():
    os.system('sudo -S pacman -Syu')
    update_button.config(text="Up-to-date!")

def action_get_info_dialog():
    I_text = "\
************************\n\
Author: Florian König\n\
Date: 29.09.19\n\
Version: 1.00\n\
************************"
    messagebox.showinfo(message=I_text, title = "Informations")

fenster = Tk()
fenster.title("Package-Updater")

menubar = Menu(fenster)

help_menu = Menu(menubar, tearoff=0)

help_menu.add_command(label="Info!", command=action_get_info_dialog)

menubar.add_cascade(label="Help", menu=help_menu)

fenster.config(menu=menubar
               )
update_label = Label(fenster, text="Click on update to get the latest package versions.",)
update_button = Button(fenster, text="update", command=button_action)

exit_button = Button(fenster, text="exit", command=fenster.quit)

update_label.pack()
update_button.pack()
exit_button.pack()

fenster.mainloop()