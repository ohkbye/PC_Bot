# PC bot program
from random import randint

# List of random names
names = ["Karlos", "Marcus", "Jaiden", "Railey", "Ivan", "James", "Joaquin", "Einstein", "Mikara", "Sharun", 
"Tomas", "Matt", "Levi", "Dennis", "Ochre", "Carlos", "Navhil", "George", "Billy", "Noel"]

# Welcome message with random name
def welcome():
    # Creating an integer variable, num with a random value from 0 to 9
    num = randint(0, 9)

    # Picking a random name from the names list and making it a string
    name_msg = "My name is " + names[num]

    # Print welcome message
    welcome_msg = ["Welcome to Joaquins PC Store", name_msg, "I will be here to help you order your PC component"]
    print("\n\n\n")
    # Center text
    for x in range(len(welcome_msg)):
        print(str("***** " + welcome_msg[x] + " *****").center(100," "))
    print("\n\n\n")

# Menu so that user can choose either delivery or click & collect
def order_type():
    print("\nWould you like your order delivered or click & collected?\n\nFor delivery enter 'D'\nFor click & collect enter 'C'")
    # Loops the code inside until user enters a valid input 'C' or 'D'
    while True:
        # Asks for letter and capitalises it
        delivery = input("\nPlease enter a letter: ").upper()
        if delivery == "C":
            print("\nYou have selected click & collect\n")
            break
        elif delivery == "D":
            print("\nYou have selected delivery\n")
            break
        else:
            print("The input must be 'C' or 'D'")


# Click & collect information - name and phone number

# Delivery informtion - name, address and phone

# Choose type of PC component

# PC component menu

# PC component order - from menu - print each component ordered with cost

# Print order out - including if order is delivery or click & collect and names and price of each component - total cost including any delivery charge

# Ability to remove an item, cancel or proceed with order

# Option for new order or to exit

# Payment method

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

main()