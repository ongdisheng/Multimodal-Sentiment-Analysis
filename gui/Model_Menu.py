# import libraries
from tkinter import *

from Label import Label

class Model_Menu:
    # models used
    OPTIONS = [
        "EF-LSTM",
        "LMF",
        "MFN",
        "CM-BERT (w/o Visual)",
        "CM-BERT (w/ Visual)"
    ]
    CURRENT_OPTION = OPTIONS[0]


    def __init__(self, window):
        self.value = StringVar()                        # datatype of menu text
        self.value.set(Model_Menu.CURRENT_OPTION)       # initial menu text
        self.window = window

    def create(self, x, y):
        menu = OptionMenu(
            self.window, self.value, *(Model_Menu.OPTIONS),
            command=lambda _: self.update(self.value)
        )
        menu.pack()
        menu.place(x=x, y=y)

        # model label
        label = Label(self.window, "Model")
        label.create(x=165, y=280)
    
    def update(self, value):
        Model_Menu.CURRENT_OPTION = value.get()