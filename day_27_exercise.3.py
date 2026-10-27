# CREATE A PROGRAM CAPABLE OF DISPLAYING QUESTIONS TO THE USER LIKE KBC.
# USE LIST DATA TYPE TO STORE THE QUESTIONS AND THEIR CORRECT ANSWERS.
# DISPLAY THE FINAL AMOUNT THE PERSON IS TAKING HOME AFTER PLAYING THE GAME.

questions = [
    [
        "What is the national juice of Pakistan", "Rooh Afza", "Sugar Cane",2
    ],  
    [
        "What is the national flower of Pakistan", "Jasmine", "Sun Flower",1
    ],  
    [
        "What is the national sports of Pakistan", "Cricket", "Hockey",2
    ],  
    [
        "What is the capital of Japan", "Tokyo", "Osaka",1
    ],  
    [
        "What is the capital of Pakistan", "Karachi", "Islamabad",2
    ],  
    [
        "Who discovered gravity", "Issac Newton", "William Shakespere",1
    ],  
    [
        "What is the largest mammal on earth", "Dolphin", "Blue Whale",2
    ],
    [
        "Who painted the MONA LISA", "Leonardo da Vinci", "King Loius",1
    ],  
    [
        "Who invented telephone", "Alexender Graham Bell", "Deoder",1
    ],  
    [
        "What is the currency of USA", "Yen", "DOLLAR",2
    ],  
    [
        "Which planet is called red planet", "Mars", "Jupitar",1
    ],  
    [
        "Which is the largest ocean on earth", "Arabian sea", "Pacific Ocean",2
    ],  
    [
        "Which is the largest river in earth", "Nile river", "Amazon river",1
    ],  
    [
        "Who was the first man to land in the moon", "Neil river", "Neil Armstrong",2
    ],  
    [
        "Which country is known as the land of rising", "China", "Japan",2
    ]
]

Levels= [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,5000000,10000000]

money=0
for i in range (0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for rupees Rs.{Levels[i]}")
    print(f"a, {question[1]}              b. {question[2]}")
    reply = int(input("Enter your answer (1-2)"))
    if(reply == question[-1]):
        print(f"Correct answer, You have won RS.{Levels[i]}")
        if(i==1):
            money = 10000
        elif (i==2):
            money=2000
        elif (i==3):
            money=3000
        elif (i==4):
            money=5000
        elif (i==5):
            money=10000
        elif (i==6):
            money=20000
        elif (i==7):
            money=40000
        elif (i==8):
            money=80000
        elif (i==9):
            money=160000
        elif (i==10):
            money=320000
        elif (i==11):
            money=640000
        elif (i==12):
            money=1250000
        elif (i==13):
            money=2500000
        elif (i==14):
            money=5000000
        elif (i==15):
            money=10000000
    else:
        print("Wrong Answer!")
        break

print(f"You take home money is {money}")