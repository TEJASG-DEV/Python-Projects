from turtle import Screen
from board import Board
from ball import Ball
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.tracer(0) # update screen only when update is called
screen.listen() # event listener


player_board = Board('right', screen)
second_player_board = Board('left', screen)
screen.update()

cur_ball = Ball(player_board, second_player_board)
cur_ball.spawn()
screen.update()

screen.onkey(key = "Up",fun = player_board.move_up)
screen.onkey(key = "Down", fun = player_board.move_down)

screen.onkey(key = "w",fun = second_player_board.move_up)
screen.onkey(key = "s", fun = second_player_board.move_down)

is_game_over = False
while not is_game_over:
	cur_ball.start_moving()
	screen.update()
	time.sleep(0.01)
	


screen.exitonclick()
