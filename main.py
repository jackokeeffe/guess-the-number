import random

num_of_guesses = 10

def start_game():
    global number_to_guess
    number_to_guess = int(random.choice(range(1, 100)))
    player_guess()

def player_guess():
    global the_players_guess
    the_players_guess = int(input('What do you think the number is? (It is between 1 and 100, you have ' + str(num_of_guesses) + ' guesses): '))
    guessing_time()

def guessing_time():
    global num_of_guesses, number_to_guess, the_players_guess
    if the_players_guess > int(number_to_guess):
        num_of_guesses -= 1
        print('Your guess is too high! Try again.')
        player_guess()
    elif the_players_guess < int(number_to_guess):
        num_of_guesses -= 1
        print('Your guess is too low! Try again.')
        player_guess()
    elif the_players_guess == int(number_to_guess):
        print('Congratulations you guessed it! The number was ' + str(number_to_guess))
        answer = input('Play again? (y/n): ')
        if answer == "y":
            num_of_guesses = 10
            start_game()
        elif answer == "n":
            exit()

start_game()
