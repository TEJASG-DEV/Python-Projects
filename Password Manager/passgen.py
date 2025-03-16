#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4) # As per Yu's Code.

def gen_passwd():
	# Select random characters from the above lists as per their respective length criteria
	rand_numlist = random.sample(numbers, nr_numbers)
	rand_symbols = random.sample(symbols, nr_symbols)
	rand_letters = random.sample(letters, nr_letters)

	# Merge the above lists and shuffle the list to get the password string list
	pass_list = [] # create empty list and extend... refer python list documentation
	pass_list.extend(rand_numlist)
	pass_list.extend(rand_symbols)
	pass_list.extend(rand_letters)

	# password list created. now shuffling them

	random.shuffle(pass_list) # you can shuffle it n times to get a random password...

	# Now to make a string from the list... using concatenation
	pass_string = ''

	for char in pass_list:
		pass_string = pass_string + char
	
	return pass_string
