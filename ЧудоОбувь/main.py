import tkinter as tk
from config import APP_NAME
from ui.catalog_page import build_catalog_page
from ui.styles import apply_application_style, configure_main_window
def main():
    root = tk.Tk()
    root.title(f"{APP_NAME} — Каталог товаров")
    configure_main_window(root)
    apply_application_style(root)
    build_catalog_page(root)
    root.mainloop()
if __name__ == "__main__":
    main()  