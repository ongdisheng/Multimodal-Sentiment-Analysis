# import libraries
import tkinter as tk

from Label import Label
from Button import Button

class Test_Result:
    def __init__(self, window, dataset_menu, model_menu):
        self.window = window
        self.dataset_menu = dataset_menu
        self.model_menu = model_menu
    
    def show(self):
        # test result label
        test_result = Label(self.window, "Test Result")
        test_result.create(x=520, y=120)
        
        # accuracy 7 label
        acc7_label = Label(self.window, "Acc7: ")
        acc7_label.create(x=520, y=180)
        acc7_value = Label(self.window, "")
        acc7_value = acc7_value.create(x=620, y=181)

        # accuracy 2 label
        acc2_label = Label(self.window, "Acc2: ")
        acc2_label.create(x=520, y=220)
        acc2_value = Label(self.window, "")
        acc2_value = acc2_value.create(x=620, y=221)

        # f1 label
        f1_label = Label(self.window, "F1: ")
        f1_label.create(x=520, y=260)
        f1_value = Label(self.window, "")
        f1_value = f1_value.create(x=620, y=261)

        # mae label
        mae_label = Label(self.window, "MAE: ")
        mae_label.create(x=520, y=300)
        mae_value = Label(self.window, "")
        mae_value = mae_value.create(x=620, y=301)

        # corr label
        corr_label = Label(self.window, "Corr: ")
        corr_label.create(x=520, y=340)
        corr_value = Label(self.window, "")
        corr_value = corr_value.create(x=620, y=341)

        # accuracy 5 label
        acc5_label = Label(self.window, "Acc5: ")
        acc5_label.create(x=520, y=380)
        acc5_value = Label(self.window, "")
        acc5_value = acc5_value.create(x=620, y=381)

        # dump values
        values = [acc7_value, acc2_value, f1_value, mae_value, corr_value, acc5_value]

        # test button
        test_btn = Button(self.window)
        Test_Btn = tk.Button(
            test_btn.window,
            text="     Test     ",
            bg="blue",
            fg="white",
            command=lambda: test_btn.test(values, self.dataset_menu.CURRENT_OPTION, self.model_menu.CURRENT_OPTION)
        )
        Test_Btn.place(x=265, y=325)

       