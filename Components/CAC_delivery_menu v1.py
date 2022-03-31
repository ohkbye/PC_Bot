# Bugs
# Will only work for valid inputs "D" and "C"
# Invalid input triggers else statement but program does not ask for input again

# Menu so that user can choose either delivery or click & collect

print("Would you like your order delivered or click & collected: ")

print("For delivey enter D")
print("For click & collect enter C")

delivery = input()

if delivery == "D":
    print("Delivery")

elif delivery == "C":
    print("Click & collect")
