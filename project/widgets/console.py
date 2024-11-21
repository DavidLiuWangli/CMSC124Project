import tkinter as tk
from widgets.widget import Widget
from widgets.ui_elements import create_styled_label, create_styled_button
from lexical_analyzer.lexical_analyzer import lexical_analyzer
from syntax_analyzer.syntax_analyzer import syntax_analyzer

class Console(Widget):
    def __init__(self, root, text_editor, tokens_table, symbol_table):
        super().__init__(root)
        self.border.place(relx=1.0, rely=0.0, anchor="ne", relwidth=0.5, relheight=0.5)
        
        # Other Widgets References
        self.text_editor = text_editor
        self.tokens_table = tokens_table
        self.symbol_table = symbol_table
        
        # Title and Buttons
        title = create_styled_label(self.header, "Console")
        title.pack(side=tk.LEFT)
        parse_button = create_styled_button(self.header, "Parse", self.parse)
        parse_button.pack(side=tk.RIGHT)
        run_button = create_styled_button(self.header, "Run", self.run)
        run_button.pack(side=tk.RIGHT)
        
        # Console Output
        self.text_area = scrolledtext.ScrolledText(
            self.content, 
            fg="white", 
            font=("Consolas", 12), 
            bg="black",
            insertbackground="white",
            wrap="none",
            undo=True)
        tab_size = font.Font(font=self.text_area["font"]).measure("    ")  # Measure 4 spaces
        self.text_area.config(tabs=(tab_size,))
        self.text_area.config(state="disabled")
        self.text_area.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    
    def parse(self):
        self.text_area.config(state="normal")
        self.text_area.delete("1.0", tk.END)
        parse_tree = syntax_analyzer(self.text_editor.text_area.get("1.0", "end-1c"))
        self.text_area.insert(tk.END, parse_tree)
        self.text_area.config(state="disabled")
    
    def run(self):
        tokens = lexical_analyzer(self.text_editor.text_area.get("1.0", "end-1c"))
        self.tokens_table.update(tokens)
        # symbol table update
