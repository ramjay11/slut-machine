import random

# Global constants
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    """
        Checks for winning combinations and calculates winnings.
        Parameters:
            columns (list of lists): The matrix representing the slut machine.
            lines (int): Number of lines to bet on.
            bet (int): Bet amount per line.
            values (dict): Dictionary containing symbol values.
        Returns:
            tuple: A tuple containing total winnings and the list of winning lines.
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][lines]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slut_machine_spin(rows, cols, symbols):
    """
        Generates a random spin of the slut machine.
        Parameters:
            rows (int): Number of rows in the slut machine.
            cols (int): Number of columns in the slut machine.
            symbols (dict): Dictionary containing symbol counts.
        Returns:
            list of lists: A matrix representing the slut machine spin.
    """
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slut_machine(columns):
    """
        Prints the slut machine spin.
        Parameters:
            columns (list of lists): The matrix representing the slot machine.
    """
    for row in range(len(columns[0])):  # Iterate over rows
        # print value
        # for i, column in enumerate(columns[row]):
        #     if i != len(columns) -1:
        #         print(column[row], end=" | ")
        #     else:
        #         print(column[row], end="")
        # for col in range(len(columns[row])):
        # print(columns[col][row], end=" ")
        # print(column[row], end=" ")
        for column in columns:  # Iterate over columns
            print(column[row], end=" ")  # Print symbol
            print("|", end=" ")
        print()  # Move to the next line after printing a row


def deposit():
    """
        Prompts the user to deposit an amount.
        Returns:
            int: The deposited amount.
    """
    while True:
        amount = input("What would you like to deposit? P")
        # Check if valid number is entered
        if amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount


def get_number_of_lines():
    """
        Prompts the user to enter the number of lines to bet on.
        Returns:
            int: The number of lines to bet on.
    """
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        # Check if valid number is entered
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number")
    return lines


def get_bet():
    """
       Prompts the user to enter the bet amount per line.
       Returns:
           int: The bet amount per line.
    """
    while True:
        amount = input("How much is your bet on each line? P")
        #
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between P{MIN_BET} - P{MAX_BET}.")
        else:
            print("Please enter a number")
    return amount


def spin(balance):
    """
        Initiates a spin of the slut machine.
        Parameters:
            balance (int): Current balance of the player.
        Returns:
            int: Net winnings from the spin.
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough balance to bet that amount, your current balance is: P{balance}")
        else:
            break
    print(f"You are betting P{bet} on {lines} lines. Total bet is equal to: P{total_bet}")
    # print(balance, lines)

    sluts = get_slut_machine_spin(ROWS, COLS, symbol_count)
    print_slut_machine(sluts)
    winnings, winning_lines = check_winnings(sluts, lines, bet, symbol_value)
    print(f"You won P{winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is P{balance}")
        spin_input = input("Press enter to play (q to quit).")
        if spin_input == 'q':
            break
        balance += spin(balance)
        #  net_winnings, update_balance = spin(balance)  # Call the function spin with balance as a parameter
        #  balance = update_balance
    print(f"You left with P{balance}")


main()
