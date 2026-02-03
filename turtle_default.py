import turtle

def move():
    turtle.forward(50)

turtle.listen()
turtle.onkey(move, "space")
turtle.done()
