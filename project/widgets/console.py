import tkinter as tk
from widgets.widget import Widget

class Console(Widget):
    def __init__(self, root):
        super().__init__(root)
        self.border.place(relx=1.0, rely=0.0, anchor="ne", relwidth=0.5, relheight=0.5)

