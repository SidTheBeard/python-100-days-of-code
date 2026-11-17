import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    color = (r,g,b)
    
    return color
    

tim.width(4)
tim.speed(0)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.setheading(tim.heading() + 10)
        tim.circle(100)
        
        

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()