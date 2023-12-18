import random
rock = """
    _______
---'    ____)
       (_____)
       (_____)
       (____)
---.___(___)
"""
paper = """
    _______
---'    ____)____
            ______)
           _______)
          _______)
---.__________)
"""
scissors = """
    _______
---'    ____)____
            ______)
        __________)
      (____)
---.__(___)
"""

def printMove(move):
    if move == 'rock':
        return rock
    if move == 'paper':
        return paper
    if move == 'scissors':
        return scissors

def makePlayerMove(playerName):
    validMoves = ["rock","paper","scissors"]
    while True:
        playerMove = input("Chose: rock, paper, or scissors? ")
        playerMove = playerMove.lower()
        if playerMove in validMoves:
            break
        else:
            print("Invalid Input, try again")
    playerArt = printMove(playerMove)
    print(playerName, "Choose:", playerArt)

    return playerMove

def makeComputerMove(computerName):
    moves = ["rock","paper","scissors"]
    computerMove = random.choice(moves)
    computerArt = printMove(computerMove)
    print(computerName," chose: ", computerArt)

# Code
    return computerMove

def checkRoundWinner(playerMove, computerMove,playerName, computerName):
    if playerMove == computerMove:
        return "It was a tie!"
    elif (playerMove == "rock" and computerMove == "scissors") or \
        (playerMove == "scissors" and computerMove == "paper") or \
        (playerMove == "paper" and computerMove == "rock"):
            return f"{playerName} won the round!"
    else:
        return f"{computerName} won the round!"

def main():
    playerName = input("What would you like the player's name to be? ")
    computerName = input("What would you like the computer's name to be? ")
    playerScore = 0
    computerScore = 0

    while playerScore < 2 and computerScore < 2:
        playerMove = makePlayerMove(playerName)
        computerMove = makeComputerMove(computerName)

        roundWinner = checkRoundWinner(playerMove,computerMove, playerName, computerName)
        print(roundWinner)

        if roundWinner == f"{playerName} won the round!":
            playerScore += 1
        elif roundWinner == f"{computerName} won the round!":
            computerScore += 1

        if playerScore == 2:
            print(playerName, "won the match!")
            break
        elif computerScore == 2:
            print(computerName, "won the match!")
            break

main()
