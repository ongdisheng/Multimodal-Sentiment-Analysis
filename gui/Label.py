# import libraries
import tkinter as tk

class Label:
    def __init__(self, window, text, font="Helvetica", bg="white", fg="#000000"):
        self.window = window
        self.text = text
        self.font = font
        self.bg = bg
        self.fg = fg
    
    def create(self, x, y):
        self.label = tk.Label(
            self.window, text=self.text, font=self.font, bg=self.bg, fg=self.fg
        )
        self.label.place(x=x, y=y)
        return self.label