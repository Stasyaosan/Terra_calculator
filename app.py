import tkinter as tk
from tkinter import ttk
from config import WINDOW, TITLE


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry(WINDOW)
        self.root.title(TITLE)
        self.create_widgets()
        self.setup_widgets()

    def create_widgets(self):
        self.frame_input = tk.Frame()
        self.input_field = tk.Entry(self.frame_input, font='Arial 15 bold', width=24, state='readonly')

        buttons = (('7', '8', '9', '/', '4'),
                   ('4', '5', '6', '*', '4'),
                   ('1', '2', '3', '-', '4'),
                   ('0', '.', '=', '+', '4')
                   )

        for row in range(4):
            for col in range(4):
                tk.Button(root, width=2, height=3, text=buttons[row][col],
                          command=lambda row=row, col=col: self.btn_click(buttons[row][col])).grid(row=row + 2,
                                                                                                   column=col,
                                                                                                   sticky="nsew",
                                                                                                   padx=1,
                                                                                                   pady=1)

    def setup_widgets(self):
        self.frame_input.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.input_field.pack(fill=tk.BOTH)

    def btn_click(self):
        pass


root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
