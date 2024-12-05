import tkinter as tk
from tkinter import ttk
from widgets.widget import Widget
from widgets.ui_elements import create_styled_label

class Entries_Table(Widget):
    def __init__(self, root):
        super().__init__(root)
        
    def create_table(self, title, columns):
        tokens_list_title = create_styled_label(self.header, title)
        tokens_list_title.pack(side=tk.TOP)
        
        style = ttk.Style()
        style = ttk.Style()
        style.configure("Treeview.Heading", 
                        font=("Consolas", 12), 
                        )
        style.configure("Treeview", 
                        foreground="white",  
                        background="black", 
                        fieldbackground="black",
                        font=("Consolas", 12), 
                        )

        self.table = ttk.Treeview(self.content, columns=columns, show="headings")
        for col in columns:
            self.table.heading(col, text=col)
        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(self.content, command=self.table.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.config(yscrollcommand=scrollbar.set)
    
    def update(self, entries):
        for row in self.table.get_children():
            self.table.delete(row)
        for entry in entries:
            self.table.insert("", tk.END, values=entry)
    
