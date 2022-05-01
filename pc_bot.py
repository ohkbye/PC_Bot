# PC bot program
# 6/4/2022
# Bugs - Phone number input allows letters
#      - Name input allows numbers


# Importing randint from random module
from random import randint

# List of random names
names = ["Karlos", "Marcus", "Jaiden", "Railey", "Ivan", "James", "Joaquin",
         "Einstein", "Mikara", "Sharun", "Tomas", "Matt", "Levi", "Dennis",
         "Ochre", "Carlos", "Navhil", "George", "Billy", "Noel"]
# Customer details dictionary
customer_details = {}

# Creating variables and lists for the PC component ordering menu
ordered_items = []
item_costs = []
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
               "Mini Tower PC Case"]]
component_cost = [[199, 239], [149, 99], [69, 59, 49], [79, 69, 59],
                  [29, 39, 49], [269, 249], [29, 19], [49, 39, 29]]

# Payment methods
payment_methods = ["Credit Card", "Internet Banking", "Online EFTPOS",
                   "Bank Transfer", "Q Card", "Finance Now"]


# Validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("\nThis cannot be blank")


# Validates strings
def check_string(question):
    while True:
        answer = input(question)
        x = answer.isalpha()
        if x == False:
            print("\nInput must only contain letters")
        else:
            return answer.title()


# Validates input to check if they are an integer
def val_int(low, high):
    while True:
        try:
            num = int(input("\nPlease enter a number: "))
            if num >= low and num <= high:
                return num
            else:
                print(f"\nYou must enter a number between {low} and {high}")
        except:
            print(f"\nInvalid input\nYou must enter a number \
between {low} and {high}")


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
    # Print welcome message
    welcome_msg = ["Welcome to Joaquins PC Store", name_msg, "I will be here \
to help you order your PC component"]
    print("\n\n\n")
    # Center text
    for x in range(len(welcome_msg)):
        print(str("***** " + welcome_msg[x] + " *****").center(100, " "))
    print("\n\n\n")


# Menu so that user can choose either delivery or click & collect
def order_type():
    global del_click
    print("\nWould you like your order delivered or click & collected?\n\nFor \
delivery enter 'D'\nFor click & collect enter 'C'")
    # Loops the code inside until user enters a valid input 'C' or 'D'
    while True:
        # Asks for letter and capitalises it
        del_click = input("\nPlease enter a letter: ").upper()
        if del_click == "C":
            print("\nYou have selected click & collect\n")
            clickcollect_info()
            break
        elif del_click == "D":
            print("\nYou have selected delivery\n")
            delivery_info()
            break
        else:
            print("The input must be 'C' or 'D'")


# Click & collect information - name and phone number
def clickcollect_info():
    question = "Please enter your name: "
    customer_details['name'] = check_string(question)
    print(customer_details['name'])

    question = "Please enter your phone number: "
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])


# Delivery informtion - name, address and phone
def delivery_info():
    question = "Please enter your name: "
    customer_details['name'] = check_string(question)
    print(customer_details['name'])

    question = "Please enter your phone number: "
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])

    question = "Please enter your house number: "
    customer_details['house'] = not_blank(question)
    print(customer_details['house'])

    question = "Please enter your street name: "
    customer_details['street'] = check_string(question)
    print(customer_details['street'])

    question = "Please enter your suburb: "
    customer_details['suburb'] = check_string(question)
    print(customer_details['suburb'])


# Choose type of PC component
def component_selection():
    global component_selected
    print("\nHere are the available types of PC components:")
    for x in range(len(component_types)):
        print(str(x + 1) + ")", component_types[x])
    print("\nWhat type of PC component would you like to order?\nEnter a \
number from the list above which matches the PC component you would like.")
    LOW = 1
    HIGH = 8
    component_selected = val_int(LOW, HIGH)
    print("\nYou have selected " + component_types[component_selected - 1])


# PC component ordering menu
def item_selection():
    global selected_item
    global selected_item_cost
    print("\nHere are the available types of",
          component_types[component_selected - 1])
    for x in range(len(components[component_selected - 1])):
        print(str(x + 1) + ")", components[component_selected - 1][x], "| $" +
              str(component_cost[component_selected - 1][x]))
    print("\nWhat type of", component_types[component_selected - 1],
          "would you like?")
    LOW = 1
    HIGH = len(components[component_selected - 1])
    num_input = val_int(LOW, HIGH)
    selected_item = components[component_selected - 1][num_input - 1]
    selected_item_cost = component_cost[component_selected - 1][num_input - 1]
    print("\nYou have selected the", selected_item)


# Select quantity of items
def quantity():
    global num_quantity
    global total_cost
    print("How many " + selected_item + "s would you like?\n(You can only \
order up to 5x " + selected_item + "s)")
    LOW = 1
    HIGH = 5
    num_quantity = val_int(LOW, HIGH)
    ordered_items.append(str(num_quantity) + "x " + selected_item)
    item_costs.append(selected_item_cost * num_quantity)
    total_cost = sum(item_costs)


# Display items selected
def display_selection():
    print("\nYou have ordered the following items: ")
    for x in range(len(ordered_items)):
        print(str(x + 1) + ". " + ordered_items[x] + " | Unit cost = $\
" + str(round(item_costs[x] / int(ordered_items[x][0]))) + " | Total = $" +
              str(item_costs[x]))
    print("\nSubtotal: $" + str(sum(item_costs)))


# Option to order another item or remove a selected item or proceed to checkout
def new_checkout():
    print("\nWould you like to order another PC component or proceed to \
checkout?\n\nTo order another item enter 'N'\nTo remove an item that has been \
selected enter 'R'\nTo proceed to checkout enter 'P'")
    while True:
        # Asks for letter and capitalises it
        answer = input("\nPlease enter a letter: ").upper()
        if answer == "N":
            print("\nOrdering another PC component...")
            pc_menu()
            break
        elif answer == "R":
            print("\nRemoving an item...")
            if len(ordered_items) == 1:
                print("\nYou have only ordered one item\nThere is no item that \
you can remove")
                new_checkout()
                break
            else:
                display_selection()
                remove_item()
                break
        elif answer == "P":
            print("\nProceeding to checkout...")
            break
        else:
            print("The input must be 'N', 'R' or 'P'")


# Removing an order
def remove_item():
    global total_cost
    print("\nWhich item would you like removed?")
    print("Enter a number from the list above which matches the item you would \
like removed.")
    LOW = 1
    HIGH = len(ordered_items)
    answer = val_int(LOW, HIGH)
    print("\nRemoving", ordered_items[answer - 1])
    del ordered_items[answer - 1]
    del item_costs[answer - 1]
    total_cost = sum(item_costs)
    display_selection()
    new_checkout()


# Checkout - Payment method
def checkout():
    global total_cost
    global payment_method
    print("\nYour details: ")
    if del_click == "D":
        total_cost += 5
        print("Your order is for delivery\nThere is a $5 delivery fee")
        print(f"\nCustomer Name: {customer_details['name']}\nCustomer Phone: \
{customer_details['phone']}\nCustomer Address: {customer_details['house']} \
{customer_details['street']}, {customer_details['suburb']}")
        display_selection()
        print("Delivery: $5\nTotal Order Cost: $" + str(total_cost))
    elif del_click == "C":
        print("Your order is for click & collect")
        print(f"\nCustomer Name: {customer_details['name']}\nCustomer Phone: \
{customer_details['phone']}")
        display_selection()
        print("Click & Collect: FREE\nTotal Order Cost: $" + str(total_cost))
    print("\nHow would you like to pay?\n\nHere are the available payment \
methods:")
    for x in range(len(payment_methods)):
        print(str(x + 1) + ")", payment_methods[x])
    print("\nSelect a payment method")
    LOW = 1
    HIGH = 6
    answer = val_int(LOW, HIGH)
    print("\nYou have selected", payment_methods[answer - 1])
    payment_method = payment_methods[answer - 1]


# Confirm order
def order_confirmation():
    print("\nTotal Order Cost: $" + str(total_cost) + "\nPayment Method:\
", payment_method)
    print("\nWould you like to confirm the order?\nTo confirm the order enter \
'Y'\nTo cancel the order enter 'N'")
    while True:
        answer = input("\nPlease enter a letter: ").upper()
        if answer == "Y":
            print("\nOrder Confirmed\nYour order has been placed and will be \
shipped tomorrow")
            if del_click == "D":
                print("Your order will arrive within 2-3 working days")
            break
        elif answer == "N":
            print("\nYour order has been cancelled")
            break
        else:
            print("The input must be 'Y' or 'N'")


# Option to restart the bot or to exit
def new_exit():
    print("\nWould you like to start another order or exit the bot\nTo start \
another order enter 'Y'\nTo exit the \
bot enter 'N'")
    while True:
        answer = input("\nPlease enter a letter: ").upper()
        if answer == "Y":
            print("\nStarting another order...")
            customer_details.clear()
            ordered_items.clear()
            item_costs.clear()
            main()
            break
        elif answer == "N":
            print("\nExiting the bot...")
            break
        else:
            print("The input must be 'Y' or 'N'")


# PC Menu function
def pc_menu():
    component_selection()
    item_selection()
    quantity()
    display_selection()
    new_checkout()


# Main function
def main():
    '''
    Purpose: To run all functions
    a welcome message
    Parameters: None
    Returns: None
    '''
    welcome()
    order_type()
    pc_menu()
    checkout()
    order_confirmation()
    new_exit()

main()