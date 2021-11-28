# -------------------------------------------------- #
# Title: Assignment07
# Description: This script demonstrates how Pickling and Structured error
#              handling work via a shopping cart price calculator program.
# ChangeLog (Who,When,What):
# Cli,11-26-2021,Created Script
# -------------------------------------------------- #

import pickle

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
item_str = ''  # Captures the user's item data
cost_flt = 0  # Captures the user's item's cost
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ''  # captures the user's option selection
file_name_str = 'ShoppingCart.dat'  # The name of the data file

# Processing ---------------------------------------------------------------- #
class Processor:
    @staticmethod
    def add_data_to_list(item, cost, list_of_rows):
        """ Creates a new row with inputted item and its cost and adds it to a list of dictionary rows

        :param item: (string) with item to input into list/table of data:
        :param cost: (string) with cost of the item:
        :param list_of_rows: (list) of dictionary rows:
        :return: (list) of dictionary rows with newly added row of item & cost
        """
        if item != '' and cost != 0:
            row = {'Item': item, 'Cost': cost}
            list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def total_items(list_of_rows):
        """ Calculates the total number of items in the list/table of data

        :param list_of_rows: (list) containing table of data
        :return: (float) with the number of items in the table
        """
        num_of_items = len(list_of_rows)
        return num_of_items

    @staticmethod
    def total_cost(list_of_rows):
        """ Calculates the total cost of the items in the table of data

        :param list_of_rows: (list) of dictionary rows
        :return: (float) with total cost of shopping list
        """
        total_cost = 0
        # print(list_of_rows)  # testing table of dictionary rows
        for row in list_of_rows:
            total_cost += row['Cost']
        return total_cost

    @staticmethod
    def pickling_list(file_name, list_of_rows):
        """ Pickles the list of data into a new binary file

        :param file_name: (string) with name of the binary file
        :param list_of_rows: (list) with list of data
        :return: nothing
        """
        with open(file_name, 'wb') as file:
            pickle.dump(list_of_rows, file)

    @staticmethod
    def unpickling_list(file_name):
        """ Unpickles the list of data from a binary file

        :param file_name: (string) with name of the binary file
        :return: list of data
        """
        with open(file_name, 'rb') as file:
            shopping_list = pickle.load(file)
        return shopping_list

# Presentation -------------------------------------------------------------- #
class IO:
    @staticmethod
    def print_menu_options():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
          Menu of Options
          0) Exit Program
          1) Add a new item and its cost
          2) See total cost & save receipt
          ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: (string) with user's menu selection
        """
        choice = str(input("Which option would you like to perform? [0 to 2] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print()
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_shopping_cart_items(item='', cost=0):
        """ User inputs an item and its cost into a list/table of data. Error handling controls the
        type of inputs allowed

        :param item: (string) with the name of the item
        :param cost: (float) with the cost of the item
        :return: (tuple) with item and its cost
        """
        try:
            item = str(input('\nEnter the name of the item in your shopping cart: ')).lower().strip()
            if item.isnumeric():
                raise Exception('Items must be in letters')
            elif len(item) == 0:
                raise Exception('Blank entries are not allowed.')
            cost = float(input('Enter its cost: '))
        except ValueError as e:
            print("Entry error")
            print('Cost must be in numbers')
            # print("Built-In Python error info: ")
            # print(e, e.__doc__, type(e), sep='\n')  # for testing: evaluating errors
        except Exception as e:
            print("Entry error")
            print(e)
            # print("Built-In Python error info: ")
            # print(e, e.__doc__, type(e), sep='\n')  # for testing: evaluating errors
        return item, cost

    @staticmethod
    def print_current_items_in_list(list_of_rows):
        """ Shows the current items in the list of dictionary rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* Receipt: *******")
        for row in list_of_rows:
            print(row["Item"] + " (" + str(row["Cost"]) + ")")
        print("*************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        print()  # Add an extra line for looks
        return str(input(message)).strip().lower()

# Main Body of Script  ------------------------------------------------------ #
print('This is the Shopping Cart Price Calculator Program')

while True:
    IO.print_current_items_in_list(list_of_rows=table_lst)  # Show current data
    IO.print_menu_options()  # Display a menu of choices to the user
    choice_str = IO.input_menu_choice()  # Get menu option

    if choice_str == '1':  # User input data into list/table & program demos error handling
        item_str, cost_flt = IO.input_shopping_cart_items()
        Processor.add_data_to_list(item=item_str, cost=cost_flt, list_of_rows=table_lst)
        choice_str = IO.input_yes_no_choice('Do you want to enter more entries? [y/n] ')
        while choice_str.lower() == 'y':  # when yes is selected, continuous inputs are allowed
            item_str, cost_flt = IO.input_shopping_cart_items()
            Processor.add_data_to_list(item=item_str, cost=cost_flt, list_of_rows=table_lst)
            choice_str = IO.input_yes_no_choice('Do you want to enter more entries? [y/n] ')
        else:
            continue

    elif choice_str == '2':
        print('Total number of items in the cart is:', Processor.total_items(list_of_rows=table_lst))
        print('Total cost in the cart:', Processor.total_cost(list_of_rows=table_lst))
        # Demo of pickling data
        IO.input_press_to_continue('Saving receipt...')
        Processor.pickling_list(file_name=file_name_str, list_of_rows=table_lst)
        IO.input_press_to_continue('Receipt saved!')
        # Demo of unpickling data
        IO.input_press_to_continue('Retrieving receipt...')
        table_lst = Processor.unpickling_list(file_name=file_name_str)

    elif choice_str == '0':  # Exits Program
        break

    else:
        IO.input_press_to_continue('Please select only 0, 1 or 2!')
