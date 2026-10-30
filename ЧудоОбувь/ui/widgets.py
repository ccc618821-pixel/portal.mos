import tkinter as tk
from config import COLOR_ACCENT, COLOR_DISABLED, COLOR_SECONDARY, COLOR_TEXT
from ui.styles import create_font
def create_button(parent, text, command, is_accent=False):
    background = COLOR_ACCENT if is_accent else COLOR_SECONDARY
    pressed_background = COLOR_SECONDARY if is_accent else COLOR_ACCENT
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=background,
        fg=COLOR_TEXT,
        activebackground=pressed_background,
        activeforeground=COLOR_TEXT,
        disabledforeground="#777777",
        font=create_font(is_bold=is_accent),
        relief="flat",
        bd=0,
        padx=14,
        pady=6,
        cursor="hand2",
    )
def set_button_enabled(button, is_enabled, is_accent=False):
    if is_enabled:
        button.configure(state="normal", bg=COLOR_ACCENT if is_accent else COLOR_SECONDARY, cursor="hand2")
    else:
        button.configure(state="disabled", bg=COLOR_DISABLED, cursor="arrow")
