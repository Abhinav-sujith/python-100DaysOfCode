import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S states Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guess_states = []

while len(guess_states) < 50:
    data = pd.read_csv("50_states.csv")
    all_states = data.state.to_list()
    answer_state = screen.textinput(title=f"{len(guess_states)} Guessed is correct",
                                    prompt="What's the province names").title()
    if answer_state == "Exit":
        missing_states = []
        for states in all_states:
            if states not in guess_states:
                missing_states.append(states)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    #If answer_state is one of the states in all the states of the 50_states.csv
    if answer_state in all_states: # will only work, if you converted the csv to list
        guess_states.append(answer_state)
        t = turtle.Turtle()#if they got it right
        t.hideturtle()
        t.penup()
        state_row = data[data.state == answer_state]
        t.goto(state_row.x.item(), state_row.y.item())
        t.write(answer_state)

#states to learn.csv

"""
This code will get you the coordinates in the map 

def get_mouse_click_coor(x,y): - We defined the function here
    print(x,y) - This is to print the coordinates 


turtle.onscreenclick(get_mouse_click_coor) - This will give the coordinates
turtle.mainloop() - This will keep the image open and won't exit on click
"""
screen.exitonclick()
