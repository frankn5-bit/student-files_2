import turtle
scr = turtle.Screen()
def red():
    turtle.color("red")
def blue():
    turtle.color("blue")
def green():
    turtle.color("green")
scr.onkey(red, "r")
scr.onkey(blue, "b")
scr.onkey(green, "g")
scr.listen()
turtle.done()