import turtle

screen = turtle.Screen()
t = turtle.Turtle()

def move():
    t.forward(50)

screen.listen()
screen.onkey(move, "space")
screen.mainloop()
