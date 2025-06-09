import random
import copy
import game


def finds_winning_move_ai(board, current_player):
    for x in range(get_width(board)):
        for y in range(get_height(board)):
            if board[x][y] == " ":
                temp_board = copy.deepcopy(board)
                temp_board[x][y] = current_player
                if game.game_won(temp_board):
                    return (x, y)
                else:
                    continue
    
    empty_cells = [(x, y) for x in range(get_width(board)) for y in range(get_height(board)) if board[x][y] == " "]

    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None


def get_width(board):
    return len(board)


def get_height(board):
    return len(board[0])

