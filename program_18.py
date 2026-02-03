# Program 18: Click to place, drag to draw
import turtle
scr = turtle.Screen()
def place(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
def draw(x, y):
    turtle.goto(x, y)
scr.onclick(place)
turtle.ondrag(draw)
turtle.done()