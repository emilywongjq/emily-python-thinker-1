# print("Hello from lesson 13")
balance = 1000
while True:
    print("Choose between one of the four options using the option number...")
    print("1.Withdraw")
    print("2.Deposit")
    print("Check balance")
    print("4.Exit")
    userChoice = int(input("What do you choose?"))
    if userChoice == 1:
        amount = int(input("How much money do you want to withdraw?"))
        if amount <= balance: # should check if it is also equal to the balance 
            balance -= amount
            print(balance)
        else:
            print("")
    if userChoice == 2:
        amount = int(input("How much do you want to deposit?"))
        balance += amount
    if userChoice == 3:
        print(balance)
    if userChoice == 4:
        break