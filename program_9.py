import turtle
scr = turtle.Screen()
def up():
    turtle.forward(20)
def left():
    turtle.left(30)
def right():
    turtle.right(30)
scr.onkey(up, "Up")
scr.onkey(left, "Left")
scr.onkey(right, "Right")
scr.listen()
turtle.done()