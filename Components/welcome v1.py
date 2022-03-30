# PC bot program
import random
from random import randint

# List of random names 
names = ["Karlos", "Marcus", "Jaiden", "Railey", "Ivan", "James", "Joaquin", "Einstein", "Mikara", "Sharun", 
"Tomas", "Matt", "Levi", "Dennis", "Ochre", "Carlos", "Navhil", "George", "Billy", "Noel"]

num = randint(0, 9)

name = (names[num])

print("***** Welcome to Joaquins PC Store ******")
print("***** My name is ", name, " *****")
print("***** I will be here to help you order your PC component *****")