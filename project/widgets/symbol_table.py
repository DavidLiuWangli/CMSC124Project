import tkinter as tk
from tkinter.ttk import Treeview
from widgets.entries_table import Entries_Table
from widgets.ui_elements import create_styled_label

class Symbol_Table(Entries_Table):
    def __init__(self, root):
        super().__init__(root)
        self.border.place(relx=1.0, rely=1.0, anchor="se", relwidth=0.5, relheight=0.5)
        self.create_table("Symbols", ("Identifier", "Value"))