import turtle
scr = turtle.Screen()
def go(x, y):
    turtle.goto(x, y)
scr.onclick(go)
turtle.done()