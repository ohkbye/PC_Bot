def check_string(question):
    while True:
        answer = input(question)
        x = answer.isalpha()
        if x == False:
            print("Input must only contain letters")
        else:
            return answer.title()
            

question = "Enter your name: "
name = check_string(question)
print(name)