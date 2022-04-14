ordered_items = []
item_cost = []
component_types = ["CPU", "Storage", "Motherboard", "Power supply", "RAM", "Graphics card", "Operating System", "Case"]
def cpu():
    print("\n1) AMD CPU $199\n2) Intel CPU $299\nWhich type of CPU would you like?")
    while True:
        try:
            num_input = int(input("\nPlease enter a number: "))
            if num_input == 1:
                print("You have selected an AMD CPU")
                ordered_items.append("AMD CPU")
                item_cost.append(199)
                break
            elif num_input == 2:
                print("You have selected an intel CPU")
                ordered_items.append("Intel CPU")
                item_cost.append(299)
                break
            else:
                print("\nYou must enter a number between 1 and 2")
        except:
            print("\nInvalid input\nYou must enter a number between 1 and 2")
    for x in range(len(ordered_items)):
        print(ordered_items[x])
def storage():
    print("\n1) SSD $149\n2) HDD $99\nWhat type of storage would you like?")
    while True:
        try:
            num_input = int(input("\nPlease enter a number: "))
            if num_input == 1:
                print("You have selected an SSD storage")
                ordered_items.append("SSD storage")
                item_cost.append(149)
                break
            elif num_input == 2:
                print("You have selected a HDD storage")
                ordered_items.append("HDD storage")
                item_cost.append(99)
                break
            else:
                print("\nYou must enter a number between 1 and 2")
        except:
            print("\nInvalid input\nYou must enter a number between 1 and 2")
    for x in range(len(ordered_items)):
        print(ordered_items[x])
def motherboard():
    print("\n1) AMD Desktop Motherboard $149\n2) Intel Desktop Motherboard $99\nWhat type of motherboard would you like?")
    while True:
        try:
            num_input = int(input("\nPlease enter a number: "))
            if num_input == 1:
                print("You have selected an SSD storage")
                ordered_items.append("SSD storage")
                item_cost.append(149)
                break
            elif num_input == 2:
                print("You have selected a HDD storage")
                ordered_items.append("HDD storage")
                item_cost.append(99)
                break
            else:
                print("\nYou must enter a number between 1 and 2")
        except:
            print("\nInvalid input\nYou must enter a number between 1 and 2")
    for x in range(len(ordered_items)):
        print(ordered_items[x])
    

for x in range(len(component_types)):
    print(str(x + 1) + ")", component_types[x])
print("\nWhat type of PC component would you like to order?\nEnter a number from the list above which matches the PC component you would like.")
while True:
    try:
        component_selection = int(input("\nPlease enter a number: "))
        if component_selection >= 1 and component_selection <= 6:
            break
        else:
            print("\nYou must enter a number between 1 and 6")
    except:
        print("\nInvalid input\nYou must enter a number between 1 and 6")

print("\nYou have selected " + component_types[component_selection - 1])
if component_selection == 1:
    cpu()
elif component_selection == 2:
    storage()
elif component_selection == 3:
    motherboard()





