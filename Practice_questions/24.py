# Rules of the "Rock, Paper, Scissors" game are:
# Rock beats Scissors,
# Scissors beat Paper,
# Paper beats Rock,
# Two identical moves are a draw.
# Let's play! You will be given valid moves of two Rock, Paper, Scissors players, and have to return which player won: 
# "Player 1 won!" for player 1, and "Player 2 won!" for player 2. In case of a draw return Draw!.
# Examples:
# "scissors",     "paper"     --> "Player 1 won!"
# "scissors",     "rock"      --> "Player 2 won!"
# "paper",        "paper"     --> "Draw!"

def rps(p1,p2):
    if p1 == p2:
        return "Draw"
    
    beats = {"rock":"scissor",
             "paper":"rock",
             "scissor":"paper"}
    
    if beats[p1] == p2:
        return "Player 1 won"
    
    return "Player 2 won"

p1 = "scissor"
p2 = "paper"
print (rps(p1,p2))