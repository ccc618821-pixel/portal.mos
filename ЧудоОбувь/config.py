import os
from datetime import date
from pathlib import Path
APP_NAME = "Чудо Обувь"
BASE_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = BASE_DIR / "resources"
PRODUCT_IMAGES_DIR = RESOURCES_DIR / "images"
LOGO_PATH = RESOURCES_DIR / "logo.png"
ICON_PATH = RESOURCES_DIR / "icon.ico"
PLACEHOLDER_IMAGE_PATH = RESOURCES_DIR / "picture.png"
db_host = "localhost"
db_name = "boots"
db_user = "postgres"
db_pass = "Timon2008.!"
db_port = 5432
FONT_FAMILY = "Calibri"
BASE_FONT_SIZE = 11
COLOR_BACKGROUND = "#FFFFFF"
COLOR_SECONDARY = "#D2F6E7"
COLOR_ACCENT = "#70B2AF"
COLOR_LOW_STOCK = "#FFB3B3"
COLOR_TEXT = "#000000"
COLOR_BORDER = "#9E9E9E"
COLOR_DISABLED = "#E3E3E3"
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 720
WINDOW_MIN_WIDTH = 900
WINDOW_MIN_HEIGHT = 560
DISCOUNT_PERCENT = 25
LOW_STOCK_LIMIT = 3
def get_calculation_date():
    """Дата расчёта скидки. По умолчанию — сегодня.

    Для проверки скидки на другую дату задайте переменную окружения
    CHUDO_CALCULATION_DATE в формате ГГГГ-ММ-ДД.
    """
    custom_date = os.getenv("CHUDO_CALCULATION_DATE")
    if custom_date:
        try:
            return date.fromisoformat(custom_date)
        except ValueError:
            return date.today()
    return date.today()