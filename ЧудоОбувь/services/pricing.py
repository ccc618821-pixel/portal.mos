from datetime import timedelta
from decimal import Decimal, ROUND_HALF_UP
from config import DISCOUNT_PERCENT
def get_previous_month_range(calculation_date):
    first_day_current_month = calculation_date.replace(day=1)
    last_day_previous_month = first_day_current_month - timedelta(days=1)
    first_day_previous_month = last_day_previous_month.replace(day=1)
    return first_day_previous_month, first_day_current_month
def calculate_discount_percent(was_ordered_last_month):
    if was_ordered_last_month:
        return 0
    return DISCOUNT_PERCENT
def calculate_final_price(base_price, discount_percent):
    price_multiplier = Decimal(100 - discount_percent) / Decimal(100)
    return (Decimal(base_price) * price_multiplier).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
