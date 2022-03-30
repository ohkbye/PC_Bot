# importing randint from random module
from random import randint

# List of random names
names = ["Karlos", "Marcus", "Jaiden", "Railey", "Ivan", "James", "Joaquin", "Einstein", "Mikara", "Sharun", 
"Tomas", "Matt", "Levi", "Dennis", "Ochre", "Carlos", "Navhil", "George", "Billy", "Noel"]

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

