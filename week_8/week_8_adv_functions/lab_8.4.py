def find_winner(player1 = "Rock", player2 = "Rock"):
    if player1 == player2:
        print("Tie")
    elif (player1 == "Rock" and player2 == "Scissors") or \
        (player1 == "Scissors" and player2 == "Paper") or \
        (player1 == "Paper" and player2 == "Rock"):
        print("1 wins")
    else:
        print("2 wins")

find_winner("Rock", "Paper") # "Player 2 wins!"
find_winner("Scissors", "Paper") # "Player 1 wins!"
find_winner("Rock", "Rock") # "It's a tie!"
find_winner("Rock") # "It's a tie!"
find_winner() # "It's a tie!"
find_winner("Scissors") # "Player 2 wins!"