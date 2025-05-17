# # Task 3: Increment Counter
# Create a function that will increase the 'counter' variable by 1 each
# time it is called.

# 1. Create a 'counter' variable and assign it '0'
# 2. Define a function 'increment_counter()':
#         a. Declare 'counter' as 'global'
#         b. Add 1 to 'counter'
# 3. Test your program out by calling the 'increment_counter()' function
# 4. 3 times before printing out the value of the 'counter' variable.

# Your output should be "3"

# counter = 0

# def increment_counter ():
#     global counter
#     counter += 1

# increment_counter()
# increment_counter()
# increment_counter()

# print (counter)

# ---------------------------------------------------------------------

# # Task 4: Square to Square
# Use a function with parameters to draw 7 squares to form the pattern
# shown on the screen.

# 1. Import the 'turtle' library
# 2. Create a 400x400 screen
# 3. Create a function "draw_square" with a "size" parameter
# 4. The "draw_square" function will draw a square of size*size around
#    the (0,0) coordinate.
# 5. Within a 'for' loop, use the draw_square function you have created
#    to draw 7 squares around the (0,0) coordinate with the following
#    sizes:
#         50, 100, 150, 200, 250, 300, 350

# import turtle
# window = turtle.Screen()
# window.setup(width = 400, height = 400)
# def draw_square (size):
#     for i in range(4):
#         turtle.pendown()
#         turtle.forward(size)
#         turtle.right(90)
# length = 10
# turtle.goto(x = 0, y = 0)
# draw_square(length)
# window.mainloop()

# ---------------------------------------------------------------------

# # Task 5: Double the Number
# Create a function that takes in a number and doubles it

# 1. Create a function named 'doubleNumber()'
# 2. The function should return the doubled number
# 3. Using the 'doubleNumber()' function, print the doubles of the
#    following numbers:
#     4
#     9
#     1530
#     284

# def doubleNumber(num):
#     for n in num:
#         num1 = n * 2
#         print('Double of ' + str('n') + ' is ' + str(num1))

# numbers = [4, 9, 1530, 284]

# doubleNumber(numbers)
# ---------------------------------------------------------------------

# # Task 6: Greetings III
# Create a function that takes in a name and returns a greeting

# 1. Create a function named 'greet()'
# 2. The function should return a greeting
#     Example: "Hello there !"
# 3. Ask the user for their name
# 4. Using the 'greet()' function, print the greeting

# ----------------------------------------------------------------------

# # Task 7: Even or Odd? III
# Create a function that takes in a number and returns whether it is
# even

# 1. Create a function named isEven()
# 2. If the number is even, the function should return True
# 3. If the number is odd, the function should return False
# 4. Using the 'isEven()' function, loop through a list of numbers and
#    print them out in this format:
#     "3 is an odd number"
#     "9 is an odd number"
#     "2 is an even number"

# def isEven (num):
#     return num % 2 == 0

# numbers = [3, 9, 7, 6, 4, 8]

# for n in numbers:
#     if isEven(n):
#         print(str(n) + " is an even number")
#     else:
#         print(str(n) + " is an odd number")

# ----------------------------------------------------------------------
   
# # Task 8: Age Group
# Create a function that will take in someone's age and return either
# 'Child' (Below 13), 'Teen' (14-20), 'Adult' (21-64), or
# 'Senior' (65 and above) based on the age provided.

# 1. Define the function 'ageGroup()' with one parameter: 'age'.
# 2. Use 'if-elif-else' statements to return the appropriate age group
#    based on the 'age' parameter

# ----------------------------------------------------------------------

# # Task 9: Calling a function within a function
# **Task 9a**:
# Create a function 'square()' that will take in a number and return
# the squared value of the number. Squared is when the number is
# multiplied by itself.

# For example, "5 squared" is 5x5, giving us 25.

# Example:
# square(3) >>> 9

def square(num):
    return num*num

num1 = 7
square(num1)

# **Task 9b**:
# Create a function 'sum_of_squares()' that will take in 2 numbers and
# return the sum of each of the number squared. You must use the
# 'square()' function within the 'sum_of_squares()' function.

# Example:
# sum_of_squares(3, 4) >>> 25
