import tkinter as tk
from config import WINDOW, TITLE


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry(WINDOW)
        self.root.title(TITLE)
        self.create_widgets()

    def create_widgets(self):
        pass
