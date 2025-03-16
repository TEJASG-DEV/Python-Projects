from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 # 25 mins
SHORT_BREAK_MIN = 5 # 5 mins
LONG_BREAK_MIN = 20 # 20 mins

timer = None
reps = 0
check = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
	global check, timer, reps
	window.after_cancel(timer)
	timer_break_label.config(text = "Timer", fg = GREEN, bg = YELLOW)
	canvas.itemconfig(timer_text, text = "0:00")
	check = ""
	check_marks.config(text = check)
	reps = 0 # this is a nasty one...

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
	# this code is not functional as there's a possibility of memory overflow and it's multi threaded...
	# also this code is asynchronous
	global reps, check
	reps += 1

	if reps % 8 == 0:
		timer_break_label.config(text = "Long Break", fg = GREEN, bg = YELLOW)
		countdown(LONG_BREAK_MIN * 60)
	elif reps % 2 == 0:
		timer_break_label.config(text = "Break", fg = PINK, bg = YELLOW)
		countdown(SHORT_BREAK_MIN * 60)
		check += "🗸"
		check_marks.config(text = check)
	else:
		timer_break_label.config(text = "Work", fg = RED, bg = YELLOW)
		countdown(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
	global timer
	time = f"%01d"%(count // 60) + ":" + f"%02d"%(count % 60) # Thank You Zed Shaw
	canvas.itemconfig(timer_text, text = time) # time
	if count > 0:
		timer = window.after(1000, countdown, count - 1)
	else:
		start_timer() # This is B.S

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

timer_break_label = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 40, "bold"))
timer_break_label.grid(row = 0, column = 1)


canvas = Canvas(width = 206, height = 224, bg = YELLOW, highlightthickness = 0) # thickness = 0 => no borders
tomato_image = PhotoImage(file = "tomato.png")
                       # ,------------ half of the canvas size to be dead center
canvas.create_image(103, 112, image = tomato_image)
canvas.grid(row = 1, column = 1)
timer_text = canvas.create_text(103, 140, text = "0:00", fill = "white", font = (FONT_NAME, 35, "bold"))

start_button = Button(text = "Start", anchor = 'e', highlightthickness = 0, command = start_timer)
start_button.grid(row = 2, column = 0)

reset_button = Button(text = "Reset", anchor = 'w', highlightthickness = 0, command = reset_timer)
reset_button.grid(row = 2, column = 2)

check_marks = Label(text = "", fg = GREEN, bg = YELLOW, font = ("TkDefaultFont", 18, "bold"))
check_marks.grid(row = 3, column = 1)

window.mainloop()
