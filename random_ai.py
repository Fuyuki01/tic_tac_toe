import random


def random_ai(board, current_player):
    empty_cells = [(x, y) for x in range(get_width(board)) for y in range(get_height(board)) if board[x][y] == " "]

    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None

def get_width(board):
    return len(board)


def get_height(board):
    return len(board[0])