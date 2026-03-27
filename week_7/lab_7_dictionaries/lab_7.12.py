def total_donations(donations):
    amount = 0
    for donation in donations.values():
        amount += donation
    print(amount)

total_donations({"John": 100, "Sarah": 200, "Mike": 50}) # → 350
total_donations({"Anna": 500, "Tom": 1000, "Jerry": 1500}) # → 3000
total_donations({"Chris": 25, "Alex": 30, "Morgan": 45}) # → 100