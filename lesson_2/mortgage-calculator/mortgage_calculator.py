"""
Mortgage calculator that takes:
- Loan Amount in dollar and cents format
- Annual Percentage Rate (APR) in decimal format
- Duration in number of years

Calculates and outputs user's monthly payment amount.
"""

# SUB-FUNCTIONS
def prompt(prompt_message):
    """
    Adds "==>" before prompt message to enhance 
    readability of instructions for user
    """
    print(f"==> {prompt_message}")

def get_loan():
    """
    Gets and validate user input for Loan Amount
    """
    while True:
        prompt("What is your loan amount?")
        prompt("(Enter in dollar and cents format, e.g. 123.45, or 700.20)")
        prompt("(Do NOT include dollar signs)")
        loan = input().strip()
        try:
            float(loan)
        except ValueError:
            prompt('Error: Loan must be in numerical format')
        else:
            return float(loan)

def get_apr():
    """
    Get and validate user input for Annual Percentage Rate (APR)
    """
    while True:
        prompt("What is the Annual Percentage Rate (APR)?")
        prompt("Enter in decimal format (0.05 for 5%)")
        input_apr = input().strip()
        try:
            float(input_apr)
        except ValueError:
            prompt('Error: Loan must be in numerical format')
        else:
            return float(input_apr)

def get_duration():
    """
    Get and validate user input for loan duration in years.
    """
    while True:
        prompt("How long is the loan in years?")
        input_duration_in_years = input().strip()
        try:
            float(input_duration_in_years)
        except ValueError:
            prompt('Error: Loan must be in numerical format')
        else:
            return float(input_duration_in_years)

# Get loan amount
loan_amount = get_loan()

# Get the Annual Percentage Rate (APR)
apr = get_apr()

# Get the loan duartion
loan_duration_in_years = get_duration()

# Calculate loan duration in months
loan_duration_in_months = loan_duration_in_years * 12
loan_duration_in_months = round(loan_duration_in_months, 2)

# Calculate Monthly Interst Rate (MIR)
monthly_interest_rate = apr / 12

# Calculate monthly payment
if monthly_interest_rate == 0:
    monthly_payment = loan_amount / loan_duration_in_months
else:
    monthly_payment = loan_amount \
        * (monthly_interest_rate \
           / (1 - (1 + monthly_interest_rate) ** (-loan_duration_in_months)))

monthly_payment = round(monthly_payment, 2)

# Print payment as dollar and cents amount
prompt(f"Your monthly payment is ${monthly_payment} for {loan_duration_in_months} months.")
