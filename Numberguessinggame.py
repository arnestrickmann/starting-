"""Number Guessing Game"""

import random 

attempts_list = []

def show_score():
    if len(attempts_list)<=0:
        print("There is currently no highscore, its yours for the taking!")
    else:
        print("The currrent highscore is {} attempts".format(min(attempts_list)))

def start_game():
    random_number = int(random.randint(1, 10))
    print ("Hello Traveler, welcome to the game of guesses!")

player_name = input("What is your name?")

wanna_play = input ("Hi, {}, would you like to play the guessing name? (Enter Yes/No)".format(player_name))


attempts = 0

show_score ()
random_number = int(random.randint(1, 10))
play_again = input ()

while True:
    try:
        guess = input ("Pick a number between 1 and 10.")
        if int(guess) < 1 or int(guess) >10:
            raise ValueError("Please guess a number within the given range.")
        if int(guess) == random_number :
            print ("Nice you got it.")
            attempts += 1
            attempts_list.append(attempts)
            print("It took you {} attempts".format(attempts))
            play_again = input ("Would you like to play again? (Enter yes/no)")
            attempts = 0
            show_score ()
            random_number = int(random.randint(1, 10))
        if play_again.lower () == "no":
            print("Thats cool, have a good one.")
        elif int(guess)>random_number:
            print("Its lower.")
            attempts += 1
        elif int(guess) < random_number:
            print("Its higher")
            attempts += 1


    except ValueError as err:
        print("Oh no, that is not a valid value. Try again...")
        print("({})".format.err)

    else:
        print ("Thats cool, have a good one.")

if __name__ == 'main':
    start_game()


