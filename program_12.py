import turtle
scr = turtle.Screen()
turtle.shape("turtle")
def stamp():
    turtle.stamp()
    turtle.forward(30)
scr.onkey(stamp, "space")
scr.listen()
turtle.done()