#the board is 7 long by 6 high

gameboard = [[0, 1, 2, 3, 4, 5],[6,7,8,9,10,11],[12,13,14,15,16,17],[18,19,20,21,22,23],[24,25,26,27,28,29],[30,31,32,33,34,35],[36,37,38,39,40,41]]
def play(gameboard):
	print("play function")

def print_board(gameboard):
	column = 0
	while column < 7:
		row = 0
		while row < 6:
			print(gameboard[column][row])
			row += 1
		column += 1


print_board(gameboard)

#def test():
	#tester = [[1,2,3], [4,5,6],[7,8,9]]
	#print(tester[2][2])


#test()
