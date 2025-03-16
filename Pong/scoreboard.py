from turtle import Turtle

class Scoreboard:
	def __init__(self):
		
		self.left_score = 0
		self.right_score = 0

		self.left_side_turtle = Turtle()
		self.left_side_turtle.hideturtle()
		self.left_side_turtle.color("white")
		self.left_side_turtle.penup()
		self.left_side_turtle.setposition(-125, 200)

		self.right_side_turtle = Turtle()
		self.right_side_turtle.hideturtle()
		self.right_side_turtle.color("white")
		self.right_side_turtle.penup()
		self.right_side_turtle.setposition(125, 200)

	def update_score(self, direction):
		if direction == 'left':
			self.left_score += 1
		elif direction == 'right':
			self.right_score += 1
		else:
			pass
		
		self.left_side_turtle.clear()
		self.right_side_turtle.clear()

		self.left_side_turtle.write(f"{self.left_score}", move=False, align='center', font=('Arial', 75, 'normal'))
		self.right_side_turtle.write(f"{self.right_score}", move=False, align='center', font=('Arial', 75, 'normal'))


