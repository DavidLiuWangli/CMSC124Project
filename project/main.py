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
text_editor = Text_Editor(root)
tokens_list = Tokens_List(root)
symbol_table = Symbol_Table(root)
Console(root, text_editor, tokens_list, symbol_table)

# Run application
root.mainloop()
