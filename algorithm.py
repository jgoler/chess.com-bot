#the board is 7 long by 6 high

gameboard = [[0, 0, 0, 0, 0, 0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
def play(gameboard, first):
	print("The player that will go first is player", first)
	#print("{b1}! This is {b2}.".format(b1 = n1, b2 = n2))
	xcoord = input("What is the x-coordinate of where you want to go? ")
	ycoord = input("And what is the y-coordinate of where you want to go? ")
	#print("{b1},{b2}".format(b1=xcoord, b2=ycoord))
	if gameboard[int(xcoord)][int(ycoord)] != 0:
		print("That position is already taken, please choose a different position")
	else:
		gameboard[int(xcoord)][int(ycoord)] = first

def print_board(gameboard):
	column = 0
	while column < 7:
		row = 0
		while row < 6:
			print(gameboard[column][row])
			row += 1
		column += 1


play(gameboard, 1)

#def test():
	#tester = [[1,2,3], [4,5,6],[7,8,9]]
	#print(tester[2][2])


#test()
