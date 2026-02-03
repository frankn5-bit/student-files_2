import turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
n = 0
def draw(x, y):
    global n
    turtle.pencolor(colors[n % 6])
    turtle.goto(x, y)
    n = n + 1
turtle.ondrag(draw)
turtle.done()