import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from widgets.widget import Widget
from widgets.custom_button import create_styled_button

class Text_Editor(Widget):
    def __init__(self, root):
        super().__init__(root)
        self.border.place(relx=0.0, rely=0.0, anchor="nw", relwidth=0.5, relheight=0.5)
        
        # Header UI
        header = tk.Frame(self.content, bg="black")
        header.pack(fill="x", side="top")
        # file name code
        
        # File Buttons
        save_as_button = create_styled_button(header, "Save As", self.save_as)
        save_as_button.pack(side=tk.RIGHT)
        save_button = create_styled_button(header, "Save", self.save)
        save_button.pack(side=tk.RIGHT)
        new_button = create_styled_button(header, "New File", self.new_file)
        new_button.pack(side=tk.RIGHT)
        browse_button = create_styled_button(header, "Browse File", self.browse_file)
        browse_button.pack(side=tk.RIGHT)
        
        # Line Divider
        divider = tk.Frame(self.content, bg="white", height=2)
        divider.pack(fill="x", side="top")
        
        # Code
        self.text_area = scrolledtext.ScrolledText(
            self.content, 
            fg="white", 
            font=("Consolas", 12), 
            bg="black",
            insertbackground="white",
            wrap="none",
            undo=True)
        self.text_area.pack(fill="both", side="top", expand=True)

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a LOLCode File",
            filetypes=(("LOLCode Files", "*.lol"), ("All Files", "*.*"))  # Filter file types
        )
        if file_path:
            self.current_file_path = file_path
            self.set_text_area()
            
    def new_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".lol", filetypes=[("LOLCode Files", "*.lol")])
        if file_path:
            self.current_file_path = file_path
            with open(self.current_file_path, 'w') as file:
                file.write("HAI\nBTW glhf\nKTHXBYE")
            self.set_text_area()

    def save(self):
        if self.current_file_path:
            code = self.text_area.get(1.0, tk.END)
            with open(self.current_file_path, 'w') as file:
                file.write(code)
        else:
            save_as()
            
    def save_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".lol", filetypes=[("LOLCode Files", "*.lol")])
        if file_path:
            code = self.text_area.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(code)
    
    def set_text_area(self):
        if self.current_file_path:
            with open(self.current_file_path, 'r') as file:
                code = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, code)
            

