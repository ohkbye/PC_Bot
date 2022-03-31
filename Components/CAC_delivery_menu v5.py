# Menu so that user can choose either delivery or click & collect

print("\nWould you like your order delivered or click & collected?\n\nFor delivery enter 'D'\nFor click & collect enter 'C'")
while True:
    delivery = input("\nPlease enter a letter: ").upper()
    if delivery == "C":
        print("\nYou have selected click & collect\n")
        break
    elif delivery == "D":
        print("\nYou have selected delivery\n")
        break
    else:
        print("The input must be 'C' or 'D'")


