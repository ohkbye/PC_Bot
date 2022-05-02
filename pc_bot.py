# PC bot program

# Importing randint from random module
from random import randint

# Creating list of random names
names = ["Karlos", "Marcus", "Jaiden", "Railey", "Ivan", "James", "Joaquin",
         "Einstein", "Mikara", "Sharun", "Tomas", "Matt", "Levi", "Dennis",
         "Ochre", "Carlos", "Navhil", "George", "Billy", "Noel"]
# Creating a dictionary of customer details
customer_details = {}

# Creating variables and lists for the PC component ordering menu
ordered_items = []  # Creating a list for the ordered items
item_costs = []  # Creating a list for the item ordered costs
# Creating a list of component types
component_types = ["CPU", "Storage", "Motherboard", "Power supply", "RAM",
                   "Graphics card", "Operating System", "Case"]
components = [["AMD CPU", "Intel CPU"],
              ["SSD", "HDD"],
              ["ATX Motherboard", "Micro-ATX Motherboard",
               "Mini-ITX Motherboard"],
              ["Fully Modular Power Supply", "Semi Modular Power Supply",
               "Non Modular Power Supply"],
              ["4GB RAM", "8GB RAM", "16GB RAM"],
              ["Nvidia GeForce Graphics Card", "AMD Radeon Graphics Card"],
              ["Windows 10 Operating System", "Windows 8 Operating System"],
              ["Full Tower PC Case", "Mid Tower PC Case",
               "Mini Tower PC Case"]]  # Creating a list of components
# Creating a list of component costs
component_cost = [[199, 239], [149, 99], [69, 59, 49], [79, 69, 59],
                  [29, 39, 49], [269, 249], [29, 19], [49, 39, 29]]

# Creating a list of payment methods
payment_methods = ["Credit Card", "Internet Banking", "Online EFTPOS",
                   "Bank Transfer", "Q Card", "Finance Now"]


# Validates inputs to check if they are blank
# Takes question as parameter
# Returns response in title class if valid
def not_blank(question):
    while True:  # Sets up while loop
        response = input(question)  # Asks for input(string)
# If the response variable is not empty and does not contain
# whitespace continue
        if not response.isspace() and response:
            # If all characters in the response variable only contain
            # letters of the alphabets and number return response
            if all(char.isalpha() or char.isdigit() for char in response):
                return response.title()
# Print error message if response contains anything other than letters
# of the alphabet or numbers
            else:
                print("\nInput must only contain letters and numbers")
# Else if response variable is empty, contains whitespaces print
# error message
        else:
            print("\nInput cannot be blank")


# Validates inputs to check if they are a string
# Takes question as parameter
# Returns response in title class if valid
def check_string(question):
    while True:  # Sets up while loop
        answer = input(question)  # Asks for input(string)
# If answer variable is not empty and does not contain
# whitespace continue
        if not answer.isspace() and answer:
            # Checks each character in the answer variable to see if
            # it is either a letter from the alphabet or space
            if all(char.isalpha() or char.isspace() for char in answer):
                return answer.title()  # Return answer in title class
            else:
                # If answer contains anything besides a letter
                # from the alphabet or spaces print error message
                print("\nInput must only contain letters")
        else:  # Else print error message
            print("\nInput cannot be blank ")


# Validates input to check if they are an integer
# Takes low and high as parameters
# Returns num
def val_int(low, high):
    while True:  # Sets up while loop
        try:  # Try running code
            # Asks for input(integer)
            num = int(input("\nPlease enter a number: "))
# If num variable is greater or equal to low and less or equal to
# high return num
            if num >= low and num <= high:
                return num
            else:  # Else print error message
                print(f"\nYou must enter a number between {low} and {high}")
# If there was an exception within the try code print error message
        except:
            print(f"\nInvalid input\nYou must enter a number \
between {low} and {high}")


# Checks phone number to ensure it is between 7 and 10 digits
# Takes question as parameter
# Returns answer
def check_phone(question):
    while True:  # Sets up while loop
            answer = input(question)  # Asks for input(string)
# If the answer variable contains a number continue
            if answer.isdigit() is True:
                # If length of answer is greater or equal to 7 and less or
                # equal to 10 return answer
                if len(answer) >= 7 and len(answer) <= 10:
                    return answer
                else:  # Else print error message
                    print("\nNZ phone numbers must have between 7 and 10 \
digits")
            else:  # Else print error message
                print("\nPlease enter a number between 7 and 10 digits")


# Welcome message with random name
def welcome():
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message
    Parameters: None
    Returns: None
    '''
# Creating an integer variable, num with a random value from 0 to 9
    num = randint(0, 9)
# Picking a random name from the names list and making it a string
    name_msg = "My name is " + names[num]
    welcome_msg = ["Welcome to Joaquins PC Store", name_msg, "I will be here \
to help you order your PC component"]  # Print welcome message
    print("\n\n\n")
    # Centering text
    for x in range(len(welcome_msg)):
        print(str("***** " + welcome_msg[x] + " *****").center(100, " "))
    print("\n\n\n")


# Menu so that user can choose either delivery or click & collect
def order_type():
    global del_click  # Makes del_click a global variable
    print("\nWould you like your order delivered or click & collected?\n\nFor \
delivery enter 'D'\nFor click & collect enter 'C'")
    while True:  # Loops the code inside until valid input 'C' or 'D'
        # Asks for input(string) and capitalises it
        del_click = input("\nPlease enter a letter: ").upper()
# If del_click variable is equal to 'C' call click & collect function
        if del_click == "C":
            print("\nYou have selected click & collect\n")
            clickcollect_info()
            break
# If del_click variable is equal to 'D' call delivery function
        elif del_click == "D":
            print("\nYou have selected delivery\n")
            delivery_info()
            break
# If del_click does not equal 'C' or 'D' print error message
        else:
            print("The input must be 'C' or 'D'")


# Click & collect information - name and phone number
def clickcollect_info():
    question = "Please enter your name: "  # Sets question variable
# Set customer name to what the check_string function returns
    customer_details['name'] = check_string(question)
    print(customer_details['name'])  # Prints customer name

    question = "Please enter your phone number: "  # Sets question variable
# Sets phone number to what the check_phone function returns
    customer_details['phone'] = check_phone(question)
    print(customer_details['phone'])  # Prints phone number


# Delivery informtion - name, address and phone
def delivery_info():
    question = "Please enter your name: "  # Sets question variable
# Set customer name to what the check_string function returns
    customer_details['name'] = check_string(question)
    print(customer_details['name'])  # Prints customer name

    question = "Please enter your phone number: "  # Sets question variable
# Set phone number to what the check_phone function returns
    customer_details['phone'] = check_phone(question)
    print(customer_details['phone'])  # Prints phone number

    question = "Please enter your house number: "  # Sets question variable
# Set house number to what the not_blank function returns
    customer_details['house'] = not_blank(question)
    print(customer_details['house'])  # Prints house number

    question = "Please enter your street name: "  # Sets question variable
# Set street name to what the check_string function returns
    customer_details['street'] = check_string(question)
    print(customer_details['street'])  # Prints street name

    question = "Please enter your suburb: "  # Sets question variable
# Set suburb to what the check_string function returns
    customer_details['suburb'] = check_string(question)
    print(customer_details['suburb'])  # Prints suburb


# Choose type of PC component
def component_selection():
    global component_selected  # Makes component_selected a global variable
    # Prints out list of types of PC components
    print("\nHere are the available types of PC components:")
# Repeats code for the length of component_types list
    for x in range(len(component_types)):
        # Prints out PC component type
        print(str(x + 1) + ")", component_types[x])
    print("\nWhat type of PC component would you like to order?\nEnter a \
number from the list above which matches the PC component you would like.")
    LOW = 1  # Sets LOW variable to 1
    HIGH = 8  # Sets HIGH variable to 8
# Set component_selected variable to what the val_int function returns
    component_selected = val_int(LOW, HIGH)
    print("\nYou have selected " + component_types[component_selected - 1])


# PC component ordering menu
def item_selection():
    global selected_item  # Makes selected_item a global variable
    global selected_item_cost  # Makes selected_item_cost a global variable
    # Print available items of selected component
    print("\nHere are the available types of",
          component_types[component_selected - 1])
# Repeats code x amount of times
    for x in range(len(components[component_selected - 1])):
        print(str(x + 1) + ")", components[component_selected - 1][x], "| $" +
              str(component_cost[component_selected - 1][x]))
# Ask user what type of (PC component) they would like
    print("\nWhat type of", component_types[component_selected - 1],
          "would you like?")
    LOW = 1  # Set LOW variable to 1
# Sets HIGH variable to length of components list
    HIGH = len(components[component_selected - 1])
# Sets num_input to what the val_int function returns
    num_input = val_int(LOW, HIGH)
# Sets selected_item variable to the item the user has selected
    selected_item = components[component_selected - 1][num_input - 1]
# Sets selected_item_cost to the cost of the item the user has selected
    selected_item_cost = component_cost[component_selected - 1][num_input - 1]
    print("\nYou have selected the", selected_item)


# Select quantity of items
def quantity():
    global total_cost  # Makes total_cost a global variable
# Asks user the quantity of selected item they would like
    print("How many " + selected_item + "s would you like?\n(You can only \
order up to 5x " + selected_item + "s)")
    LOW = 1  # Sets LOW variable to 1
    HIGH = 5  # Sets HIGH variable to 5
# Sets num_quantity to what val_int function returns
    num_quantity = val_int(LOW, HIGH)
# Append the selected_item and the quantity into the ordered_items list
    ordered_items.append(str(num_quantity) + "x " + selected_item)
# Append the cost of the selected item into the item_costs list
    item_costs.append(selected_item_cost * num_quantity)
# Set total_cost variable to the sum of all integers in item_costs list
    total_cost = sum(item_costs)


# Display items selected
def display_selection():
    # Prints out the items that the user has currently selected
    print("\nYou have ordered the following items: ")
    for x in range(len(ordered_items)):  # Repeats code x amount of times
        print(str(x + 1) + ". " + ordered_items[x] + " | Unit cost = $\
" + str(round(item_costs[x] / int(ordered_items[x][0]))) + " | Total = $" +
              str(item_costs[x]))
    print("\nSubtotal: $" + str(sum(item_costs)))  # Print subtotal


# Option to order another item or remove a selected item or proceed to checkout
def new_checkout():
    # Asks user if they want to order another component, remove an item or
    # proceed to checkout
    print("\nWould you like to order another PC component, remove an item that \
has been ordered or proceed to checkout?\n\nTo order another item enter \
'N'\nTo remove an item that has been selected enter 'R'\nTo proceed to \
checkout enter 'P'")
    while True:  # Sets up while loop
        # # Asks for input(string) capitalises it
        answer = input("\nPlease enter a letter: ").upper()
        # If answer variable is equal to 'N' call pc_menu function
        if answer == "N":
            print("\nOrdering another PC component...")
            pc_menu()
            break
        elif answer == "R":  # If answer variable is equal to 'R' continue
            print("\nRemoving an item...")
# If the length of ordered_items is equal to 1 print error message
            if len(ordered_items) == 1:
                print("\nYou have only ordered one item\nThere is no item that \
you can remove")
                new_checkout()
                break
# Else call display_selection function and then call return_item function
            else:
                display_selection()
                remove_item()
                break
# If answer variable is equal to 'P' proceed to checkout by breaking out
# of the loop
        elif answer == "P":
            print("\nProceeding to checkout...")
            break
        else:  # If answer was not equal to 'N', 'R', 'P' print error message
            print("The input must be 'N', 'R' or 'P'")


# Removing an order
def remove_item():
    global total_cost  # Makes total_cost a global variable
    print("\nWhich item would you like removed?")
    print("Enter a number from the list above which matches the item you would \
like removed.")
    LOW = 1  # Sets LOW variable to 1
    # Sets HIGH variable to length of ordered_items list
    HIGH = len(ordered_items)
    answer = val_int(LOW, HIGH)  # Set answer to what val_int function returns
    print("\nRemoving", ordered_items[answer - 1])
# Delete the item in the ordered_items list with the index of the answer - 1
    del ordered_items[answer - 1]
# Delete the cost in the item_costs list with the index of the answer minus 1
    del item_costs[answer - 1]
# Set total_cost variable to the sum of all integers in item_costs list
    total_cost = sum(item_costs)
    display_selection()  # Call display_selection function
    new_checkout()  # Call new_checkout function


# Checkout - Payment method
def checkout():
    global total_cost  # Makes total_cost a global variable
    global payment_method  # Makes payment_method a global variable
    # Print details
    print("\nYour details: ")
    if del_click == "D":  # If del_click variable is equal to 'D' continue
        total_cost += 5  # Adds 5 to the total_cost variable
        print("Your order is for delivery\nThere is a $5 delivery fee")
        # Prints customer details
        print(f"\nCustomer Name: {customer_details['name']}\nCustomer Phone: \
{customer_details['phone']}\nCustomer Address: {customer_details['house']} \
{customer_details['street']}, {customer_details['suburb']}")
        display_selection()  # Call display_selection function
# Print total order cost
        print("Delivery: $5\nTotal Order Cost: $" + str(total_cost))
    elif del_click == "C":  # If del_click variable is equal to 'C' continue
        print("Your order is for click & collect")
        # Print customer details
        print(f"\nCustomer Name: {customer_details['name']}\nCustomer Phone: \
{customer_details['phone']}")
        display_selection()  # Call display_Selection function
# Print total order cost
        print("Click & Collect: FREE\nTotal Order Cost: $" + str(total_cost))
    # Print available payment methods
    print("\nHow would you like to pay?\n\nHere are the available payment \
methods:")
    for x in range(len(payment_methods)):  # Repeats code x amount of times
        print(str(x + 1) + ")", payment_methods[x])
    print("\nSelect a payment method")
    LOW = 1  # Set LOW variable to 1
    HIGH = 6  # Set HIGH variable to 6
# Set answer variable to what val_int function returns
    answer = val_int(LOW, HIGH)
    print("\nYou have selected", payment_methods[answer - 1])
    payment_method = payment_methods[answer - 1]  # Sets payment_method


# Confirm order
def order_confirmation():
    print("\nTotal Order Cost: $" + str(total_cost) + "\nPayment Method:\
", payment_method)  # Print total order cost and payment method
    print("\nWould you like to confirm the order?\nTo confirm the order enter \
'Y'\nTo cancel the order enter 'N'")  # Asks user to confirm order
    while True:  # Sets up while loop
        # Asks for input(string) and capitalises it
        answer = input("\nPlease enter a letter: ").upper()
        if answer == "Y":  # If answer variable is equal to 'Y' confirm order
            print("\nOrder Confirmed\nYour order has been placed and will be \
shipped tomorrow")
# If del_click variable is equal to 'D' print the order will arrive
# within 2-3 working days
            if del_click == "D":
                print("Your order will arrive within 2-3 working days")
            break
        elif answer == "N":  # If answer variable is equal to 'N' cancel order
            print("\nYour order has been cancelled")
            break
        else:  # Else if input is not equal to 'Y' or 'N' print error message
            print("The input must be 'Y' or 'N'")


# Option to restart the bot or to exit
def new_exit():
    print("\nWould you like to start another order or exit the bot\nTo start \
another order enter 'Y'\nTo exit the \
bot enter 'N'")  # Asks user if they want to start another order or exit bot
    while True:  # Sets up while loop
        # Asks for input(string) and capitalises it
        answer = input("\nPlease enter a letter: ").upper()
        if answer == "Y":  # If answer is equal to 'Y' start another order
            print("\nStarting another order...")
            customer_details.clear()  # Clear customer_details dictionary
            ordered_items.clear()  # Clear ordered_items list
            item_costs.clear()  # Clear item_costs list
            main()  # Call main function
            break
        elif answer == "N":  # If answer is equal to 'N' exit bot
            print("\nExiting the bot...")
            break
        else:  # Else if answer was not equal to 'Y' or 'N' print error message
            print("The input must be 'Y' or 'N'")


# PC Menu function
def pc_menu():
    component_selection()  # Calls component_selection function
    item_selection()  # Calls item_selection function
    quantity()  # Calls quantity function
    display_selection()  # Calls display_selection function
    new_checkout()  # Calls new_checkout function


# Main function
def main():
    '''
    Purpose: To run all functions
    a welcome message
    Parameters: None
    Returns: None
    '''
    welcome()  # Calls welcome function
    order_type()  # Calls order_type function
    pc_menu()  # Calls pc_menu function
    checkout()  # Calls checkout function
    order_confirmation()  # Calls order_confirmation function
    new_exit()  # Calls new_exit function

main()  # Calls main function and starts the program
