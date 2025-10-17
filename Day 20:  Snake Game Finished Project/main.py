from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 600,height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up") # first letter needs to be capital
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect Collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect Collision with tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            scoreboard.game_over()
    # if head collides with an segment in the tail
        #trigger game over sequence




"""

starting_positions = [(0,0),(-20,0),(-40,0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


    for seg_num in range(len(segments)-1,0,-1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)

segment  = Turtle("square")
segment.color('white')

segment_1 = Turtle("square")
segment_1.color("white")
segment_1.goto(-20,0)

segment_2 = Turtle("square")
segment_2.color('white')
segment_2.goto(-40,0)
"""

screen.exitonclick()
