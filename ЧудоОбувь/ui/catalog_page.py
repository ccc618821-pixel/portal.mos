import tkinter as tk
from config import COLOR_BACKGROUND, COLOR_TEXT, get_calculation_date
from database.connection import open_connection
from database.repository import fetch_catalog_items
from ui.messages import show_error
from ui.page_header import build_page_header
from ui.product_card import create_product_card
from ui.scrollable_area import create_scrollable_area
from ui.styles import create_font
def load_catalog_items():
    try:
        with open_connection() as connection:
            return fetch_catalog_items(connection, get_calculation_date())
    except Exception as error:
        show_error(
            "Каталог недоступен",
            "Не удалось загрузить каталог из базы данных.\n\n"
            "Проверьте, что PostgreSQL запущен, база создана скриптом sql/boots.sql, "
            "а параметры подключения в файле config.py указаны верно.\n\n"
            f"Техническая информация: {error}",
        )
        return None
def build_catalog_page(container):
    page = tk.Frame(container, bg=COLOR_BACKGROUND)
    page.pack(fill="both", expand=True)
    build_page_header(page, "Каталог товаров")
    scrollable_frame, cards_frame = create_scrollable_area(page)
    scrollable_frame.pack(fill="both", expand=True, padx=12, pady=12)
    catalog_items = load_catalog_items()
    if catalog_items is None:
        error_text = ("Каталог не загружен. Устраните ошибку подключения "
                      "и перезапустите приложение.")
        tk.Label(
            cards_frame,
            text=error_text,
            font=create_font(13),
            bg=COLOR_BACKGROUND,
            fg=COLOR_TEXT,
        ).pack(pady=40)
        return page
    if not catalog_items:
        tk.Label(
            cards_frame,
            text="В каталоге пока нет товаров.",
            font=create_font(13),
            bg=COLOR_BACKGROUND,
            fg=COLOR_TEXT,
        ).pack(pady=40)
        return page
    for catalog_item in catalog_items:
        create_product_card(cards_frame, catalog_item).pack(fill="x", pady=(0, 10))
    return page