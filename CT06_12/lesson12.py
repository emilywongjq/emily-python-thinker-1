# print("Hello from lesson 12")

# num = input("What is a random number that you can think of? :")

# if num % 3 == 0 and num % 5 == 0:
#     print("The number is divisible by 3 abd 5")
# else:
#     print("The number is not divisible by 3 abd 5")
# max_visitors = 30
# visitors = 0
# while True :
#     addVisitor = input("Add visitor?")
#     if addVisitor == "yes":
#         visitors += 1
#         print("Number of visitors : " + str(visitors))
#     if visitors == max_visitors:
#         break
# print("Sry we are not able to fit you. im sry")

# visitors = 18
# while visitors < 30 :
#     visitors += 1
#     print("Number of visitors : " + str(visitors))

# visitors = 4
# while visitors < 25 :
#     visitors += 1
#     print("Number of visitors : " + str(visitors))

# order = ""
# skip_comma = True

# while True :
#     userInput = input("What item do you want to order?")
#     if userInput == "end":
#         break
#     else:
#         if skip_comma:
#             order += userInput
#             skip_comma = False
#         else:
#             order += "," + userInput
# print(order)

num = 10
while num != 0 :
    print(num)
    num = num - 1
else:
    print("Happy new year!!!")


num = 10
while num != 0 :
    print(num)
    num = num - 1
    if num == 5:
        break
else:
    print("Happy new year!!!")
