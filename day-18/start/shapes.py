import turtle as t
import random

tim = t.Turtle()
tim.speed(0)
t.colormode(255)
tim.shape("turtle")
tim.width(10)
screen = t.Screen()
shapes = [3,4,5,6,7,8,9,10,3]
colors = ["Black", "DodgerBlue","Gold", "FireBrick4", "FireBrick", "LightCoral","Gold", "Purple4"]
turns = [90, 180, 270, 360, -90, -180, -270]


for _ in range(100):
    tim.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    tim.forward(50)
    tim.right(random.choice(turns))
        
screen.exitonclick()
