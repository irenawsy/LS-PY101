import json

# SUB-FUNCTIONS
def prompt(prompt_message):
    print(f"==> {prompt_message}")

def message(msg_key, lang = 'en'):
    return MESSAGES[lang][msg_key]

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

# PROGRAM CODE
# Load messages from JSON file
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Supported languages
supported_languages = ["en", "es"]

# Ask user for preferred language
prompt("Select language (en - English, es - Español)")
user_lang = input()

while user_lang not in supported_languages:
    prompt(message('invalid_language'))
    user_lang = input()

# Actual Calculator
while True:
    # Welcome the user
    prompt(message('welcome', user_lang))

    # Ask user for first number
    prompt(message('ask_num1', user_lang))
    num_1 = input()

    while invalid_number(num_1):
        prompt(message('invalid_number', user_lang))
        num_1 = input()

    # Ask user for second number
    prompt(message('ask_num2', user_lang))
    num_2 = input()

    while invalid_number(num_2):
        prompt(message('invalid_number', user_lang))
        num_2 = input()

    # Ask user for type of operation to perform: + - x /
    prompt(message('ask_operation', user_lang))
    op_type = input()

    while op_type not in ["+", "-", "*", "/"]:
        prompt(message('invalid_operation', user_lang))
        op_type = input()

    # Convert input into appropriate data type
    num_1 = float(num_1)
    num_2 = float(num_2)

    # Calculate
    match op_type:
        case '+':
            result = num_1 + num_2

        case '-':
            result = num_1 - num_2

        case '*':
            result = num_1 * num_2

        case '/':
            try:
                result = num_1 / num_2
            except ZeroDivisionError:
                prompt(message('division_by_zero', user_lang))
                result = "Calculation Error"

    result = round(result, 2)

    # Display result
    prompt(f'{num_1} {op_type} {num_2}  = {result}')

    # Ask if user wants to do another calculation
    prompt(message('another_operation', user_lang))
    another_one = input().strip()

    # Terminate if user enters anything other than 'yes' or 'y'
    # If no input, assume "no"
    if (another_one and another_one[0].lower()) != \
    MESSAGES[user_lang]['yes'][0]:
        break