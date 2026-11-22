#a = int(input("Enter any value between 5 and 9"))
#if (a>5 or a<9):
   # raise ValueError ("Value should be between 5 and 9")

# QUICK QUIZ

def vr():

    while True:
        user_input = int(input("Enter any value between 5 and 9 or quit"))
        if user_input.lower() == "quit":
            print("Exiting...")
            return
        elif not user_input.isdigit():
            print("Invalid input.Please enter a number")
        else:
            number = int(user_input)
        if 5 < number < 9:
            return
        else: 
            raise ValueError ("Please enter a number between 5 and 9")

