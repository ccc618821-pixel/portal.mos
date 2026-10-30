import tkinter as tk
from config import (
    COLOR_BACKGROUND,
    COLOR_BORDER,
    COLOR_LOW_STOCK,
    COLOR_TEXT,
    FONT_FAMILY,
    LOW_STOCK_LIMIT,
)
from services.formatting import format_price
from ui.image_loader import load_product_image
from ui.styles import create_font
CARD_IMAGE_SIZE = 120
COMPOSITION_WRAP_LENGTH = 620
def bind_click_recursively(widget, click_handler):
    widget.bind("<Button-1>", click_handler)
    widget.configure(cursor="hand2")
    for child_widget in widget.winfo_children():
        bind_click_recursively(child_widget, click_handler)
def create_price_label(parent, catalog_item, background):
    price_frame = tk.Frame(parent, bg=background)
    if catalog_item["discount_percent"] > 0:
        old_price_text = format_price(catalog_item["base_price"])
        tk.Label(
            price_frame,
            text=old_price_text,
            font=(FONT_FAMILY, 11, "overstrike"),
            bg=background,
            fg=COLOR_TEXT,
        ).pack()
    final_price_text = format_price(catalog_item["final_price"])
    tk.Label(
        price_frame,
        text=final_price_text,
        font=create_font(18, True),
        bg=background,
        fg=COLOR_TEXT,
    ).pack()
    return price_frame
def create_product_card(parent, catalog_item, on_click=None):
    is_low_stock = catalog_item["total_quantity"] <= LOW_STOCK_LIMIT
    background = COLOR_LOW_STOCK if is_low_stock else COLOR_BACKGROUND
    card = tk.Frame(parent, bg=background, highlightbackground=COLOR_BORDER, highlightthickness=1)
    card.columnconfigure(1, weight=1)
    product_image = load_product_image(catalog_item["image_path"], CARD_IMAGE_SIZE)
    image_label = tk.Label(
        card,
        image=product_image,
        bg=background,
        width=CARD_IMAGE_SIZE + 10,
        height=CARD_IMAGE_SIZE + 10,
    )
    image_label.grid(row=0, column=0, padx=(10, 6), pady=8)
    details_frame = tk.Frame(card, bg=background)
    details_frame.grid(row=0, column=1, sticky="nsew", padx=8, pady=8)
    title_text = f"{catalog_item['manufacturer']} | {catalog_item['product_name']}"
    tk.Label(
        details_frame,
        text=title_text,
        font=create_font(14, True),
        bg=background,
        fg=COLOR_TEXT,
        anchor="w",
        justify="left",
        wraplength=COMPOSITION_WRAP_LENGTH,
    ).pack(anchor="w", pady=(0, 4))
    category_text = f"Категория: {catalog_item['category']}"
    tk.Label(
        details_frame,
        text=category_text,
        font=create_font(12),
        bg=background,
        fg=COLOR_TEXT,
        anchor="w",
    ).pack(anchor="w")
    quantity_text = f"Количество пар: {catalog_item['total_quantity']}"
    tk.Label(
        details_frame,
        text=quantity_text,
        font=create_font(12),
        bg=background,
        fg=COLOR_TEXT,
        anchor="w",
    ).pack(anchor="w")
    composition_text = f"Состав: {catalog_item['composition']}"
    tk.Label(
        details_frame,
        text=composition_text,
        font=create_font(10),
        bg=background,
        fg=COLOR_TEXT,
        anchor="w",
        justify="left",
        wraplength=COMPOSITION_WRAP_LENGTH,
    ).pack(anchor="w", pady=(2, 0))
    price_frame = create_price_label(card, catalog_item, background)
    price_frame.grid(row=0, column=2, padx=24)
    if on_click is not None:
        def handle_click(event):
            on_click(catalog_item)
        bind_click_recursively(card, handle_click)
    return card