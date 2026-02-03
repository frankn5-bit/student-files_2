import turtle
scr = turtle.Screen()
def dot(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(20, "blue")
scr.onclick(dot)
turtle.done()