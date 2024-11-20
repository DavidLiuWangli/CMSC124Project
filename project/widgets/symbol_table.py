import tkinter as tk
from widgets.widget import Widget

class Symbol_Table(Widget):
    def __init__(self, root):
        super().__init__(root)
        self.border.place(relx=1.0, rely=1.0, anchor="se", relwidth=0.5, relheight=0.5)
        

