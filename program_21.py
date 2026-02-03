# Program 21: Click to catch the turtle!
import turtle
import random
scr = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.penup()
score = 0
def catch(x, y):
    global score
    if abs(x - t.xcor()) < 20 and abs(y - t.ycor()) < 20:
        score = score + 1
        print("GOT IT! Score:", score)
    t.goto(random.randint(-200, 200), random.randint(-150, 150))
t.goto(random.randint(-200, 200), random.randint(-150, 150))
scr.onclick(catch)
turtle.done()