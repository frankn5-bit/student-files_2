import turtle
turtle.pensize(10)
turtle.pencolor("purple")
def draw(x, y):
    turtle.goto(x, y)
turtle.ondrag(draw)
turtle.done()