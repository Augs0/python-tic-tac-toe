gameboard = input('Enter cells:')
gameboard_list = list(gameboard)

print('---------')
print('| {} {} {} |'.format(gameboard_list[0], gameboard_list[1], gameboard_list[2]))
print('| {} {} {} |'.format(gameboard_list[3], gameboard_list[4], gameboard_list[5]))
print('| {} {} {} |'.format(gameboard_list[6], gameboard_list[7], gameboard_list[8]))
print('---------')


valid_moves = [['1', '3'], ['2', '3'], ['3', '3'],
              ['1', '2'], ['2', '2'], ['3', '2'],
              ['1', '1'], ['2', '1'], ['3', '1']]

def calculate_move():
    move = input('Enter the coordinates:').split()
    if move in valid_moves:
        square = valid_moves.index(move)
        if gameboard_list[square] != '_' or '':
            print('This cell is occupied! Choose another one!')
            return calculate_move()
        else:
             gameboard_list[square] = 'X'
    else:
        try:
            if all(int(coord) for coord in move):
                print("Coordinates should be from 1 to 3!")
                return calculate_move()
        except ValueError:
                print("You should enter numbers!")
                return calculate_move()
      

calculate_move()


print('---------')
print('| {} {} {} |'.format(gameboard_list[0], gameboard_list[1], gameboard_list[2]))
print('| {} {} {} |'.format(gameboard_list[3], gameboard_list[4], gameboard_list[5]))
print('| {} {} {} |'.format(gameboard_list[6], gameboard_list[7], gameboard_list[8]))
print('---------')
