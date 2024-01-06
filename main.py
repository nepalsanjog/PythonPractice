import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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

def check_winning(columns, lines, bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][lines]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += values[symbol] * bet
            winning_lines.append(line + 1)

    return winning, winning_lines

#def get_slot_machine_spin(rows, cols, symbols):


#def print_slot_machine(columns):    




#this function will get the deposite amount
def deposit():
    while True:

        #store the value in amount
        amount = input("what would you like to deposit? $")

        #check if the deposite amount is a number
        if amount.isdigit():

            #convert to int
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print ("please enter a number.")
    return amount

#this gets the number of lines they want to bet on, max is 3
def get_num_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (-1" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int (lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else: 
            print("Please enter a number.")

    return lines
    
def get_bet():
    while True:

        #store user input on amount
        amount = input("what amount would you like to bet?")

        #check if input is a number
        if amount.isdigit():
            #if it is convert it to int
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print ("enetr a number")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"you do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winning, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"you won ${winning}.")
    print(f"you won on lines: ", * winning_lines)
    return winning - total_bet

def main():
    balance = deposit()
    lines = get_num_of_lines()
    bet = get_bet()
    total_bet = bet * lines

    print(f"you are betting ${bet} on {lines} lines. totl bet is {total_bet}.")


    print(balance, lines)