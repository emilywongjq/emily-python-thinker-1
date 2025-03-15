# print("Hello from lesson 7")
# print("レッスン 7 からこんにちは")
#____________________________𝕥𝕒𝕤𝕜_𝟙a______________________________________
# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = str(total / 3)

# student_name = "Alex"

# print ("Average score for " + student_name + " is: " + average_score)
#                             𝕥𝕒𝕤𝕜 𝟙b
#___________________( -_•)╦̵̵̿╤─🃜🃚🃖🃁🂭🂺( ദ്ദി ˙ᗜ˙ )_________________________


# for i in range(1,11):
#     print(i)


# for i in range(2, 21, 2):
#     print(i)


# for i in range(10, 0, -1):
#     print(i)
#                                           𝕥𝕒𝕤𝕜 𝟜
#___________________________________(ᵕ—ᴗ—)🃜🃚🃖🃁🂭🂺c( •̀⤙•́ c)____________________________________________________


# word = input("What word do you want to repeat?")
# n = int(input("How many times do you want to repeat?"))
# for i in range(n):
#     print(word)

#_____________________________𝕥𝕒𝕤𝕜_𝟝__________________________________
 

# name = input("What is your name?")
# n = int(input("How many times do you want to repeat?"))
# for i in range(n):
#     print("Nice to meet you "+ name)

#_____________________________𝕥𝕒𝕤𝕜_𝟞_____________________________________
 

sum = 0

# for i in range(1, 6):
#     sum = sum + int(input("What is the number #" + str(i)))

# print(sum)

#________________________________________________________________________
 
# number = int(input("What is the number for the timestable?"))

# for i in range(1, 13):
#     print(str(number) + " x " + str(i) + " = " + str(i*number))




###────୨ৎ────###────୨ৎ────###────୨ৎ────###────୨ৎ────###────୨ৎ────###

# num = int(input("How many layers do you want the pyramid to have: "))

# for i in range(1, num + 1):
#     print(str(i) * i)


# total = 0

# for i in range(1, 6):
#     total = total + int(input("What is the score of student "+ str(i)))

# average = total/ 5
# print ("The average score of all 5 students is " + str(average))


total = 0
numStudents = int(input("How many students do you have?"))
for i in range(1, numStudents+1):
    total = total + int(input("What is the score of student "+ str(i) + "? "))

average = total/ numStudents
print ("The average score is " + str(average))