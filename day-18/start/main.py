from turtle import *

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
def go_forward(steps = 100):
    global timmy
    timmy.forward(steps)


def turn_right():
    global timmy
    timmy.right(90)

for i, _ in enumerate(range(20)):
    if i % 2 == 0:
        timmy.pd()
    go_forward(10)
    timmy.pu()

screen.exitonclick()

