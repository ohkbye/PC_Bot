

ordered_items = []
item_cost = []
component_types = ["CPU", "Storage", "Motherboard", "Power supply", "RAM", "Graphics card", "Operating System", "Case"]

components = [["AMD CPU", "Intel CPU"], ["SSD", "HDD"], ["ATX Motherboard", "Micro-ATX Motherboard", "Mini-ITX Motherboard"], 
["Fully Modular Power Supply", "Semi Modular Power Supply", "Non Modular Power Supply"],]
component_cost = [[199, 239], [149, 99], [69, 59, 49], [79, 69, 59]]
def item_selection():
    print("\nHere are the available types of", component_types[component_selection - 1])
    for x in range(len(components[component_selection - 1])):
        print(str(x + 1) + ")", components[component_selection - 1][x], "$" + str(component_cost[component_selection - 1][x]))
    print("\nWhat type of", component_types[component_selection - 1], "would you like?")
    while True:
        try:
            num_input = int(input("Please enter a number: "))
            for x in range(len(components[component_selection - 1])):
                if num_input == x + 1:
                    print("\nYou have selected the", components[component_selection - 1][x])
                    ordered_items.append(components[component_selection - 1][x])
                    item_cost.append(component_cost[component_selection - 1][x])
                    return
            else:
                print("\nYou must enter a number between 1 and", len(components[component_selection - 1]))
        except ValueError:
            print("\nInvalid input\nYou must enter a number between 1", len(components[component_selection - 1]))



for x in range(len(component_types)):
    print(str(x + 1) + ")", component_types[x])
print("\nWhat type of PC component would you like to order?\nEnter a number from the list above which matches the PC component you would like.")
while True:
    try:
        component_selection = int(input("\nPlease enter a number: "))
        if component_selection >= 1 and component_selection <= 8:
            break
        else:
            print("\nYou must enter a number between 1 and 8")
    except:
        print("\nInvalid input\nYou must enter a number between 1 and 8")

print("\nYou have selected " + component_types[component_selection - 1])
item_selection()
for x in range(len(ordered_items)):
    print(ordered_items[x])