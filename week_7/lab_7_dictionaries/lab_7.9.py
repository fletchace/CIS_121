receipt = {"side salad":6, "chicken parm":12, "cookie":3}
food_cost = 0
for food, price in receipt.items():
    if food == "side salad":
        food_cost += price
    elif food == "chicken parm":
        food_cost += price
    elif food == "cookie":
        food_cost += price

print(f"Bill Total: ${food_cost}")