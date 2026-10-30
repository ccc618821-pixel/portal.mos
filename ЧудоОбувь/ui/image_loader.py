import math
import tkinter as tk
from config import PLACEHOLDER_IMAGE_PATH, PRODUCT_IMAGES_DIR
image_cache = {}
def load_image_from_file(file_path, max_side):
    cache_key = (str(file_path), max_side)
    if cache_key in image_cache:
        return image_cache[cache_key]
    try:
        original_image = tk.PhotoImage(file=str(file_path))
    except (tk.TclError, OSError):
        return None
    reduction_factor = max(1, math.ceil(max(original_image.width(), original_image.height()) / max_side))
    if reduction_factor > 1:
        scaled_image = original_image.subsample(reduction_factor)
    else:
        scaled_image = original_image
    image_cache[cache_key] = scaled_image
    return scaled_image
def load_product_image(image_name, max_side):
    if image_name:
        product_image = load_image_from_file(PRODUCT_IMAGES_DIR / image_name, max_side)
        if product_image is not None:
            return product_image
    return load_image_from_file(PLACEHOLDER_IMAGE_PATH, max_side)
