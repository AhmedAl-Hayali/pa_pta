# Task: Deep Dictionary Navigation
# Instructions: Extract 'year'. If any key is missing, return "Unknown".

def get_vehicle_year(data):
    try:
        return data["specs"]["model_info"]["year"]
    except KeyError:
        return "Unknown"

# Test Case
vehicle = {'specs': {'model_info': {'year': 2024}}} # 2024
vehicle = {'specs': {'model_info': {'yaer': 2024}}} # "Unknown"
vehicle = {} # "Unknown"
# Expected: 2024
print(get_vehicle_year(vehicle))