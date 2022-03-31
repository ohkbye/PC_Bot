# Menu so that user can choose either delivery or click & collect

# Bug - need to make it so that it only accepts 1 or 2
from multiprocessing.sharedctypes import Value


print("Would you like your order delivered or click & collected? ")

print("For delivey enter 1")
print("For click & collect enter 2")


while True:
    try:
        delivery = int(input("Please enter a number: "))
        if delivery >= 1 and delivery <= 2:
            if delivery == 1:
                print("Delivery")
                break

            elif delivery == 2:
                print("Click & collect")
                break
        else:
            print("The number must be 1 or 2")
    except ValueError:
        print("That is not a valid number")
        print("Please enter 1 or 2")

