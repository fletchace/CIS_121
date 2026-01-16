print("Hello World!")
#1
year=input("Enter year: ")
month=input("Enter month: ")
day=input("Enter day: ")
print("The date is "+month,day + ", " + year + ".")
#2
name=input("Enter your name: ")
age=input("Enter your age: ")
print("Howdy",name + ". " + age,"is a cool age.")
#3
firstName=input("Enter your first name: ")
lastName=input("Enter your last name: ")
print("Hello",firstName,lastName,". See ya next time.")
#4
firstName=input("Enter your first name: ")
lastName=input("Enter your last name: ")
print("Hello",firstName,lastName + ". How's it hangin?")
#5
colorPicked=input("Pick a color: ")
animal=input("Pick an animal: ")
print("You picked a",colorPicked,animal + ".")
#6
food=input("Enter a food: ")
drink=input("Enter a drink: ")
print(f"Your order is a {food} and a {drink}.")
#7
favoriteColor=input("Enter your favorite color: ")
favoriteFood=input("Enter your favorite food: ")
print(f"I also like {favoriteColor} and {favoriteFood}!")
#8
city=input("Enter a city: ")
state=input("Enter a state: ")
print(f"You are currently in {city}, {state}.")
#9
x='3'
y='7'
print(x,y)
temporary=''
temporary=x
x=y
y=temporary
print(x,y)