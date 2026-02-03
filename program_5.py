import turtle
scr = turtle.Screen()
count = 0
def click(x, y):
    global count
    count = count + 1
    print("Clicks:", count)
    turtle.dot(15)
    turtle.goto(x, y)
scr.onclick(click)
turtle.done()