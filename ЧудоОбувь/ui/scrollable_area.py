import tkinter as tk
from tkinter import ttk
from config import COLOR_BACKGROUND
def calculate_scroll_units(event):
    if event.num == 4:
        return -1
    if event.num == 5:
        return 1
    if event.delta == 0:
        return 0
    if abs(event.delta) >= 120:
        return int(-event.delta / 120)
    return -1 if event.delta > 0 else 1
def create_scrollable_area(parent):
    outer_frame = tk.Frame(parent, bg=COLOR_BACKGROUND)
    canvas = tk.Canvas(outer_frame, bg=COLOR_BACKGROUND, highlightthickness=0)
    scrollbar = ttk.Scrollbar(outer_frame, orient="vertical", command=canvas.yview)
    inner_frame = tk.Frame(canvas, bg=COLOR_BACKGROUND)
    inner_window_id = canvas.create_window((0, 0), window=inner_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    def stretch_inner_frame(event):
        canvas.itemconfigure(inner_window_id, width=event.width)
    def scroll_with_mouse_wheel(event):
        if not canvas.winfo_exists():
            return
        canvas.yview_scroll(calculate_scroll_units(event), "units")
    def release_mouse_wheel(event):
        canvas.unbind_all("<MouseWheel>")
        canvas.unbind_all("<Button-4>")
        canvas.unbind_all("<Button-5>")
    inner_frame.bind("<Configure>", update_scroll_region)
    canvas.bind("<Configure>", stretch_inner_frame)
    canvas.bind_all("<MouseWheel>", scroll_with_mouse_wheel)
    canvas.bind_all("<Button-4>", scroll_with_mouse_wheel)
    canvas.bind_all("<Button-5>", scroll_with_mouse_wheel)
    outer_frame.bind("<Destroy>", release_mouse_wheel)
    return outer_frame, inner_frame
