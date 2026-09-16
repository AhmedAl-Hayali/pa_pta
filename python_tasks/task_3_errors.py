# Task: Error Handling & Resilience
# Goal: Calculate a discount safely.

def calculate_discount(price, discount_percent):
    """
    Instructions: Handle cases where discount_percent is 0 
    or if inputs are strings/None. Return 0 for invalid inputs.
    """
    try:
        result = price * (1 - discount_percent/100)
    except TypeError:
        if discount_percent is not None:
            discount_percent = float(discount_percent)
        else:
            discount_percent = 0
        result = price * (1 - discount_percent / 100)
    return result
    

# Test Case
print(calculate_discount(100, "10")) # Should return 0 or handle conversion
print(calculate_discount(100, 0))    # Should return 0
print(calculate_discount(100, None))    # Should return 0