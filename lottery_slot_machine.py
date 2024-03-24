# this is a slot machine project

# this module is used to generate random numbers for the slot machine
import random

# the global variables which are common to the whole of 
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 10

#number of rows and columns in the slot machine
ROWS = 3
COLS = 3

symbols = {
    'w' : 6,
    'x' : 2,
    'y' : 4,
    'z' : 5
}

#this function is to generate symbols for each column based on the dictionary "symbols"
def slotmachine_spin(rows, cols, symbols):
    all_symbols = []
    #add all the symbols to the list "symbols"
    for symbols, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        #make a copy of all symbols 
        current_symbols = all_symbols[:]
        #generating row symbols
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

#printing the columns in transposed order
def display_slot_machine_spin(columns):
    for row in range(len(columns[0]))

# this function takes user input for the amount to be deposited in the slot machine
def deposit():
    while True:
    # to check if the entered value is a positive number
        amount = input("Enter amount to deposit: $")
        if amount.isdigit():    
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("Amount must be greater than zero!")
        else:
            print("Please enter a valid amount.")
         # the loop continues until the user enters a positive integer
    return amount

# this function takes user input for the number of lines to bet on
def get_number_of_lines():
    # checks if the number of lines is a positive number and in range
    while True:
        lines = input("Enter number of lines to bet on\nAvailabel lines 1 - " + str(MAX_LINES) + " : ")
        if lines.isdigit():
            lines = int(lines)
            if (MAX_LINES >= lines >= 1):
                break
            else:
                print("Please enter the lines in range!")
        else:
            print("Please enter a valid number")
    # the loop continues until the user enters a positive integer in range
    return lines

#function to get the betting amount from user for each line
def get_bet_amount(cur_amt):
    # checks if the entered amount can be put to bet
    while True:
        bet_amt = input("Enter the bet amount on each line: $")
        if bet_amt.isdigit():
            bet_amt = int(bet_amt)
            if ((MIN_BET <= bet_amt <= MAX_BET) and bet_amt <= cur_amt) :
                break
            else:
                if cur_amt < MAX_BET:
                    cur_max = cur_amt
                else:
                    cur_max_max = MAX_BET
                print(f"Bet amount must be between ${MIN_BET} - ${cur_max}.")
        else:
            print("Enter a valid bet amount")
        # runs until user enters a valid bet amount
    return bet_amt

# this function displays the current balance of the player
def display_cur_balance(cur_amt):
    print("Your balance amount is $" + str(cur_amt))



# the main function is called slot_machine
def slot_machine():
    current_amount = deposit()
    lines_on_bet = get_number_of_lines()
    bet_amount = get_bet_amount(current_amount)
    display_cur_balance(current_amount)



# running the main function 
slot_machine()  