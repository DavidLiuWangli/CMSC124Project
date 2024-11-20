import tkinter as tk

def create_styled_label(parent, text):
    return tk.Label(
        parent,
        text=text,
        fg="white",
        font=("Consolas", 10),
        bg="black",
        padx=2,
        pady=2
    )

def create_styled_button(parent, text, function):
    button = create_styled_label(parent, text)
    button.bind("<Button-1>", lambda e: function())
    button.bind("<Enter>", lambda event: enter(event, button))
    button.bind("<Leave>", lambda event: leave(event, button))
    return button
    
def enter(event, button):
    button.config(fg="black", bg="white")

def leave(event, button):
    button.config(fg="white", bg="black")
    