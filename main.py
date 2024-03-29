# This entrypoint file to be used in development. Start by reading README.md
import budget

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55, "t-shirt")
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
house = budget.Category("Housing")
house.deposit(2000, "Rent")

print(food)
print(clothing)
print(house)
