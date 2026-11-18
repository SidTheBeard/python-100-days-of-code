import turtle as t
import random

turtles = []
colors = ["Red", "Blue", "Gold", "Green", "Black", "Purple"]

fin = t.Turtle()
fin.pu()
fin.goto(x=200, y=400)
fin.pd()
fin.setheading(270)
fin.forward(600)


for i, _ in enumerate(range(6)):
    turtle = t.Turtle()
    turtle.pu()
    turtle.shape("turtle")
    turtle.color(colors[i])
    turtles.append(turtle)

for i, turtle in enumerate(turtles):
    turtle.goto(x=-200, y=i*50)

screen = t.Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if bet:
    racing = True

while racing:
    for turtle in turtles:
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

        if turtle.xcor() >= 200:
            turtle_color = turtle.pencolor().lower()
            print(f"{turtle_color.title()} wins!")
            if turtle_color == bet:
                print("Your bet hit!")
            else:
                print("You lost!")

            racing = False


screen.exitonclick()