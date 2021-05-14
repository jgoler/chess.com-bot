import copy
#the board is 7 long by 6 high
#our player uses 1 and their player uses 2 to indicate that the spot is theirs
gameboard = [[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]]

def winner_exists(gameboard):
    row = 0
    x_value = 0
    while (row < 6 and x_value < 4):
        if (int(gameboard[row][x_value]) == int(gameboard[row][x_value + 1])) and (int(gameboard[row][x_value]) == int(gameboard[row][x_value + 2])) and (int(gameboard[row][x_value]) == int(gameboard[row][x_value + 3])) and (int(gameboard[row][x_value]) != 0):
            return True
        if (x_value == 3):
            x_value = 0
            row += 1
        else:
            x_value += 1  
        
    row = 0
    x_value = 0
    while (row < 3 and x_value < 7):
        if (int(gameboard[row][x_value]) == int(gameboard[row + 1][x_value])) and (int(gameboard[row][x_value]) == int(gameboard[row + 2][x_value])) and (int(gameboard[row][x_value]) == int(gameboard[row + 3][x_value])) and (int(gameboard[row][x_value]) != 0):
            return True
        if (row == 2 and x_value != 6):
            x_value += 1
            row = 0
        else:
            row += 1
    row = 0
    x_value = 0
    while (row < 3 and x_value < 7):
        if (x_value < 4):
            if (int(gameboard[row][x_value]) == int(gameboard[row + 1][x_value + 1])) and (int(gameboard[row][x_value]) == int(gameboard[row + 2][x_value + 2])) and (int(gameboard[row][x_value]) == int(gameboard[row + 3][x_value + 3])) and (int(gameboard[row][x_value]) != 0):
                return True
        if (x_value > 2):
            if (int(gameboard[row][x_value]) == int(gameboard[row + 1][x_value - 1])) and (int(gameboard[row][x_value]) == int(gameboard[row + 2][x_value - 2])) and (int(gameboard[row][x_value]) == int(gameboard[row + 3][x_value - 3])) and (int(gameboard[row][x_value]) != 0):
                return True
        if (x_value < 6):
            x_value += 1  
        else:
            row += 1
            x_value = 0
    return False


def play(gameboard, first):
    current_player = first
    print(winner_exists(gameboard))
    while (not winner_exists(gameboard)):
        print("Please make your move player ", current_player)
        #print("{b1}! This is {b2}.".format(b1 = n1, b2 = n2))
        xcoord = input("What is the x-coordinate of where you want to go? ")
        ycoord = input("And what is the y-coordinate of where you want to go? ")
        #print("{b1},{b2}".format(b1=xcoord, b2=ycoord))
        if gameboard[int(ycoord)-1][int(xcoord)-1] != 0:
            print("That position is already taken, please choose a different position")
        else:
            gameboard[int(ycoord)-1][int(xcoord)-1] = current_player
            if current_player == 1:
                current_player = 2
            else:
                current_player = 1
        print_board(gameboard)


def print_board(gameboard):
    row = 5
    #print('__________________')
    print('_______________')
    while row >= 0:
        current_pos = gameboard[row][0]
        second_pos = gameboard[row][1]
        third_pos = gameboard[row][2]
        fourth_pos = gameboard[row][3]
        fifth_pos = gameboard[row][4]
        sixth_pos = gameboard[row][5]
        seventh_pos = gameboard[row][6]
        #print("|{n1}|".format(n1=current_pos)
        print("|{b1}|{b2}|{b3}|{b4}|{b5}|{b6}|{b7}|".format(b1 = current_pos, b2 = second_pos, b3=third_pos, b4=fourth_pos, b5=fifth_pos, b6=sixth_pos, b7=seventh_pos))
        print('_______________')
        row -= 1

def test(gameboard):
    print(gameboard[6][0])

print_board(gameboard)
play(gameboard, 1)
print(winner_exists(gameboard))


def find_children(state, current_player):
    children = []
    for x in range(len(state))[::-1]:
        for y in range(len(state[x])):
            if (state[x][y] == 0):
                new_state = copy.deepcopy(state)
                new_state[x][y] = current_player
                children.append(new_state)
    return children

def heuristic(state):
    #figure out number of fours in a row for one player
    
    #figure out number of threes in a row for one player
    #figure out number of twos in a row for one player
    #do same for other player and subtract
#state is current state, depth is amount of moves we want to search, and maximizingPlayer tells us if we ar enemy or not
def minimax(state, depth, maximizingPlayer):
    if (depth == 0) or (winner_exists(state)):
        return heuristic(state) 
    if maximizingPlayer:
        maxEval = -infinity
        for x in find_children(state, 1):
            eval = minimax(child, depth - 1, false)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = +infinity
        for y in find_children(state, 0):
            eval = minimax(child, depth-1, true)
            minEval = min(minEval, eval)
        return minEval