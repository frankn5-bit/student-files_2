import turtle
def draw(x, y):
    turtle.goto(x, y)
turtle.ondrag(draw)
turtle.done()
