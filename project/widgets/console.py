import tkinter as tk
from tkinter import font
from tkinter import scrolledtext
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
        self.text_area.config(wrap="word")
    
    def run(self):
        tokens = lexical_analyzer(self.text_editor.text_area.get("1.0", "end"))
        self.tokens_table.update(tokens)
        # symbol table update
        self.text_area.config(state="normal")
        self.text_area.delete("1.0", tk.END)
        parse_result = syntax_analyzer(self.text_editor.text_area.get("1.0", "end"))
        self.text_area.insert(tk.END, parse_result)
        self.text_area.config(state="disabled")
    
    async def get_input(self):
        self.text_area.config(state="normal")
        self.text_area.bind("<Return>", on_enter)
        
        self.text_area.mark_set("insert", "end")
        await listen()
        
        self.text_area.unbind("<Return>")
        self.text_area.config(state="disabled")
        
        return self.console_input
        
    async def listen(self):
        while self.console_input == None:
            self.update()
            await asyncio.sleep(0.01)
            
    def on_enter(self):
        self.console_input = self.text_area.get("end-2l linestart", "end-1c").strip()
        
