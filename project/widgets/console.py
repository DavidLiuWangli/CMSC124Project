import tkinter as tk
from widgets.widget import Widget
from widgets.ui_elements import create_styled_label, create_styled_button
from lexical_analyzer.lexical_analyzer import lexical_analyzer

class Console(Widget):
    def __init__(self, root, text_editor, tokens_list, symbol_table):
        super().__init__(root)
        self.border.place(relx=1.0, rely=0.0, anchor="ne", relwidth=0.5, relheight=0.5)
        
        # Other Widgets References
        self.text_editor = text_editor
        self.tokens_list = tokens_list
        self.symbol_table = symbol_table
        
        # Title and Run Button
        title = create_styled_label(self.header, "Console")
        title.pack(side=tk.LEFT)
        run_button = create_styled_button(self.header, "Run", self.run)
        run_button.pack(side=tk.RIGHT)
        
    def run(self):
        tokens = lexical_analyzer(self.text_editor.text_area.get("1.0", "end-1c"))
        self.tokens_list.update(tokens)
        # symbol table update
