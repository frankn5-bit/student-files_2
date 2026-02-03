import turtle

screen = turtle.Screen()
t = turtle.Turtle()

def left(x, y):
    print("Left:", x, y)
    t.color("blue")
    t.goto(x, y)

def right(x, y):
    print("Right:", x, y)
    t.color("red")
    t.goto(x, y)

screen.onscreenclick(left, 1)    # left button
screen.onscreenclick(right, 3)   # right button

screen.mainloop()
