import tkinter as tk
from config import APP_NAME, COLOR_SECONDARY, COLOR_TEXT, LOGO_PATH
from ui.image_loader import load_image_from_file
from ui.styles import create_font
from ui.widgets import create_button
HEADER_LOGO_SIZE = 56
def build_page_header(parent, page_title, user_full_name=None, action_buttons=None):
    parent.winfo_toplevel().title(f"{APP_NAME} — {page_title}")
    header_frame = tk.Frame(parent, bg=COLOR_SECONDARY)
    header_frame.pack(fill="x")
    logo_image = load_image_from_file(LOGO_PATH, HEADER_LOGO_SIZE)
    if logo_image is not None:
        tk.Label(header_frame, image=logo_image, bg=COLOR_SECONDARY).pack(side="left", padx=(12, 8), pady=6)
    tk.Label(header_frame, text=page_title, font=create_font(20, True), bg=COLOR_SECONDARY,
             fg=COLOR_TEXT).pack(side="left", padx=8)
    if user_full_name:
        tk.Label(header_frame, text=user_full_name, font=create_font(13, True), bg=COLOR_SECONDARY,
                 fg=COLOR_TEXT).pack(side="right", padx=16)
    for button_text, button_command, is_accent in reversed(action_buttons or []):
        create_button(header_frame, button_text, button_command, is_accent).pack(side="right", padx=4, pady=10)
    return header_frame
