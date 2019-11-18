"""

Dev: Josh Porter
Date: 11/17/19
Program: Cpu vs Cpu War game

"""

import random

def victoryScreen(player, hands):
    """Prints a personalized victory screen to the terminal"""

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'~~~~~ {player} wins!! ~~~~~')
    print(f'~~~~~~ In {hands} hands ~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~')


def drawCard(player):
    """Generates and returns a random number that represents a card's value"""

    card = random.randint(0, 14)
    print(f"{player} drew a {card}")
    return card 

def main():
    """Contains the game's loop and all conditional checks"""

    playerOneScore = 0
    playerTwoScore = 0
    numOfHands = 0
    
    while playerOneScore < 10 and playerTwoScore < 10: # Game continues until one of the players score 10
        
        playerOneCard = drawCard(player='player1') # Call the drawcard function using the argument 'player1' for the player parameter
        playerTwoCard = drawCard(player='player2')

        if playerOneCard > playerTwoCard:
            print('Player1 wins the round\n')
            playerOneScore += 1 # increment playerone's score
            numOfHands += 1
        
        elif playerTwoCard > playerOneCard:
            print('Player2 wins the round\n')
            playerTwoScore += 1
            numOfHands += 1

        else:
            print("A tie! no one increases\n")
        
    if playerOneScore == 10:
        victoryScreen(player='player1', hands=numOfHands)
    
    elif playerTwoScore == 10:
        victoryScreen(player='player2', hands=numOfHands)

main()



