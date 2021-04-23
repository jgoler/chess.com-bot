#the board is 7 long by 6 high

gameboard = [[0, 0, 0, 0, 0, 0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
def play(gameboard, first):
	print("The player that will go first is player", first)
	#print("{b1}! This is {b2}.".format(b1 = n1, b2 = n2))
	xcoord = input("What is the x-coordinate of where you want to go? ")
	ycoord = input("And what is the y-coordinate of where you want to go? ")
	#print("{b1},{b2}".format(b1=xcoord, b2=ycoord))
	if gameboard[int(xcoord)-1][int(ycoord)-1] != 0:
		print("That position is already taken, please choose a different position")
	else:
		gameboard[int(xcoord)-1][int(ycoord)-1] = first
	print_board(gameboard)


def is_winner(gameboard):
	return true

def print_board(gameboard):
	row = 0
	#print('__________________')
	print('_______________')
	while row < 6:
		current_pos = gameboard[0][5-row]
		second_pos = gameboard[1][5-row]
		third_pos = gameboard[2][5-row]
		fourth_pos = gameboard[3][5-row]
		fifth_pos = gameboard[4][5-row]
		sixth_pos = gameboard[5][5-row]
		seventh_pos = gameboard[6][5-row]
		#print("|{n1}|".format(n1=current_pos)
		print("|{b1}|{b2}|{b3}|{b4}|{b5}|{b6}|{b7}|".format(b1 = current_pos, b2 = second_pos, b3=third_pos, b4=fourth_pos, b5=fifth_pos, b6=sixth_pos, b7=seventh_pos))
		print('_______________')
		row += 1

def test(gameboard):
	print(gameboard[6][0])

play(gameboard, 1)

#def test():
	#tester = [[1,2,3], [4,5,6],[7,8,9]]
	#print(tester[2][2])


#test()
