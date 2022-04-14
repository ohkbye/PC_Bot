component_types = ["CPU", "Storage", "Motherboard", "Power supply", "RAM", "Graphics card", "Operating System", "Case"]

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

