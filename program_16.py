# Program 16: Timer - how long between clicks?
import turtle
import time
scr = turtle.Screen()
last = time.time()
def click(x, y):
    global last
    now = time.time()
    gap = round(now - last, 2)
    print("Time:", gap, "seconds")
    last = now
    turtle.goto(x, y)
scr.onclick(click)
turtle.done()