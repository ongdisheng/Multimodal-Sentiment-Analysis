# import libraries
from tkinter import *
import tkinter as tk

from Label import Label

class Dataset_Menu:
    # datasets used
    OPTIONS = [
        "CMU-MOSI",
        "CMU-MOSEI",
        "CH-SIMS"
    ]
    CURRENT_OPTION = OPTIONS[0]

    def __init__(self, window):
        self.value = StringVar()                        # datatype of menu text
        self.value.set(Dataset_Menu.CURRENT_OPTION)     # initial menu text
        self.window = window
    
    def create(self, x, y):
        menu = OptionMenu(
            self.window, self.value, *(Dataset_Menu.OPTIONS),
            command=lambda _: self.update(self.value)
        )
        menu.pack()
        menu.place(x=x, y=y)

        # dataset label
        label = Label(self.window, "Dataset")
        label.create(x=165, y=240)
    
    def update(self, value):
        Dataset_Menu.CURRENT_OPTION = value.get()