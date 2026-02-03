# Program 20: Random teleport on click
import turtle
import random
scr = turtle.Screen()
def jump(x, y):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(20, "red")
    print("Jumped to:", x, y)
scr.onclick(jump)
turtle.done()