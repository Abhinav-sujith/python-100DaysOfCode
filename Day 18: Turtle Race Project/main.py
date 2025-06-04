import random
from turtle import Turtle,Screen

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_choice = screen.textinput(title = "Make you bet:", prompt="Which turtle will win the race? Enter a color: ")
print(user_choice)
color = ["red","orange","yellow","blue","purple","pink"]
y_positions = [-70,-40,-10,20,50,80]
all_turtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"you have won! The {winning_color} turtle is the winner")
            else:
                print(f"You lose. The winning color is {winning_color}")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()


"""
-- Version new 

def move_forward():
    emmy.forward(10)
def backwards():
    emmy.back(10)
def move_right():
    new_heading = emmy.heading() - 10
    emmy.setheading(new_heading)
def move_left():
    new_heading = emmy.heading() + 10
    emmy.setheading(new_heading)
def clear_drawing():
    emmy.clear()
    emmy.penup()
    emmy.home()
    emmy.pendown()

screen.listen()
screen.onkey(key="w",fun= move_forward)
screen.onkey(key="s",fun= backwards)
screen.onkey(key="d",fun= move_right)
screen.onkey(key="a",fun= move_left)
screen.onkey(key="c",fun= clear_drawing)

-- My version

def move_forward():
    emmy.forward(10)
def backwards():
    emmy.back(10)
def move_right():
    emmy.right(10)
def move_left():
    emmy.left(10)
def clear_drawing():
    emmy.reset()

screen.onkey(key="w",fun= move_forward)
screen.onkey(key="s",fun= backwards)
screen.onkey(key="d",fun= move_right)
screen.onkey(key="a",fun= move_left)
screen.onkey(key="c",fun= clear_drawing)
"""