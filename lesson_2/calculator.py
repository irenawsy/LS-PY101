import json

# Load messages from JSON file
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt("Select language")
user_lang = input()

while True:
    # Welcome the user
    prompt(MESSAGES[user_lang]['welcome'])

    # Ask user for first number
    prompt(MESSAGES[user_lang]['ask_num1'])
    num_1 = input()

    while invalid_number(num_1):
        prompt(MESSAGES[user_lang]['invalid_number'])
        num_1 = input()

    # Ask user for second number
    prompt(MESSAGES[user_lang]['ask_num2'])
    num_2 = input()

    while invalid_number(num_2):
        prompt(MESSAGES[user_lang]['invalid_number'])
        num_1 = input()

    # Ask user for type of operation to perform: + - x /
    prompt(MESSAGES[user_lang]['ask_operation'])
    op_type = input()

    while op_type not in ["+", "-", "*", "/"]:
        prompt(MESSAGES[user_lang]['invalid_operation'])
        op_type = input()

    num_1 = int(num_1)
    num_2 = int(num_2)

    # Calculate
    match op_type:
        case '+':
            result = num_1 + num_2

        case '-':
            result = num_1 - num_2

        case '*':
            result = num_1 * num_2

        case '/':
            result = num_1 / num_2

    # Display result
    prompt(f'The result is {result}')

    prompt(MESSAGES[user_lang]['another_operation'])
    another_one = input()
    
    if (another_one and another_one[0].lower()) != 'y':
        break