###############
### imports ###
###############

import sys
import random
import time

############
### code ###
############

def get_user_guess(input_prompt):
    """ handles user input for game """
    ipt = input(input_prompt)
    if ipt == "x":
        sys.exit()
    elif ipt == "n":
        # exit game, ask if wants to start new one
        return "n"
    elif ipt == "s":
        # cheat
        return "s"
    else:
        try:
            num = int(ipt)
        except:
            num = get_user_guess("please choose an integer only:")  # get new input
        return num


def game():
    """
    runs a round of guessing game. 
    returns None
    ends after user wins, will not continue to additional round. 
    """
    print("starting new game:")
    target = random.randint(1, 20) # get computer guess
    user_guess = get_user_guess("Please  guess:")
    while not user_guess == target:
        if user_guess == "n":
            return
        elif user_guess == "s":
            print("Cheater! the number is:", target)
            user_guess = get_user_guess("Try again:") # ask for new input
            continue # check if new input is equal to target
        # print guess status
        if user_guess < target:
            print("Guess is too small")    
        elif user_guess > target:
            print("Guess is too big")
        
        # ask for new input
        user_guess = get_user_guess("Try again:")
        # loop iteration ends, check if new input is equal to target

    # get to this part only if user_guess == target:
    print("Guess was exact! You win!")
    return


def new_game_input(prompt):
    """ 
    asks if to start a new game
    will ask again if input is not any of the possible answers
    returns T (start new game) or F (don't start new game) """
    
    ipt = input(prompt)
    if ipt == "yes":
        return True
    elif ipt == "no":
        return False
    else: # input not compatible
        return new_game_input("Please answer only using yes or no. Start new game? (yes/no)")


# main running function:
def main():
    """ main function that runs guessing games prompted by user input """
    print("Welcome!")
    new_game = new_game_input("Start new game? (yes/no)")
    while new_game:
        game() # run game. when game ends, will continue to next iteration of loop and ask if to start new game
        new_game = new_game_input("Start new game? (yes/no)")
    
    # user did not want to start a new game
    print("Goodbye!")
    return
    

### run game when file run:
main()
time.sleep(2) 
sys.exit

