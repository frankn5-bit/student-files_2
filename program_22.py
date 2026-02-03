# Program 22: Mini Target Game with Score
import turtle
import random
import time
scr = turtle.Screen()
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
score = 0
start = time.time()
def play(x, y):
    global score
    if abs(x - target.xcor()) < 25 and abs(y - target.ycor()) < 25:
        score = score + 1
        elapsed = round(time.time() - start, 1)
        print(f"Score: {score} in {elapsed}s")
        target.goto(random.randint(-250, 250), random.randint(-180, 180))
target.goto(random.randint(-250, 250), random.randint(-180, 180))
scr.onclick(play)
turtle.done()