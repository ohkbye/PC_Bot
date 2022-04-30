def val_int(low, high):
    while True:
        try:
            num = int(input(f"Enter a number between {low} and {high}: "))
            if num >= low and num <= high:
                return num
            else:
                print(f"Please enter a number between {low} and {high}")
        except:
            print("That is not a valid number")
            print(f"Please enter a number between {low} and {high}")

LOW = 1
HIGH = 2
answer = val_int(LOW, HIGH)
print(answer)
