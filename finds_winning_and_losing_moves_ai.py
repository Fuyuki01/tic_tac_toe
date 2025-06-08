import random
import copy


def finds_winning_and_losing_moves_ai(board, current_player):

    for x in range(get_width(board)):
        for y in range(get_height(board)):
            if board[x][y] == " ":
                temp_board = copy.deepcopy(board)
                temp_board[x][y] = current_player
                if game_won(temp_board):
                    return (x, y)
                else:
                    continue
    
    for x in range(get_width(board)):
        for y in range(get_height(board)):
            if board[x][y] == " ":
                temp_board = copy.deepcopy(board)
                if current_player == "X":
                    temp_board[x][y] = "O"
                    if game_won(temp_board):
                        return (x, y)
                    else:
                        continue
                elif current_player == "O":
                    temp_board[x][y] = "X"
                    if game_won(temp_board):
                        return (x, y)
                    else:
                        continue
    
    empty_cells = [(x,y) for x in range(get_width(board)) for y in range(get_height(board)) if board[x][y] == " "]

    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None



def get_width(board):
    return len(board)


def get_height(board):
    return len(board[0])


def game_won(board):
    won_x = ["X", "X", "X"]
    won_o = ["O", "O", "O"]

    for x in range(get_width(board)):
        columns = []
        for y in range(get_height(board)):
            columns.append(board[y][x])
        if columns == won_o:
            return "O"
        elif columns == won_x:
            return "X"
        else:
            continue
    
    for y in range(get_height(board)):
        row = []
        for x in range(get_width(board)):
            row.append(board[y][x])
        if row == won_o:
            return "O"
        elif row == won_x:
            return "X"
        else:
            continue
    
    main_diag = []

    for i in range(get_width(board)):
        main_diag.append(board[i][i])
    
    anti_diag = []

    for i in range(get_width(board)):
        anti_diag.append(board[i][get_width(board) - i - 1])
    
    if main_diag == won_x:
        return "X"
    elif main_diag == won_o:
        return "O"
    
    if anti_diag == won_x:
        return "X"
    elif anti_diag == won_o:
        return "O"
    
    return None