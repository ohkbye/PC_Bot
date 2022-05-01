def check_phone(question, ph_low, ph_high):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num //= 10
                count += 1
            if count >= ph_low and count <= ph_high:
                return num
            else:
                print("NZ phone numbers have between 7 and 10 digits")
        except:
            print("Please enter a number")

ph_low = 7
ph_high = 10
question = "Please enter your phone number: "

phone = check_phone(question, ph_low, ph_high)
print(phone)
