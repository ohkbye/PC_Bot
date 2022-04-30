def val_int():
    while True:
        try:
            num = int(input(""))
            if num >= 1 and num <= 2:
                return num

            else:
                print("The number must be 1 or 2")
        except:
            print("That is not a valid number")
            print("Please enter 1 or 2")

print("Enter a number between 1 and 2")

answer = val_int()

print(answer)
