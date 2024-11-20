import tkinter as tk
from tkinter.ttk import Treeview
from widgets.widget import Widget
from widgets.ui_elements import create_styled_label

class Tokens_List(Widget):
    def __init__(self, root):
        super().__init__(root)
        self.border.place(relx=0.0, rely=1.0, anchor="sw", relwidth=0.5, relheight=0.5)
        
        # Table Headers
        tokens_list_title = create_styled_label(self.header, "Lexemes")
        tokens_list_title.pack(side=tk.TOP)
        columns = ("Lexeme", "Classification")
        self.table = Treeview(self.content, columns=columns, show="headings")
        for col in columns:
            self.table.heading(col, text=col)
        self.table.pack(fill=tk.BOTH, expand=True)
        
    def update(self, tokens):
        for row in self.table.get_children():
            self.table.delete(row)
        for token in tokens:
            self.table.insert("", tk.END, values=token)
        
    
        

