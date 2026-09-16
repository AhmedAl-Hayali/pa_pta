# Task: String Formatting
# Goal: Transform a raw SKU into a readable title.

def format_sku(sku_string):
    """
    Instructions: Convert 'engine-oil-10w30' to 'Engine Oil 10w30'.
    """
    string_els = sku_string.split("-")
    for string_el in string_els:
        if string_el[0].isalpha():

# Test: format_sku("brake-pads-ceramic") -> "Brake Pads Ceramic"
print(format_sku("brake-pads-ceramic"))