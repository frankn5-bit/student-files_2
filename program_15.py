import turtle
scr = turtle.Screen()
clicks = []
def save(x, y):
    clicks.append((x, y))
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(10, "blue")
    print("Points:", len(clicks))
def connect():
    turtle.penup()
    for point in clicks:
        turtle.goto(point)
        turtle.pendown()
    turtle.goto(clicks[0])  # close shape
scr.onclick(save)
scr.onkey(connect, "space")
scr.listen()
turtle.done()