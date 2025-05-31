import turtle as t
import random

t.colormode(255)
emmy = t.Turtle()
color_list = [(234, 225, 83), (195, 8, 69), (231, 54, 132), (194, 164, 15), (112, 178, 214), (199, 77, 15), (216, 162, 101), (34, 187, 112), (29, 104, 167), (14, 23, 64), (20, 29, 168), (212, 136, 175), (231, 224, 7), (197, 34, 130), (15, 181, 210), (231, 167, 197)]
emmy.speed("fastest")
emmy.hideturtle()

emmy.setheading(225)
emmy.penup()
emmy.forward(300)
emmy.setheading(0)
no_of_dots = 100

for dot_count in range(1,no_of_dots + 1 ):
    emmy.penup()
    emmy.dot(10,random.choice(color_list))
    emmy.forward(50)

    if dot_count % 10 == 0:
        emmy.setheading(90)
        emmy.forward(50)
        emmy.setheading(180)
        emmy.forward(500)
        emmy.setheading(0)

screen = t.Screen()
screen.exitonclick()

"""def positioning():
    emmy.setheading(90)
    emmy.forward(50)
    emmy.setheading(180)
    emmy.forward(500)
    emmy.setheading(360)"""

"""emmy.setheading(90)
emmy.forward(50)
emmy.setheading(180)
emmy.forward(500)
emmy.setheading(0)"""

"""
-- HOW I EXTRACTED COLOR FROM AN IMAGE AND SAVED IT INTO A TUPLE

import colorgram
rgb_color = []
colors = colorgram.extract("image.jpg",30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_color.append(new_color)
print(rgb_color)
"""
