import turtle
def draw_pentagon():
    for i in range(5):
        turtle.forward(100)
        turtle.right(72)
turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
draw_pentagon()
turtle.done()
