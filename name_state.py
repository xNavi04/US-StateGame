from turtle import Turtle
import pandas

DATA = pandas.read_csv("50_states.csv")
NAME_STATES = DATA.state.to_list()

class Name_state:
    def display_state(self,state):
        global NAME_STATES
        if state in NAME_STATES:
            x = DATA.x[DATA.state == state].to_list()[0]
            y = DATA.y[DATA.state == state].to_list()[0]
            cordinates = (x, y)
            print(cordinates)
            state_sign = Turtle()
            state_sign.penup()
            state_sign.ht()
            state_sign.goto(cordinates)
            state_sign.write(state)
            NAME_STATES.remove(state)
            return True

    def create_new_csv(self):
        dict_new = {"missing_states" : NAME_STATES}
        data = pandas.DataFrame(dict_new)
        data.to_csv("missing_states.csv")



