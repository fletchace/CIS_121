def total_sales(sales):
    total = 0
    for items in sales.values():
        total += items
    print(total)

total_sales({"Laptop": 5, "Phone": 10, "Tablet": 3}) # → 18
total_sales({"Shoes": 20, "Hats": 15, "Jackets": 10}) # → 45