import tkinter as tk
from abc import ABC

class Widget(ABC):
    def __init__(self, root):
        self.root = root
        self.border = tk.Frame(self.root, bg="white")
        self.content = tk.Frame(self.border, bg="black", bd=10)
        self.content.pack(padx=2, pady=2, expand=True, fill=tk.BOTH)
        
        # Header Bar
        self.header = tk.Frame(self.content, bg="black")
        self.header.pack(fill=tk.X, side=tk.TOP)
        # Line Divider
        divider = tk.Frame(self.content, bg="white", height=4)
        divider.pack(fill=tk.X, side=tk.TOP)
    
