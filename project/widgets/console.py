import tkinter as tk
from widgets.widget import Widget

class Text_Editor(Widget):
    def __init__(self, root):
        super().__init__(self, root)
        self.frame.place(relx=1.0, rely=0.0, anchor="ne", relwidth=0.5, relheight=0.5)

