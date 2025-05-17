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
# window = turtle.screen()
# window.setup(width = 400 height = 400)
# def draw_square (size):
#     turtle.seth()
#     for i in range(4):

#     turtle.pendown()
