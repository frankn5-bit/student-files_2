# Program 19: Spiral with spacebar
import turtle
scr = turtle.Screen()
size = 5
def spiral():
    global size
    turtle.forward(size)
    turtle.right(15)
    size = size + 2
scr.onkey(spiral, "space")
scr.listen()
turtle.done()