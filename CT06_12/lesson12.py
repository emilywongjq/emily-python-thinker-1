# print("Hello from lesson 12")

# num = input("What is a random number that you can think of? :")

# if num % 3 == 0 and num % 5 == 0:
#     print("The number is divisible by 3 abd 5")
# else:
#     print("The number is not divisible by 3 abd 5")
max_visitors = 30
visitors = 0
while True :
    addVisitor = input("Add visitor?")
    if addVisitor == "yes":
        visitors += 1
        print("Number of visitors : " + str(visitors))
    if visitors == max_visitors:
        break
print("Sry we are not able to fit you as you are too fat im sry")

# visitors = 18
# while visitors < 30 :
#     visitors += 1
#     print("Number of visitors : " + str(visitors))

# visitors = 4
# while visitors < 25 :
#     visitors += 1
#     print("Number of visitors : " + str(visitors))