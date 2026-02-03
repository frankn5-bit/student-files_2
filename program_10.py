import turtle
scr = turtle.Screen()
def w():
    turtle.setheading(90)
    turtle.forward(20)
def a():
    turtle.setheading(180)
    turtle.forward(20)
def s():
    turtle.setheading(270)
    turtle.forward(20)
def d():
    turtle.setheading(0)
    turtle.forward(20)
scr.onkey(w, "w")
scr.onkey(a, "a")
scr.onkey(s, "s")
scr.onkey(d, "d")
scr.listen()
turtle.done()