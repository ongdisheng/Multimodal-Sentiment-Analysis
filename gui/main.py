# import libraries
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

from Dataset_Menu import Dataset_Menu
from Model_Menu import Model_Menu
from Test_Result import Test_Result


def run():
    """
    Start GUI application
    """
    # create main window
    window = tk.Tk()
    window.configure(background="white")    # background
    window.geometry("800x600")              # size
    window.title("GUI")                     # title

    # add image
    frame = tk.Frame(window)
    frame.place(x=185, y=125)
    img = Image.open("./image/image.jpg")
    # img = Image.open("./image/anime.jpg")
    img = img.resize((170,100))
    img = ImageTk.PhotoImage(img)
    label = tk.Label(frame, image=img)
    label.configure(image=img)
    label.img = img
    label.pack()

    # create dropdown menu (dataset)
    dataset_menu = Dataset_Menu(window)
    dataset_menu.create(x=265, y=240)

    # create dropdown menu (model)
    model_menu = Model_Menu(window)
    model_menu.create(x=265, y=280)

    # show test result panel
    test_result = Test_Result(window, dataset_menu, model_menu)
    test_result.show()

    return window


if __name__ == "__main__":
    run().mainloop()