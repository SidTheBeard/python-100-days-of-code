import math
import turtle as t
import sys

snake = t.Turtle()
snake.pu()
snake.shape("square")
snake.color("Green")
snake.shapesize(1,3)
apples = []
playing = True
level = 1

def turn_down():
    global level
    snake.setheading(270)
    level += 1
    print(level)
    # snake.forward(10)

def turn_up():
    global level
    snake.setheading(90)
    level += 1
    print(level)
    # snake.forward(10)

def turn_left():
    global level
    snake.setheading(180)
    level += 1
    print(level)
    # snake.forward(10)

def turn_right():
    global level
    snake.setheading(0)
    level += 1
    print(level)
    # snake.forward(10)

def off():
    playing = False
    sys.exit()

screen = t.Screen()
screen.setup(width=500, height=400)

screen.listen()

while playing:
    speed = math.ceil(level * 0.2)
    snake.speed(0 if speed > 10 else speed)
    snake.forward(5)
    screen.onkey(key="Up", fun=turn_up)
    screen.onkey(key="Right", fun=turn_right)
    screen.onkey(key="Down", fun=turn_down)
    screen.onkey(key="Left", fun=turn_left)
    screen.onkey(key="Q", fun=off)
    

screen.exitonclick()
