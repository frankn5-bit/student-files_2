import turtle
scr = turtle.Screen()
def show(x, y):
    print("Click:", x, y)
    turtle.goto(x, y)
scr.onclick(show)
turtle.done()