# Menu so that user can choose either delivery or click & collect

print("Would you like your order delivered or click & collected? ")

print("For delivey enter 1")
print("For click & collect enter 2")

delivery = int(input())

if delivery == 1:
    print("Delivery")

elif delivery == 2:
    print("Click & collect")

else:
    print("Invalid input")