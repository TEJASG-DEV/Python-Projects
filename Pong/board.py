from turtle import Turtle

OFFSETS = [-40 , -20, 0, 20, 40]
class Board:
	
	def __init__(self, direction, turtle_screen):
		self.make_board(direction, turtle_screen)

	def make_board(self, direction, turtle_screen):
		self.segments = []
		self.turtle_screen = turtle_screen
		
		if direction == 'left':
			x_pos = -380
		else: # right
			x_pos = 380

		for offset in OFFSETS:
			segment = Turtle("square")
			segment.penup()
			segment.color("white")
			
			# The below if block helps to move the board up or down later by using just the forward function
			if offset == -40:
				segment.setheading(270)
			elif offset == 40:
				segment.setheading(90) 
			else:
				pass
			
			segment.setposition(x_pos, offset)
			self.segments.append(segment)

	
	def move_up(self):
		old_pos = self.segments[-1].pos()
		if self.segments[-1].ycor() == 280: # move within the boundary of the screen
			pass
		else:
			self.segments[-1].forward(20)
			for i in range(2, (len(self.segments) + 1)): # -2 to -4... -5 is needed just to see the nature of range()
				if i == 2: # first:
					cur_pos = self.segments[-1 * i].pos()
					self.segments[-1 * i].setposition(old_pos) # for -1th position
					prev_pos = cur_pos
				else:
					cur_pos = self.segments[-1 * i].pos()
					self.segments[-1 * i].setposition(prev_pos) # for -ith position
					prev_pos = cur_pos

		self.turtle_screen.update()

	def move_down(self):
		old_pos = self.segments[0].pos()
		if self.segments[0].ycor() == -280:
			pass
		else:
			self.segments[0].forward(20) # remember during initialization i have set the headings differently...
			for i in range(1, len(self.segments)):
				if i == 1:
					cur_pos = self.segments[i].pos()
					self.segments[i].setposition(old_pos)
					prev_pos = cur_pos
				else:
					cur_pos = self.segments[i].pos()
					self.segments[i].setposition(prev_pos)
					prev_pos = cur_pos

		self.turtle_screen.update()
