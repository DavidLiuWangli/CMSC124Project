import tkinter as tk
from tkinter import font
from tkinter import filedialog
from tkinter import scrolledtext
from widgets.widget import Widget
from widgets.ui_elements import create_styled_label, create_styled_button
import os

class Text_Editor(Widget):
    def __init__(self, root):
        super().__init__(root)
        self.border.place(relx=0.0, rely=0.0, anchor="nw", relwidth=0.5, relheight=0.5)
        
        # File name label and current file path
        self.file_name = create_styled_label(self.header, "*Untitled")
        self.file_name.pack(side=tk.LEFT)
        self.current_file_path = None
        
        # File Buttons
        save_as_button = create_styled_button(self.header, "Save As", self.save_as)
        save_as_button.pack(side=tk.RIGHT)
        save_button = create_styled_button(self.header, "Save", self.save)
        save_button.pack(side=tk.RIGHT)
        new_button = create_styled_button(self.header, "New File", self.new_file)
        new_button.pack(side=tk.RIGHT)
        browse_button = create_styled_button(self.header, "Browse File", self.browse_file)
        browse_button.pack(side=tk.RIGHT)
        
        # Code
        self.text_area = scrolledtext.ScrolledText(
            self.content, 
            fg="white", 
            font=("Consolas", 12), 
            bg="black",
            insertbackground="white",
            wrap="none",
            undo=True)
        self.text_area.bind("<<Modified>>", self.on_text_area_change)
        tab_size = font.Font(font=self.text_area["font"]).measure("    ")  # Measure 4 spaces
        self.text_area.config(tabs=(tab_size,))
        self.text_area.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a LOLCode File",
            filetypes=(("LOLCode Files", "*.lol"), ("All Files", "*.*"))
        )
        if file_path:
            self.current_file_path = file_path
            self.set_file_name()
            self.set_text_area()
            
    def new_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".lol", filetypes=[("LOLCode Files", "*.lol")])
        if file_path:
            self.current_file_path = file_path
            self.set_file_name()
            with open(self.current_file_path, 'w') as file:
                file.write("HAI\nBTW glhf\nKTHXBYE")
            self.set_text_area()

    def save(self):
        if self.current_file_path and not self.text_area.edit_modified:
            return
        if self.current_file_path:
            code = self.text_area.get(1.0, tk.END)
            with open(self.current_file_path, 'w') as file:
                file.write(code)
            self.set_file_name()
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".lol", filetypes=[("LOLCode Files", "*.lol")])
            if file_path:
                self.current_file_path = file_path
                code = self.text_area.get(1.0, tk.END)
                with open(self.current_file_path, 'w') as file:
                    file.write(code)
            self.set_file_name()
        
    def save_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".lol", filetypes=[("LOLCode Files", "*.lol")])
        if file_path:
            code = self.text_area.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(code)
    
    def get_file_name(self):
        return self.file_name.cget("text")
    
    def set_file_name(self):
        self.file_name.config(text=os.path.basename(self.current_file_path))
    
    def set_asterisk_file_name(self):
        self.file_name.config(text="*" + os.path.basename(self.current_file_path))
    
    def on_text_area_change(self, event):
        if self.text_area.edit_modified(): 
            if "*" not in self.get_file_name():
                self.set_asterisk_file_name()
            self.text_area.edit_modified(False)
    
    def set_text_area(self):
        if self.current_file_path:
            with open(self.current_file_path, 'r') as file:
                code = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, code)
            self.text_area.edit_modified(False)
