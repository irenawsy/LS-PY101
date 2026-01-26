print('Welcome to Calculator!')

# Ask user for first number
num_1 = input('First number: ')

# Ask user for second number
num_2 = input('Second number: ')

# Ask user for type of operation to perform: + - x /
op_type = input('Specify operation type (+, -, x, /): ')

num_1 = int(num_1)
num_2 = int(num_2)

# Calculate
match op_type:
    case '+':
        result = num_1 + num_2

    case '-':
        result = num_1 - num_2

    case 'x':
        result = num_1 * num_2

    case '/':
        result = num_1 / num_2

# Display result
print(f'The results is: {result}')