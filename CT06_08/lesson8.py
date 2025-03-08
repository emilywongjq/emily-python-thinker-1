# name = input("What is your name?")# asking user for their name
# print("Nice to meet you "+ name)# print out the sentence


start_number = int(input("What number do you want to start with?"))# ask the user what number do they want to start with
stop_number = int(input("What number do you want to stop at?"))# ask the user what number do they want to stop at
increment_number = int(input("What is your increment?"))# ask the user what is their increment

for i in range(start_number,stop_number,increment_number):# do not -1 for the stop number as it will not work in the 2nd scenario)
    print(i)