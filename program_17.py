# Program 17: Reaction timer!
import turtle
import time
import random
scr = turtle.Screen()
scr.bgcolor("red")
start = 0
def go():
    global start
    scr.bgcolor("green")
    start = time.time()
def click(x, y):
    if start > 0:
        reaction = round(time.time() - start, 3)
        print("Reaction:", reaction, "seconds!")
        scr.bgcolor("red")
scr.ontimer(go, random.randint(2000, 5000))
scr.onclick(click)
turtle.done()