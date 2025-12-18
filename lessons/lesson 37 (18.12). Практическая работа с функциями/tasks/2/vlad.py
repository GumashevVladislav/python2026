def delivery_cost(city, weight_kg, urgent):
    if urgent:
        return 500 + 30 * weight_kg
    return 300 + 20 * weight_kg

print(delivery_cost("Казань", 2, urgent=True))
