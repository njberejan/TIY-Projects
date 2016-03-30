import random

number_of_guesses = 0

#computer must pick random number between 1 and 100.
def generate_random_number():
    return random.randint(1, 100)

#ask for user guess of computer's random number.
def prompt_player():
    player_guess = input("Please guess a number between 1 and 100: ")
    return player_guess

#keep count of the number of guesses.
def increase_guess(number_of_guesses):
    return number_of_guesses + 1

#determine if player guess is fully numeric or not.
def is_number(player_guess):
    try:
        int(player_guess)
        return True
    except TypeError:
        return False
    except ValueError:
        print("That is not a number, champ.")
        return False

#couldn't get this to work.
def guess_list(player_guess):
    return user_guesses.append(player_guess)

#determines if input is less than 1.
def is_less_than_1(player_guess):
    return player_guess < 1

#determine if input is greater than 100.
def is_greater_than_100(player_guess):
    return player_guess > 100

#determines if more than five guesses have been made.
def is_great_than_4_guesses(number_of_guesses):
    return number_of_guesses > 3

def is_close(player_guess, computer_guess): #not sure how to work the math to not return True for all values
    if player_guess - computer_guess <= 5:
        print("Close but no cigar!")
    # elif player_guess - computer_guess >= 5:
    #     print("Close but no cigar!")
    else:
        return None

def is_a_waste(player_guess, user_guesses):
    if player_guess < player_guess in user_guesses: #will not work if user guesses lower than previous guess but higher than comp num 
        print("You're wasting your time with that guess!")

#this is the entire program in a function.
def run_game():
    number_of_guesses = 0
    computer_guess = generate_random_number()
    user_guesses = []
    print(computer_guess)

    while True:
        player_guess = prompt_player()
        if is_number(player_guess):
            player_guess = int(player_guess)
            if player_guess in user_guesses:
                print("You've already guessed that number. Are you taking stupid pills?")
                continue
            elif player_guess == computer_guess:
                print("Congratulations, you win!")
                break
            elif is_less_than_1(player_guess):
                print("That number is not within the specified range, bucko.")
                continue
            elif is_greater_than_100(player_guess):
                print("That number is not within the specified range, bucko.")
                continue
            elif is_great_than_4_guesses(number_of_guesses):
                print("You have exceeded your alloted guesses. You lose.")
                break
            elif player_guess < computer_guess:
                is_close(player_guess, computer_guess)
                print("Your guess is too low.")
                user_guesses.append(player_guess)
                number_of_guesses = increase_guess(number_of_guesses)
                continue
            elif player_guess > computer_guess:
                is_close(player_guess, computer_guess)
                print("Your guess is too high.")
                user_guesses.append(player_guess)
                number_of_guesses = increase_guess(number_of_guesses)
                continue
            else:
                print("Congratulations, you win!")
                break



run_game()
