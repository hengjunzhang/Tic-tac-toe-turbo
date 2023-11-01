from logic import check_winner
def get_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def print_board(board):
    for row in board:
        print(row)

def get_player_input(current_player):
    prompt = f"player{current_player} > "
    player_input = input(prompt)
    row_col_list = player_input.split(',')
    row, col = [int(x) for x in row_col_list]
    return row,col

def switch_player(current_player):
    if current_player == 'X':
        return 'O'
    return 'X'

if __name__ == '__main__':
    current_player = 'X'
    board = get_empty_board()
    winner = None
    while winner is None:
        print_board(board)
        try:
            row, col = get_player_input(current_player)
        except ValueError:
            print("Invalid Input, try again")
            continue

        board[row][col] = current_player
        winner = check_winner(board)
        current_player = switch_player(current_player)
print_board(board)
print(f"Winner is {current_player}")
