import turtle
scr = turtle.Screen()
clicks = []
def save(x, y):
    clicks.append((x, y))
    print("Saved:", len(clicks), "clicks")
    turtle.goto(x, y)
    turtle.dot(10)
scr.onclick(save)
turtle.done()