import random
import turtle
from turtle import Screen

john = turtle.Turtle()
turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


john.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        john.color(random_colour())
        john.circle(100)
        john.setheading(john.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
