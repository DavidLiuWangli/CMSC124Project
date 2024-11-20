import tkinter as tk
from widgets.console import Console
from widgets.symbol_table import Symbol_Table
from widgets.text_editor import Text_Editor
from widgets.tokens_list import Tokens_List

# Window
root = tk.Tk()
root.title("Lolcode Interpreter")
root.geometry("1000x500")
root.configure(bg="black")

# Widgets
Console(root)
Symbol_Table(root)
Text_Editor(root)
Tokens_List(root)

# Run application
root.mainloop()
