import tkinter as tk
from abc import ABC

class Widget(ABC):
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root, bg="black", bd="10", width=500, height=250)
