#  print("Hello from lesson 13")



# while True:
#     print("Choose between one of the four options using the option number...")
#     print("1.Withdraw")
#     print("2.Deposit")
#     print("Check balance")
#     print("4.Exit")
#     userChoice = int(input("What do you choose?"))
#     if userChoice == 1:
#         amount = int(input("How much money do you want to withdraw?"))
#         if amount <= balance: # should check if it is also equal to the balance 
#             balance -= amount
#             print(balance)
#         else:
#             print("Error://!?U are too broke.😁✌️🤞")
#     if userChoice == 2:
#         amount = int(input("How much do you want to deposit?"))
#         balance += amount
#     if userChoice == 3:
#         print(balance)
#     if userChoice == 4:
#         break# balance = 1000
# ₊˚ ✧ __________________________________________⊱⋆⊰_________________________________________________________ ✧ ₊˚#

# groceries = [
#     "Apples",
#     "Bread",
#     "Carrots",
#     "Dates",
#     "Eggs",
#     "Flour",
#     "Grapes",
#     "Honey"
# ]
# groceries[7] = "Herbs"

# groceries.append("Ice")
# groceries.insert(1,"Bananas")

# del(groceries[2])#method 1
# #Method # 2: item_that_was_removed = groceries.pop(3)
# print(groceries)
#════════════════════════════════════════════════════════════════════════════════════

pizza_toppings = [
    'Mushrooms',
    'Pepperoni',
    'Cheese',
    'Extra Cheese'
]
for n in range(len(pizza_toppings)):
    print('The available toppings are: ')
    print(str(n+1) + '.' + pizza_toppings[n])

while True:
    user_input = int(input('Please choose your pizza topping by number :'))
    if user_input == 'end':
        break