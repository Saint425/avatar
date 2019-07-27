import random
user = input("Please choose one of the Elements: Water, Earth, Fire, or Air.\n") #Players Input from one of the Elements  
computer_elements = ['Water', 'Earth', 'Fire', 'Air'] #Computers Choices  
computer_input = random.choice(computer_elements) #Computer Randomly Picks from elements list 
print("Computer's Element is:", computer_input) #Shows Computer's Choice
if computer_input == user:	
    print('A Tie!! D:') 
elif user == 'Air' and computer_input == 'Water':
    print('You Win :D') 
elif user == 'Air' and computer_input == 'Fire':
	print('You lose D: Computer wins :D')	
elif user == 'Air' and computer_input == 'Earth':
	print('You lose D: Computer wins :D') 
elif user == 'Earth' and computer_input == 'Fire':
    print('You lose D: Computer wins :D')  
elif user == 'Earth' and computer_input == 'Water':
	print('You Win :D')  
elif user == 'Earth' and computer_input == 'Air':
	print('You lose D: Computer wins :D')  
elif user == 'Water' and computer_input == 'Fire':
    print('You Win :D') 
elif user == 'Water' and computer_input == 'Air':
	print('You lose D: Computer wins :D') 
elif user == 'Water' and computer_input == 'Earth':
	print('You lose D: Computer wins :D')
elif user == 'Fire' and computer_input == 'Water':
	print('You lose D: Computer wins :D') 
elif user == 'Fire' and computer_input == 'Earth':
	print('You Win :D') 
elif user == 'Fire' and computer_input == 'Air':
	print('You Win :D')
else:
	print('Error, please try again D:') # Error should you input anything other than one of the four elements
