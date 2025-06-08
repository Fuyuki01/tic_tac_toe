import copy
import game 


def minimax_ai(board, current_player):
    best_move = None
    best_score = None

    for move in get_legal_moves(board):
        new_board = copy.deepcopy(board)

        game.make_move(new_board, move, current_player)

        oponent = get_opponent(current_player)

        score = minimax(new_board, oponent, current_player)

        if best_score is None or best_score < score:
            best_score = score
            best_move = move
        
    return best_move


def minimax(board, current_player, original_player):
    winner = game.game_won(board)

    if winner is not None:
        if winner == original_player:
            return +10
        else:
            return -10
    
    if game.is_board_full(board):
        return 0
    
    legal_moves = get_legal_moves(board)

    scores = []

    for move in legal_moves:
        new_board = copy.deepcopy(board)
        game.make_move(new_board, move, current_player)

        opponent = get_opponent(current_player)
        score = minimax(new_board, opponent, original_player)
        scores.append(score)
    
    if current_player == original_player:
        return max(scores)
    else:
        return min(scores)




def get_legal_moves(board):
    return [(x, y) for x in range(game.get_width(board)) for y in range(game.get_height(board)) if board[x][y] == " " ]


def get_opponent(current_player):
    if current_player == "O":
        return 'X'
    else:
        return "O"

        

