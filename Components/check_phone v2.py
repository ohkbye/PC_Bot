def check_phone():
    while True:
            answer = input("Please enter your phone number: ")
            if answer.isdigit() == True:
                if len(answer) >= 7 and len(answer) <= 10:
                    return answer
                else:
                    print("\nNZ phone numbers must have between 7 and 10 digits")
            else:
                print("\nPlease enter a number between 7 and 10 digits")
print(check_phone())

