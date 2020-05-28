#tictactor by python
#easy gaming programming

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

turn = 'X'
for picking in range(9):
    print("Turn " + turn)
    print("Please enter location you want to put " + turn)
    pick = input()
    theBoard[pick] = turn
    printBoard(theBoard)

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
