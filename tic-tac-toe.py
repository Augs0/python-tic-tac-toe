gameboard_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
# this is an f string which helps format variables :)


def build_board():
    board = f"""  
    ---------
    | {gameboard_list[0]} {gameboard_list[1]} {gameboard_list[2]} |
    | {gameboard_list[3]} {gameboard_list[4]} {gameboard_list[5]} |
    | {gameboard_list[6]} {gameboard_list[7]} {gameboard_list[8]} |
    ---------"""
    print(board)


valid_moves = [['1', '3'], ['2', '3'], ['3', '3'],
              ['1', '2'], ['2', '2'], ['3', '2'],
              ['1', '1'], ['2', '1'], ['3', '1']]

rounds = 0

def calculate_move():
    global rounds
    move = input('Enter the coordinates:').split()
    if move in valid_moves:
        square = valid_moves.index(move)
        if gameboard_list[square] != " ":
            print('This cell is occupied! Choose another one!')
            if rounds < 9:
                rounds += 1
                return calculate_move()
            else:
                state_of_play()    
        else:
            if rounds < 9:
                if rounds % 2 != 0:
                    gameboard_list[square] = 'X'
                else:
                    gameboard_list[square] = 'O'
                build_board()
                rounds += 1
                return calculate_move()
            else:
                state_of_play()
    else:
        try:
            if all(int(coord) for coord in move):
                print("Coordinates should be from 1 to 3!")
                return calculate_move()
        except ValueError:
                print("You should enter numbers!")
                return calculate_move()


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

build_board()
calculate_move()
