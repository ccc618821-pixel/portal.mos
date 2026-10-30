import tkinter as tk
from tkinter import font as tk_font
from tkinter import ttk
from config import (
    BASE_FONT_SIZE,
    COLOR_ACCENT,
    COLOR_BACKGROUND,
    COLOR_SECONDARY,
    COLOR_TEXT,
    FONT_FAMILY,
    ICON_PATH,
    LOGO_PATH,
    WINDOW_HEIGHT,
    WINDOW_MIN_HEIGHT,
    WINDOW_MIN_WIDTH,
    WINDOW_WIDTH,
)
from ui.image_loader import load_image_from_file
NAMED_FONTS = ("TkDefaultFont", "TkTextFont", "TkMenuFont", "TkHeadingFont", "TkCaptionFont", "TkTooltipFont")
def create_font(size=BASE_FONT_SIZE, is_bold=False):
    if is_bold:
        return (FONT_FAMILY, size, "bold")
    return (FONT_FAMILY, size)
def apply_application_style(root):
    root.configure(background=COLOR_BACKGROUND)
    for named_font in NAMED_FONTS:
        try:
            tk_font.nametofont(named_font).configure(family=FONT_FAMILY, size=BASE_FONT_SIZE)
        except tk.TclError:
            continue
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure(".", font=create_font(), background=COLOR_BACKGROUND, foreground=COLOR_TEXT)
    style.configure("TCombobox", fieldbackground=COLOR_BACKGROUND, background=COLOR_SECONDARY)
    style.configure("Treeview", font=create_font(), rowheight=30, background=COLOR_BACKGROUND,
                    fieldbackground=COLOR_BACKGROUND)
    style.configure("Treeview.Heading", font=create_font(is_bold=True), background=COLOR_SECONDARY,
                    relief="flat")
    style.map("Treeview", background=[("selected", COLOR_ACCENT)], foreground=[("selected", COLOR_TEXT)])
    root.option_add("*TCombobox*Listbox.font", f"{FONT_FAMILY} {BASE_FONT_SIZE}")
    root.option_add("*TCombobox*Listbox.selectBackground", COLOR_ACCENT)
    root.option_add("*TCombobox*Listbox.selectForeground", COLOR_TEXT)
def set_window_icon(root):
    try:
        root.iconbitmap(str(ICON_PATH))
    except tk.TclError:
        logo_image = load_image_from_file(LOGO_PATH, 64)
        if logo_image is not None:
            root.iconphoto(True, logo_image)
def configure_main_window(root):
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    root.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
    set_window_icon(root)
