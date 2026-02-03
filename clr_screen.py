import turtle

turtle.speed(0)
scr = turtle.Screen()

def clr_scr():
    turtle.clear()

def go_to_click(x,y):
    
    turtle.goto(x,y)
    
    
turtle.ondrag(go_to_click)
turtle.listen()
turtle.onkey(clr_scr, "c")

turtle.done()