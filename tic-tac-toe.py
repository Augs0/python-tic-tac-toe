gameboard = input()
gameboard_list = list(gameboard)

print('---------')
print('| {} {} {} |'.format(gameboard[0], gameboard[1], gameboard[2]))
print('| {} {} {} |'.format(gameboard[3], gameboard[4], gameboard[5]))
print('| {} {} {} |'.format(gameboard[6], gameboard[7], gameboard[8]))
print('---------')

winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]

def state_of_play():
    wins = 0
    spaces = 0
    x_wins = 0
    o_wins = 0
    if gameboard_list.count('X') - gameboard_list.count('O') > 1 or gameboard_list.count('O') - gameboard_list.count('X') > 1:
        print('Impossible')
        return
    else:
        for winning_combo in winning_combos:
             if gameboard_list[winning_combo[0]] == 'X' and gameboard_list[winning_combo[1]] == 'X' and gameboard_list[winning_combo[2]] == 'X':
                 wins += 1   
                 x_wins += 1 
             elif gameboard_list[winning_combo[0]] == 'O' and gameboard_list[winning_combo[1]] == 'O' and gameboard_list[winning_combo[2]] == 'O':
                 wins += 1
                 o_wins += 1
             elif gameboard_list[winning_combo[0]] == '_' or gameboard_list[winning_combo[0]] == ' ' or gameboard_list[winning_combo[1]] == '_' or gameboard_list[winning_combo[1]] == ' ' or gameboard_list[winning_combo[2]] == '_' or gameboard_list[winning_combo[2]] == ' ':  
                 spaces += 1
        if x_wins >= 1 and o_wins >= 1:
            print('Impossible')
            return
        elif wins == 0 and spaces == 0:
            print('Draw')
            return
        elif wins == 0 and spaces != 0:
            print('Game not finished')
            return    
        elif x_wins > o_wins:
            print('X wins')
        elif o_wins > x_wins:
            print('O wins')     
                   
state_of_play()

