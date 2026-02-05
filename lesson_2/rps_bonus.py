import random
import os

# Constants
VALID_CHOICES = {'r' : 'rock',
                 'p' : 'paper',
                 'c' : 'scissors',
                 'l' : 'lizard',
                 'k' : 'spock'}

WINNING_COMBOS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors'],
}

USER_WIN = "user_win"
CPU_WIN = "cpu_win"
TIE = "tie"

# Define sub-functions
def prompt(message):
    print(f"==> {message}")

def get_user_choice():
    choice_list = []

    for key, value in VALID_CHOICES.items():
        choice_list.append(f"{key} - {value}")

    prompt(f'Choose one: {", ".join(choice_list)}')
    input_choice = input().strip().lower()

    while input_choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        input_choice = input().strip().lower()

    return VALID_CHOICES[input_choice]

def player_wins(choice_player, choice_cpu):
    return choice_cpu in WINNING_COMBOS[choice_player]

def computer_wins(choice_player, choice_cpu):
    return choice_player in WINNING_COMBOS[choice_cpu]

def determine_winner(choice_player, choice_cpu):
    if player_wins(choice_player, choice_cpu):
        return USER_WIN
    elif computer_wins(choice_player, choice_cpu):
        return CPU_WIN
    else:
        return TIE

def display_winner(my_choice, cpu_choice):
    who_won = determine_winner(my_choice, cpu_choice)

    if who_won == USER_WIN:
        prompt('You won!')
    elif who_won == CPU_WIN:
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

def display_grand_winner(user_result, cpu_result):
    print('\n')
    prompt(f'You won {user_result} time(s), CPU won {cpu_result} time(s).')
    if user_result > cpu_result:
        prompt("You are the GRAND WINNER!")
    elif user_result < cpu_result:
        prompt("CPU is the GRAND WINNER")
    else:
        prompt("It's a tie!")

    print('\n')

# Main Code
while True:
    prompt('Welcome to Rock Paper Scissors Lizard Spock!')
    print('\n')
    prompt('RULES')
    prompt('Rock beats Scissors and Lizard')
    prompt('Paper beats Rock and Spock')
    prompt('Scissors beats Lizard and Paper')
    prompt('Spock beats Rock and Scissors')
    prompt('Lizard beats Paper and Spock')
    print('\n')
    prompt("Let's play best-of-5!")

    round_num = 1
    user_win_count = 0
    cpu_win_count = 0

    while round_num <= 5:
        print('\n')
        prompt(f'ROUND {round_num}')
        user_choice = get_user_choice()

        computer_choice = random.choice(list(VALID_CHOICES.values()))

        prompt(f"You chose {user_choice}, computer chose {computer_choice}")

        round_result = determine_winner(user_choice, computer_choice)
        display_winner(user_choice, computer_choice)

        if round_result == USER_WIN:
            user_win_count += 1
        elif round_result == CPU_WIN:
            cpu_win_count += 1

        round_num += 1

    display_grand_winner(user_win_count, cpu_win_count)

    while True:
        prompt("Do you want to play another best-of-5 match? (y/n)")
        answer = input().strip().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break

        else:
            prompt("That's not a valid choice")

    if answer[0] == 'n':
        prompt('Thanks for playing!')
        break

    os.system('clear')
