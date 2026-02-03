import turtle

'''
leftclick = 1
middle (wheel) = 2
right click = 3'''

screen = turtle.Screen()
t = turtle.Turtle()

def right_click(x, y):
    print("Right click at:", x, y)
    t.goto(x, y)

screen.onscreenclick(right_click, btn=3)
screen.mainloop()
