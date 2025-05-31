import turtle as t
import random
from hist_paint import color_list

emmy = t.Turtle()

for _ in range(0,100,10):
    emmy.shape("circle")
    emmy.dot(20,random.choice(color_list))
    stamp_id = emmy.stamp()
    emmy.forward(_)









"""
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color
    
-- my version spirograph

for _ in range(1):
    for i in range(0,360,5):
        emmy.speed("fastest")
        emmy.pensize()
        emmy.color(random_color())
        emmy.setheading(i)
        emmy.circle(100)
        
-- Random walk(my version)

direction = [0,90,180,270]
length = [20,30,25,35,40,45,50]

for _ in range(100):
    emmy.pensize(10)
    emmy.speed(8)
    emmy.setheading(random.choice(direction))
    emmy.forward(random.choice(length))
    emmy.color(random_color())

colors = ["Gold", "DeepSkyBlue", "HotPink", "Lime", "Turquoise", "Orchid", "Tomato", "Coral", "Violet", "Salmon"]    
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        emmy.forward(100)
        emmy.right(angle)

for shape_side in range(3,11):
    emmy.color(random.choice(colors))
    draw_shape(shape_side)


First Trial Version

def shape(length,distances,angle,colours):
    for i in range(length):
        emmy.pencolor(colours)
        emmy.forward(distances)
        emmy.right(angle)

shape(3,100,120,"Yellow")
shape(4,100,90,"Black")
shape(5,100,72,"Green")
shape(6,100,60,"Blue")
shape(7,100,51.43,"Purple")
shape(8,100,45,"Orange")
shape(9,100,40,"Red")
shape(10,100,36,"violet")
"""





screen = t.Screen()
screen.exitonclick()