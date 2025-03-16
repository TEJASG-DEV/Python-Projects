from turtle import Turtle
from scoreboard import Scoreboard
import random

DIST_UNITS = 2 # any units that divide 380, 280 properly... 1, 2, 4, 5, 8, 10, 20 but beyond 2 the game gets harder...  

FORTY_FIVE = (DIST_UNITS, DIST_UNITS)
ONE_THIRTY_FIVE = (-DIST_UNITS, DIST_UNITS)
TWO_TWENTY_FIVE = (-DIST_UNITS, -DIST_UNITS)
THREE_FIFTEEN = (DIST_UNITS, -DIST_UNITS)

ANGLES = [FORTY_FIVE, ONE_THIRTY_FIVE, TWO_TWENTY_FIVE, THREE_FIFTEEN]

class Ball(Turtle):
	def __init__(self, board1_instance, board2_instance):
		
		super().__init__()
		self.hideturtle()
		self.shape("circle")
		self.color("red")
		self.penup()
		# set initial heading... later update with collission
		self.heading_angle = random.choice(ANGLES)

		# have a board reference within this class
		self.board1_reference = board1_instance
		self.board2_reference = board2_instance

		# scoreboard
		self.scoreboard = Scoreboard()
		self.scoreboard.update_score("none") # hits pass statement and 0, 0  score will be displayed
		
	def spawn(self):
		random_y_coord = 20 * random.randint(-13, 13) # between -260 to 260 in increments of 20
		self.setposition(0, random_y_coord)
		self.showturtle()

	def hit_the_top(self):
		return (round(self.ycor()) == 280) # This will evaluate to false if round is not used...

	def hit_the_bottom(self):
		return (round(self.ycor()) == -280) # or you may use == 280.0 try and see...

	def start_moving(self):
		# to get the y co ordinates of the board
		def get_board_ylist(board_reference):
			y_list = []
			for segment in board_reference.segments:
				y_list.append( round( segment.ycor() ) )

			return y_list
		
		# check if gone beyond board left or right
		if (self.xcor() > 390):
			self.scoreboard.update_score("left") # left player
			# left player gets point
			self.spawn()
		elif (self.xcor() < -390):
			self.scoreboard.update_score("right")
			self.spawn()
		else:
			pass


		cur_pos = self.pos()
		# Bouncing logic below.. if the ball hits the wall
		if (self.hit_the_top() and (self.heading_angle == FORTY_FIVE)): # self.hit_the_top() instead of hit_the_top(self)
			self.heading_angle = THREE_FIFTEEN
		elif (self.hit_the_top() and (self.heading_angle == ONE_THIRTY_FIVE)):
			self.heading_angle = TWO_TWENTY_FIVE
		elif (self.hit_the_bottom() and (self.heading_angle == THREE_FIFTEEN)):
			self.heading_angle = FORTY_FIVE
		elif (self.hit_the_bottom() and (self.heading_angle == TWO_TWENTY_FIVE)):
			self.heading_angle = ONE_THIRTY_FIVE
		else:
			pass
			#print("Some corner case regarding top and bottom hit.")

		# Detect collission with board ... if x_coord == (+/-)360 and 
		board1_ylist = get_board_ylist(self.board1_reference)
		board2_ylist = get_board_ylist(self.board2_reference)

		if ( (round(self.xcor()) == 360) and (round(self.ycor()) in board1_ylist) and (self.heading_angle == THREE_FIFTEEN) ):
			self.heading_angle = TWO_TWENTY_FIVE
		elif ( (round(self.xcor()) == 360) and (round(self.ycor()) in board1_ylist) and (self.heading_angle == FORTY_FIVE) ):
			self.heading_angle = ONE_THIRTY_FIVE
		elif ( (round(self.xcor()) == -360) and (round(self.ycor()) in board2_ylist) and (self.heading_angle == ONE_THIRTY_FIVE) ):
			self.heading_angle = FORTY_FIVE
		elif ( (round(self.xcor()) == -360) and (round(self.ycor()) in board2_ylist) and (self.heading_angle == TWO_TWENTY_FIVE) ):
			self.heading_angle = THREE_FIFTEEN
		else:
			pass

		new_pos = (cur_pos[0] + self.heading_angle[0], cur_pos[1] + self.heading_angle[1])
		self.setposition(new_pos)


