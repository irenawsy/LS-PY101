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

while True:
    # Welcome the user
    prompt(MESSAGES['welcome'])

    # Ask user for first number
    prompt(MESSAGES['ask_num1'])
    num_1 = input()

    while invalid_number(num_1):
        prompt(MESSAGES['invalid_number'])
        num_1 = input()

    # Ask user for second number
    prompt(MESSAGES['ask_num2'])
    num_2 = input()

    while invalid_number(num_2):
        prompt(MESSAGES['invalid_number'])
        num_1 = input()

    # Ask user for type of operation to perform: + - x /
    prompt(MESSAGES['ask_operation'])
    op_type = input()

    while op_type not in ["+", "-", "*", "/"]:
        prompt(MESSAGES['invalid_operation'])
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

    prompt(MESSAGES['another_operation'])
    another_one = input()
    
    if (another_one and another_one[0].lower()) != 'y':
        break