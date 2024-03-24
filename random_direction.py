import random
import turtle
from turtle import Screen

john = turtle.Turtle()
turtle.colormode(255)

num_sides = 5

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


directions = [0, 90, 180, 270]
john.pensize(10)
john.speed("fast")

for _ in range(400):
    john.color(random_colour())
    john.forward(30)
    john.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
