import colorgram
import turtle as t
import random

spacing = 40
screen = t.Screen()
tim = t.Turtle()
tim.hideturtle()
tim.pu()
tim.setheading(180)
tim.forward(200)
tim.setheading(0)
t.colormode(255)

rgb_colors = []
colors = colorgram.extract('art.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    
    if r + g + b < 600:
        rgb_colors.append((r,g,b))
    
    

for i, _ in enumerate(range(1, 101)):
    if i % 10 == 0:
        tim.setheading(270)
        tim.forward(spacing)
        tim.setheading(180)
        tim.forward(spacing * 9)
        tim.setheading(0)
    else:
        tim.forward(spacing)
    tim.dot(20, random.choice(rgb_colors))

screen.exitonclick()