import random_ai as rm
import finds_winning_move_ai as wn
import finds_winning_and_losing_moves_ai as wln
import minimax as max
import street_hardened_minimax as smax
import random
import sys 


width = 3
height = 3


def new_board():
    return [[" " for j in range(height)] for i in range(width)]


def game_won(board):
    won_x = ["X", "X", "X"]
    won_o = ["O", "O", "O"]

    for x in range(width):
        columns = []
        for y in range(height):
            columns.append(board[y][x])
        if columns == won_o:
            return "O"
        elif columns == won_x:
            return "X"
        else:
            continue
    
    for y in range(height):
        row = []
        for x in range(width):
            row.append(board[y][x])
        if row == won_o:
            return "O"
        elif row == won_x:
            return "X"
        else:
            continue
    
    main_diag = []

    for i in range(3):
        main_diag.append(board[i][i])
    
    anti_diag = []

    for i in range(width):
        anti_diag.append(board[i][width - i - 1])
    
    if main_diag == won_x:
        return "X"
    elif main_diag == won_o:
        return "O"
    
    if anti_diag == won_x:
        return "X"
    elif anti_diag == won_o:
        return "O"
    
    return None


def get_move(current_player):
    valid_moves = ["0", "1", "2"]
    print()
    x = input(f"{current_player} what is your x cordinate move? ")
    if x not in valid_moves: 
        while x not in valid_moves: 
            x = input(f"{current_player} what is your x cordinate move? ")

    y = input(f"{current_player} what is your y cordinate move? ")
    
    if y not in valid_moves:
        while y not in valid_moves:
            y = input(f"{current_player} what is your y cordinate move? ")

    return (int(x), int(y))


def render_board(board):
    print("   0, 1, 2")
    print("   -------" )
    for x in range(width):
        print(x, end=" ")
        print("|", end=" ")
        for y in range(height):
            print(board[x][y], end=" ")
        print("|", end="")
        print()
    print("   -------")


def is_board_full(board):
    for x in range(width):
        for y in range(height):
            if board[x][y] == " ":
                return False
    
    return True


def make_move(board, move, current_player):
    n_board = board
    if current_player == "X":
        n_board[move[0]][move[1]] = "X"
    else:
        n_board[move[0]][move[1]] = "O"

    return n_board


def is_move_valid(board, move):
    if board[move[0]][move[1]] not in ["X", "O"]:
        return True
    else:
        return False


def which_player_move(player, board, current_player):
    if player == "random_ai":
        move = rm.random_ai(board, current_player)
    elif player == "find_win_loss_ai":  
        move = wln.finds_winning_and_losing_moves_ai(board, current_player)
    elif player == "find_winning_ai":
        move = wn.finds_winning_move_ai(board, current_player)
    elif player == "player":
        move = get_move(current_player)
    elif player == "minimax":
        move = max.minimax_ai(board, current_player)
    elif player == "street_minimax":
        move = smax.minimax_ai(board, current_player)
    
    return move


def get_width(board):
    return len(board)


def get_height(board):
    return len(board[0])


def main():
    players = ["X", "O"]
    player_number = 0
    board = new_board()
    
    random_player = random.randint(0, 1)

    player1 = "street_minimax"
    player2 = "minimax"

    while True:
        if player_number == 2:
            player_number = 0
        current_player = players[player_number % 2]

        # render the current board
        render_board(board)

        # get the players new move
        if player_number == random_player:
            print(f"player = {player1} current_player = {current_player}")
            move = which_player_move(player1, board, current_player)
        else:
            print(f"player = {player2} current_player = {current_player}")
            move = which_player_move(player2, board, current_player)
        
        while True:

            if is_move_valid(board, move):
                # Update the board
                board = make_move(board, move, current_player)

                break
            else:
                print()
                print("square is already taken please try again")
            
            if player_number == random_player:
                print(f"player = {player1} current_player = {current_player}")
                move = which_player_move(player1, board, current_player)
            else:
                print(f"player = {player2} current_player = {current_player}")
                move = which_player_move(player2, board, current_player)

        # Finish the game if someone won
        winner = game_won(board)
        if winner is not None:
            render_board(board)
            print(f"{winner} won congrulations")
            break

        if is_board_full(board):
            render_board(board)
            print("DRAW!")
            break
        
        player_number += 1

        
if __name__ == "__main__":
    main()
