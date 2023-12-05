import turtle
from turtle import Screen
from name_state import Name_state

score = 0

screen = Screen()
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)



name_state = Name_state()

game_is_on = True

while game_is_on:
    state = screen.textinput(title=f"Score {score}/50", prompt="Write state!").title()

    if state == "Exit":
        name_state.create_new_csv()
        break

    if name_state.display_state(state) is True:
        score+=1

    if score == 50:
        name_state.create_new_csv()
        break


screen.exitonclick()





