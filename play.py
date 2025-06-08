from game import main


def play():
    draw = 0
    player1_win = 0
    player2_win = 0

    for _ in range(1000):
        win = main()

        if win == 0:
            draw += 1
        elif win == 1:
            player1_win += 1
        else:
            player2_win += 1
    
    print("After 1000 games:")
    print(f"Draws: {draw}")
    print(f"Player 1 wins: {player1_win}")
    print(f"Player 2 wins: {player2_win}")

play()