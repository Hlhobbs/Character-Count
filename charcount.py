#Name: Hayden Hobbs
#Date of Completion: 1/19/18

def make_message( word_arg ):
	message = word_arg + " has " + str( len(word_arg) ) + " characters."
	return message
	
function_ref = make_message #Now, function_ref refers to the same function as make_message

while True:
	word = input("Type a word, followed by Enter (to quit, type 'quit'): ")
	if word == 'quit':
		break
	print( function_ref( word)) #make_message and function_call the same function now