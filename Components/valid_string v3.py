def check_string(question):
    while True:
        answer = input(question)
        if answer:
            if any(char.isdigit() for char in answer) == True:
                print("\nInput must only contain letters")
            else:
                return answer.title()
        else:
            print("\nInput cannot be blank")
        
            

question = "Enter your name: "
name = check_string(question)
print(name)