import tkinter as tk
from tkinter import font
from tkinter import scrolledtext
from widgets.widget import Widget
from widgets.ui_elements import create_styled_label, create_styled_button
from lexical_analyzer.lexical_analyzer import lexical_analyzer
from syntax_semantic_analyzer.syntax_semantic_analyzer import syntax_semantic_analyzer, typecast_string

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
        run_button = create_styled_button(self.header, "Run", self.run)
        run_button.pack(side=tk.RIGHT)
        clear_button = create_styled_button(self.header, "Clear", self.clear)
        clear_button.pack(side=tk.RIGHT)
        
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
        self.text_area.config(wrap="word")
    
    def run(self):
        code = self.text_editor.text_area.get("1.0", "end")
        file_name = self.text_editor.get_file_name()
        
        tokens = lexical_analyzer(code)
        self.tokens_table.update(tokens)
        
        self.log(f"Running {file_name}")
        syntax_semantic_analyzer(code, self, file_name)
    
    def log(self, text=""):
        self.text_area.config(state="normal")
        self.text_area.insert(tk.END, f"{text}\n")
        self.text_area.mark_set("insert", "end")
        self.text_area.see("insert")
        self.text_area.config(state="disabled")
        self.text_area.update()
        
    def clear(self):
        self.text_area.config(state="normal")
        self.text_area.delete("1.0", tk.END)
        self.text_area.config(state="disabled")
        self.text_area.update()
    
    def update_table(self, symbol_table):
        symbol_table = {key:typecast_string(value) for (key, value) in symbol_table.items()}
        self.symbol_table.update(list(symbol_table.items()))
            
    def get_input(self, symbol_table):
        self.update_table(symbol_table)
        self.text_area.config(state="normal")
        self.text_area.bind("<Return>", self.on_enter)
        
        self.console_input = None
        self.console_input_ready = tk.BooleanVar(value=False) 
        self.text_area.update()
        
        self.root.wait_variable(self.console_input_ready)
        
        self.text_area.unbind("<Return>")
        self.text_area.config(state="disabled")
        self.text_area.update()
        return self.console_input
            
    def on_enter(self, event):
        self.console_input = self.text_area.get("end-1l", "end").strip()
        self.console_input_ready.set(True) 
        
