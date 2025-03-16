import turtle
import pandas as pd

board_pen = turtle.Turtle()
board_pen.hideturtle()
board_pen.color("black")
board_pen.penup()

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(height = 490, width = 730)
screen.bgpic("blank_states_img.gif")

# Read the states csv, process it into a dictionary that you can use to get the state coordinates
states_data_frame = pd.read_csv("50_states.csv")

state_names = states_data_frame["state"].tolist() # to_list and tolist are aliases
state_x_coord = states_data_frame["x"].tolist()
state_y_coord = states_data_frame["y"].tolist()

states_coords_dict = {}
for i in range(0, len(state_names)):
	states_coords_dict[ state_names[i] ] = ( state_x_coord[i], state_y_coord[i] )
	
# print(states_coords_dict)

# Take input from user until all states have been removed (i.e, the user has guessed all states)



while len(state_names) > 0:
	state_name = ( screen.textinput(f"Guess a state name.(Score: {50 - len(state_names)}/50)", "Enter any name of a U.S. state:") ).title()
	
	if state_name.lower() == "exit": # exit code
		break
	elif state_name in state_names:
		state_names.pop( state_names.index(state_name) )
		board_pen.setposition( states_coords_dict[state_name] )
		board_pen.write(f"{state_name}", align = "center")
	else:
		pass	
	
	score = 50 - len(state_names)


# game has ended (presumably)
if score == 50:
	board_pen.color("red")
	board_pen.setposition((0, 0))
	board_pen.write("You Guessed All The States. You Win!", align = "center", font = ('Arial', 20, 'normal'))
else:
	# missed states are converted to csv
	states_to_learn = pd.DataFrame( { "States To Learn" : state_names } ) # Convert a dict to a data frame
	states_to_learn.to_csv("Missed_States.csv")


"""
#	Here's the code for getting co ordinates to get mouse click coordinates :
	def get_mouse_click_coor(x, y):
		print(x, y)

	turtle.onscreenclick(get_mouse_click_coor)
	turtle.mainloop()
"""


screen.exitonclick()
