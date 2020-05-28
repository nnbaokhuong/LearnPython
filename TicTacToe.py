# tictactoe by python
# easy gaming programming

print('--------------')
print('TicTacToe game')
print('-Demo version-')
print('--------------')
print()
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


theBoard = {
    '1' : '1',
    '2' : '2',
    '3' : '3',
    '4' : '4',
    '5' : '5',
    '6' : '6',
    '7' : '7',
    '8' : '8',
    '9' : '9'
    }

#Choose your turn
print("Player X or O?")
print("Please input X or O")
turn = input()
turn1 = turn.lower()
while turn1 != 'x' and turn != 'o':
    print("Please input X or O")
    turn = input()
    
printBoard(theBoard)

for picking in range(9):
    print("Turn " + turn)
    print("Please enter location you want to put " + turn)
    pick = input()
    if int(pick) not in range(9):
        print('Please enter in range from 1 to 9 only')
        pick=input()
        
    theBoard[pick] = turn
    printBoard(theBoard)

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
