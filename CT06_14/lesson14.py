import turtle 
window = turtle.Screen()
window.setup(width= 600, height= 400)
t = turtle.Turtle()
t.shape('turtle')
t.fillcolor('green')

t.seth(0)
for i in range(3):
    t.pendown()
    
window.mainloop()