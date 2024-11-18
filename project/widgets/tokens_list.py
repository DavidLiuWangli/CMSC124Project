import tkinter as tk
from widgets.widget import Widget

class Tokens_List(Widget):
    def __init__(self, root):
        super().__init__(root)
        self.border.place(relx=0.0, rely=1.0, anchor="sw", relwidth=0.5, relheight=0.5)

