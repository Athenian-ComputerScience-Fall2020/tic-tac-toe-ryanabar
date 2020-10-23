# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.

theBoard = {'UL': ' ', 'UM': ' ', 'UR': ' ',
              'ML': ' ', 'MM': ' ', 'MR': ' ',
              'LL': ' ', 'LM': ' ', 'LR': ' '}
def show_board(theBoard):
        print('  ', theBoard['UL'], '  |','  ' ,theBoard['UM'], '  |', '  ',theBoard['UR'])
        print('-------+--------+--------')
        print('  ', theBoard['ML'], '  |','  ' ,theBoard['MM'], '  |', '  ',theBoard['MR'])
        print('-------+--------+--------')
        print('  ', theBoard['LL'], '  |','  ' ,theBoard['LM'], '  |', '  ',theBoard['LR'], '\n')
def directions():
        print("Enter which position acronym you want your X or O to go.")
        print("\n")
        print("\n")
        print('  ', 'UL', '  |','  ' ,'UM', '  |', '  ','UR')
        print('--------+---------+--------')
        print('  ', 'ML', '  |','  ' ,'MM', '  |', '  ','MR')
        print('--------+---------+--------')
        print('  ', 'LL', '  |','  ' ,'LM', '  |', '  ','LR', '\n')
        print('=========================')
        print("\n")
def winner_winner_chicken_dinner(theBoard):
    check = 0
    if theBoard['UL'] == theBoard['UM'] == theBoard['UR'] != ' ' :
        check = 1
    elif theBoard['UL'] == theBoard['ML'] == theBoard['LL'] != ' ':
        check = 1
    elif theBoard['UL'] == theBoard['MM'] == theBoard['LR'] != ' ':
        check = 1
    elif theBoard['ML'] == theBoard['MM'] == theBoard['MR'] != ' ':
        check = 1
    elif theBoard['LL'] == theBoard['LM'] == theBoard['LR'] != ' ':
        check = 1
    elif theBoard['LL'] == theBoard['MM'] == theBoard['UR'] != ' ':
        check = 1
    elif theBoard['UR'] == theBoard['MR'] == theBoard['LR'] != ' ':
        check = 1
    elif theBoard['LM'] == theBoard['MM'] == theBoard['UM'] != ' ':
        check = 1
    return check
def play(theBoard):
    node = "X"
    for i in range(9):
        directions()
        show_board(theBoard)
        print('It is ', node, 'turn to play.')
        print("\n'")
        turn = input()
        while True:
            if theBoard[turn] == ' ':
                theBoard[turn] = node
                break
            else:
                print("That spot has already been taken. Place your", node, "somewhere else please.")
                print("\n")
                directions()
                show_board(theBoard)
                turn = input()
        check = winner_winner_chicken_dinner(theBoard)
        if check == 1:
            print('The winner is', node)
            break
        else:
            print("There was no winner. Would you like to play again?")
        cont = input("Please say yes or no. ")
        if cont == "no":
            break;
        elif cont == "No":
            break;
        if node == 'X':
            node = 'O'
        else:
            node = 'X'

play(theBoard)
