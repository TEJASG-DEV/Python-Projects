from tkinter import *
from tkinter import messagebox # this is shit... why be explicit... when * handles everything...
import json # We'll be using the json module

# Functions: json.dump(), json.load() and json.update()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import passgen
def gen_passwd():
	password_entry.delete(0, END)
	password = passgen.gen_passwd()
	password_entry.insert(0, password)

# ---------------------------- SEARCH ------------------------------- #
def search():
	try:
		with open("data.json", 'r') as data_file:
			user_data = json.load(data_file)
	except: # for all errors that occur because file doesn't exist.
		message = messagebox.Message(title = "File Not Found", icon = 'warning', message = "Please add / create new user data.")
		messagebox.OK
		message.show()
	else:
		# user data is in dictionary format.

		# get the query within the website entry
		website_name = website_entry.get()
		# get the username and password...
		if website_name in user_data.keys():
			details = f""" Here are your details: 
Website: {website_name} 
Username/Email: {user_data[website_name]['email']} 
Password: {user_data[website_name]['password']} 
							"""
			message = messagebox.Message(title = "Data  Found", icon = 'info', message = details)
			messagebox.OK
			message.show()
		else:
			message = messagebox.Message(title = "No Match", icon = 'warning', message = "User data not found.")
			messagebox.OK
			message.show()
	finally:
		pass


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_user():
	website_name = website_entry.get()
	username_or_email = email_username_entry.get()
	password = password_entry.get()
	
	# Verify weather entry is not empty
	if len(website_name) == 0 or len(username_or_email) == 0 or len(password) == 0:
		message = messagebox.Message(title = "Invalid Input", icon = 'warning', message = "Please enter valid data. Do not leave the fields empty.")
		#messagebox.WARNING = 'warning' # show exclamation mark icon...
		messagebox.OK # Have an OK button
		message.show()

	else:

		# Prompt user before writing
		is_ok = messagebox.askokcancel(title = website_name,
										message = f"These are the details you entered:\nWebsite = {website_name}"f"\nUsername/Email: {username_or_email}"f"\nPassword: {password}\nIs it OK to save?")

		if is_ok:
			data_to_store = { 
								website_name : {
												"email" : username_or_email,
												"password" : password
												}
							}
			try:
				with open("data.json", 'r') as data_file:
					# Test read code first read the data, store it in a variable...
					data = json.load(data_file)
					#print(data) 
					data.update(data_to_store) # then update the old read data with the new data
			except: # Catch all the possible errors that occur above... as it happens because file doesn't exist. 
				with open("data.json", 'w') as data_file:
					json.dump(data_to_store, data_file, indent = 4)
	
			else: # this happens if try is successful... Did this fix by watching video >:-(
				 with open("data.json", 'w') as data_file: # here we write the updated data to the file... clears old data
				 	json.dump(data, data_file, indent = 4)

			finally:
				website_entry.delete(0, END)
				password_entry.delete(0, END)

		else:
			pass

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

window.config(padx = 20, pady = 20)

canvas = Canvas(width = 200, height = 200, highlightthickness = 0) 
logo_image = PhotoImage(file = "logo.png")

canvas.create_image(100, 100, image = logo_image)
canvas.grid(row = 0, column = 1) # grid to be used later

website_label = Label(text = "Website :", anchor = 'e')
website_label.grid(row = 1, column = 0)

website_entry = Entry(width = 21)
website_entry.grid(row = 1, column = 1, sticky = 'W', padx = 4) # columnspan = 2
website_entry.focus()

search_button = Button(text = "Search", command = search, width = 16)
search_button.grid(row = 1, column = 2, sticky = 'W', columnspan = 2)

email_username_label = Label(text = "Email/Username :", anchor = 'e')
email_username_label.grid(row = 2, column = 0)

email_username_entry = Entry(width = 35)
email_username_entry.grid(row = 2, column = 1, columnspan = 2)
email_username_entry.insert(0, "example@example.com")

password_label = Label(text = "Password :", anchor = 'e')
password_label.grid(row = 3, column = 0)

password_entry = Entry(width = 21) # 21
password_entry.grid(row = 3, column = 1, sticky = 'W', padx = 2)

generate_password_button = Button(text = "Generate Password", command = gen_passwd)
generate_password_button.grid(row = 3, column = 2, columnspan = 2, sticky = 'W')

add_button = Button(text = "Add", width = 33, command = add_user)
add_button.grid(row = 4, column = 1, columnspan = 2, sticky = 'E')


window.mainloop()

"""
You might store these passwords in an encrypted format so as to improve security.

also might add features so that entries with the same website name and different usernames can be accessed.

"""


