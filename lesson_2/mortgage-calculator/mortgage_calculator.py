"""
Mortgage calculator that takes:
- Loan Amount in dollar and cents format
- Annual Percentage Rate (APR) in decimal format
- Duration in number of years

Calculates and outputs user's monthly payment amount.
"""

# CONSTANTS
MONTHS_IN_YEAR = 12

# SUB-FUNCTIONS
def prompt(prompt_message):
    """
    Adds "==>" before prompt message to enhance readability of instructions for user
    """
    print(f"==> {prompt_message}")

def get_valid_input(zero_check = False):
    """
    Get and validate user's input.
    Only positive numbers are allowed.
    Can toggle for zero-check
    :param zero_check: False - no zero-check, True - do zero-check
    """
    while True:
        user_input = input().strip()
        try:
            user_input = float(user_input)
            if user_input < 0:
                prompt('Error: Input must be positive')
                continue
            if zero_check:
                if user_input == 0:
                    prompt('Error: Input must not be Zero')
                    continue
        except ValueError:
            prompt('Error: Input must be in numerical format')
        else:
            return user_input

def display_results(loan_amt, annual_interest_rate, duration_years, duration_months, payment):
    """
    Display results
    """
    print('\n')
    prompt('RESULTS')
    prompt(f'Loan Amount: ${loan_amt:.2f}')
    prompt(f'APR: {annual_interest_rate * 100}%')
    prompt(f'Loan Duration: {duration_years} years ' +
           f'({duration_months} months)')
    prompt(f'Your monthly payment is ${payment:.2f} for ' +
           f'{duration_months} months.')
    print('\n')

# Mortgage Calculator
while True:
    print('\n')

    # Get loan amount
    prompt("What is your loan amount?")
    prompt("(Enter in dollar and cents format, e.g. 123.45, or 700.20)")
    prompt("(Do NOT include dollar signs)")
    loan_amount = get_valid_input(True)

    # Get the Annual Percentage Rate (APR)
    prompt("What is the Annual Percentage Rate (APR)?")
    prompt("Enter in decimal format (0.05 for 5%)")
    apr = get_valid_input()

    # Get the loan duration
    prompt("How long is the loan in years?")
    loan_duration_in_years = get_valid_input(True)

    # Calculate loan duration in months
    loan_duration_in_months = loan_duration_in_years * MONTHS_IN_YEAR
    loan_duration_in_months = round(loan_duration_in_months, 2)

    # Calculate Monthly Interst Rate (MIR)
    monthly_interest_rate = apr / MONTHS_IN_YEAR

    # Calculate monthly payment
    if monthly_interest_rate == 0:
        monthly_payment = loan_amount / loan_duration_in_months
    else:
        monthly_payment = (loan_amount *
                           (monthly_interest_rate /
                            (1 - (1 + monthly_interest_rate) ** (-loan_duration_in_months))))

    # Print payment as dollar and cents amount
    display_results(loan_amount,
                    apr,
                    loan_duration_in_years,
                    loan_duration_in_months,
                    monthly_payment)

    # Ask if user wants to do another calculation
    prompt('Another calculation? (y/n)')
    another_one = input().strip()

    # Terminate if user enters anything other than 'yes' or 'y'
    # If no input, assume "no"
    if (another_one and another_one[0].lower()) != "y":
        break
