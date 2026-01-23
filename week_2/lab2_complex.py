human_age = float(input("Enter your age: ")) * 360
dog_years = round(human_age / 360 , 0)
dog_months = round(((human_age / 360 - dog_years , 0) * 12) , 0)
dog_days = round((((human_age / 360 - dog_years , 0) * 12 - dog_months) * 360) , 1)
print(f"You are {dog_years} years, {dog_months} months, and {dog_days} days old in dog years")