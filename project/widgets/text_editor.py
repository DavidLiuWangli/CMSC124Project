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
        
        # Line Numbering
        self.line_numbers = tk.Text(
            self.content, 
            fg="white", 
            font=("Consolas", 12), 
            bg="black",
            insertbackground="white",
            wrap="none",
            state="disabled",
            )
        self.line_numbers.pack(fill=tk.Y, side=tk.LEFT)
        
        # Code
        self.text_area = scrolledtext.ScrolledText(
            self.content, 
            fg="white", 
            font=("Consolas", 12), 
            bg="black",
            insertbackground="white",
            wrap="none",
            undo=True
            )
        tab_size = font.Font(font=self.text_area["font"]).measure("    ")  # Measure 4 spaces
        self.text_area.config(tabs=(tab_size,))
        self.text_area.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        
        self.line_numbers.bind("<MouseWheel>", self.on_mouse_wheel)
        self.update_line_numbers()
        
        self.text_area.vbar.config(command=self.on_scroll)
        self.text_area.bind("<MouseWheel>", self.on_mouse_wheel)
        self.text_area.bind("<Key>", self.on_key_pressed)
        self.text_area.bind("<<Modified>>", self.on_text_area_change)

    def on_key_pressed(self, event=None):
        self.line_numbers.yview_moveto(self.text_area.yview()[0])
    
    def on_scroll(self, *args):
        self.text_area.yview(*args)
        self.line_numbers.yview(*args)

    def on_mouse_wheel(self, event):
        current_fraction = self.text_area.yview()[0]
        new_fraction = current_fraction + (-1 * (event.delta // 120)) / 100
        self.text_area.yview_moveto(new_fraction)
        self.line_numbers.yview_moveto(new_fraction)
    
    def on_text_area_change(self, event):
        if "*" not in self.get_file_name():
            self.set_asterisk_file_name()
        self.text_area.edit_modified(False)
        self.update_line_numbers()
    
    def update_line_numbers(self, event=None):
        self.line_numbers.config(state="normal")
        self.line_numbers.delete("1.0", "end")
        self.line_numbers.delete(1.0, tk.END)

        num_lines = int(self.text_area.index("end-1c").split(".")[0])
        line_number_string = "\n".join(str(i) for i in range(1, num_lines + 1)).splitlines()
        
        max_length = max(len(line) for line in line_number_string)
        for line in line_number_string:
            spaces = ' ' * (max_length - len(line))
            self.line_numbers.insert(tk.END, spaces + line + '\n')
        self.line_numbers.delete("end-1c", "end")
        
        self.line_numbers.config(width=max_length)
        self.line_numbers.yview_moveto(self.text_area.yview()[0])
        self.line_numbers.config(state="disabled")
    
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
    
    def set_text_area(self):
        if self.current_file_path:
            with open(self.current_file_path, 'r') as file:
                code = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, code)
            self.update_line_numbers()
            self.text_area.edit_modified(False)
