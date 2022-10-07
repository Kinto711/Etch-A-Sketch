import turtle
from turtle import Turtle, Screen
import replit

t = Turtle()
screen = Screen()
def move_forward():
    t.forward(15)

def move_backward():
    t.backward(15)

def move_counter_clockwise():
    t.left(10)
def move_clockwise():
    t.right(10)

def clear():
    t.clear()
    t.penup()
    t.home()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
