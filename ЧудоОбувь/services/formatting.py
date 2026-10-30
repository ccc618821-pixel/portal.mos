from decimal import Decimal
def format_price(amount):
    rounded_amount = Decimal(amount).quantize(Decimal("0.01"))
    whole_part, fraction_part = f"{rounded_amount:.2f}".split(".")
    grouped_whole_part = f"{int(whole_part):,}".replace(",", " ")
    if fraction_part == "00":
        return f"{grouped_whole_part} руб."
    return f"{grouped_whole_part},{fraction_part} руб."
def format_size(size_value):
    decimal_value = Decimal(str(size_value))
    if decimal_value == decimal_value.to_integral_value():
        return str(int(decimal_value))
    return f"{decimal_value.normalize():f}".replace(".", ",")
