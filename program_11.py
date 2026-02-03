import turtle
scr = turtle.Screen()
presses = 0
def step():
    global presses
    presses = presses + 1
    print("Steps:", presses)
    turtle.forward(10)
scr.onkey(step, "space")
scr.listen()
turtle.done()