"""DAY 36 OF 100 DAYS 
PYTHON PROJECT"""

import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(3)  

tree = turtle.Turtle()
tree.speed(0)
tree.color("#fbfbfb")
tree.left(90)
tree.penup()
tree.goto(0, -250)
tree.pendown()

def draw_tree(branch):
    if branch < 5:
        return
    tree.forward(branch)

    tree.right(25)
    draw_tree(branch * 0.75)

    tree.left(50)
    draw_tree(branch * 0.75)

    tree.right(25)
    tree.backward(branch)

draw_tree(100)

screen.update() 
turtle.done()