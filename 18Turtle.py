from turtle import Turtle, Screen
from random import randint, choice
import colorgram

my_turtle = Turtle()
my_turtle.shape("circle")
screen = Screen()
screen.colormode(255)
my_turtle.speed(15)
my_turtle.penup()
my_turtle.ht()


rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    if (r + g + b) < 720:
        add_color = (r, g, b) 
        rgb_colors.append(add_color)


length = (20 * 10) + (50 * 9)
x_start = length - (length * 1.5)
y_start = length - (length * 1.5)

my_turtle.goto((x_start, y_start))

for x in range(0, 10):
    for y in range(0, 10):
        my_turtle.dot(20, choice(rgb_colors))
        my_turtle.fd(50)
    my_turtle.sety(my_turtle.ycor() + 50)
    my_turtle.setx(x_start)


screen.exitonclick()