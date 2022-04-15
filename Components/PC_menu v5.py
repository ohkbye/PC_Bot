

from multiprocessing.sharedctypes import Value


ordered_items = []
item_costs = []
component_types = ["CPU", "Storage", "Motherboard", "Power supply", "RAM", "Graphics card", "Operating System", "Case"]

components = [["AMD CPU", "Intel CPU"], ["SSD", "HDD"], ["ATX Motherboard", "Micro-ATX Motherboard", "Mini-ITX Motherboard"], 
["Fully Modular Power Supply", "Semi Modular Power Supply", "Non Modular Power Supply"], ["4GB RAM", "8GB RAM", "16GB RAM"],
["Nvidia GeForce Graphics Card", "AMD Radeon Graphics Card"], ["Windows 10 Operating System", "Windows 8 Operating System"],
["Full Tower PC Case", "Mid Tower PC Case", "Mini Tower PC Case"]]
component_cost = [[199, 239], [149, 99], [69, 59, 49], [79, 69, 59], [29, 39, 49], [269, 249], [29, 19], [49, 39, 29]]

def component_selection():
    for x in range(len(component_types)):
        print(str(x + 1) + ")", component_types[x])
    print("\nWhat type of PC component would you like to order?\nEnter a number from the list above which matches the PC component you would like.")
    while True:
        global component_selected
        try:
            component_selected = int(input("\nPlease enter a number: "))
            if component_selected >= 1 and component_selected <= 8:
                break
            else:
                print("\nYou must enter a number between 1 and 8")
        except:
            print("\nInvalid input\nYou must enter a number between 1 and 8")
    print("\nYou have selected " + component_types[component_selected - 1])

def item_selection():
    print("\nHere are the available types of", component_types[component_selected - 1])
    for x in range(len(components[component_selected - 1])):
        print(str(x + 1) + ")", components[component_selected - 1][x], "$" + str(component_cost[component_selected - 1][x]))
    print("\nWhat type of", component_types[component_selected - 1], "would you like?")
    while True:
        try:
            num_input = int(input("Please enter a number: "))
            for x in range(len(components[component_selected - 1])):
                if num_input == x + 1:
                    global selected_item
                    global selected_item_cost
                    selected_item = components[component_selected - 1][x]
                    selected_item_cost = component_cost[component_selected - 1][x]
                    print("\nYou have selected the", selected_item)
                    return
            else:
                print("\nYou must enter a number between 1 and", len(components[component_selected - 1]))
        except ValueError:
            print("\nInvalid input\nYou must enter a number between 1", len(components[component_selected - 1]))

def quantity():
    while True:
        try:
            num_quantity = int(input(str("How many " + selected_item + "s would you like?\n(You can only order up to 5x " + selected_item + "s)\n\nPlease enter the quantity: ")))
            if num_quantity >= 1 and num_quantity <= 5:
                ordered_items.append(str(num_quantity) + "x " + selected_item)  
                item_costs.append(selected_item_cost * num_quantity)      
                break
            else:
                print("\nYou must enter a number between 1 and 5")
        except ValueError:
            print("Invalid Input\nYou must enter a number between 1 and 5")
    

component_selection()
item_selection()
quantity()


print("You have ordered the following items: ")
for x in range(len(ordered_items)):
    print(ordered_items[x] + " for $" + str(item_costs[x]))
print("Your total is $" + str(sum(item_costs)))
