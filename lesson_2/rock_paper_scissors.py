import random

# Constants
VALID_CHOICES = ['rock', 'paper', 'scissors']

# Define sub-functions
def prompt(message):
    print(f"==> {message}")

def display_winner(my_choice, cpu_choice):
    if ((my_choice == "rock" and cpu_choice == "scissors") or
        (my_choice == "paper" and cpu_choice == "rock") or
        (my_choice == "scissors" and cpu_choice == "paper")):
        prompt("You win!")
    elif ((my_choice == "rock" and cpu_choice == "paper") or
        (my_choice == "paper" and cpu_choice == "scissors") or
        (my_choice == "scissors" and cpu_choice == "rock")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

# Main Code
play_again = True

while play_again:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You chose {choice}, computer chose {computer_choice}")

    display_winner(choice, computer_choice)
    
    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")

    if answer[0] == 'n':
        play_again = False