def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

# Welcome the user
prompt('Welcome to Calculator!')

# Ask user for first number
prompt("What's the first number?")
num_1 = input()

while invalid_number(num_1):
    prompt("Hmm... that does not look like a valid number.")
    num_1 = input()

# Ask user for second number
prompt("What's the second number?")
num_2 = input()

while invalid_number(num_2):
    prompt("Hmm... that does not look like a valid number.")
    num_1 = input()

# Ask user for type of operation to perform: + - x /
prompt('Specify operation type (+, -, *, /): ')
op_type = input()

while op_type not in ["+", "-", "*", "/"]:
    prompt('You must choose +, -, * /')
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
print(f'The results is: {result}')