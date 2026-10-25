# EXERCISE 2 "GOOD MORNING"
# CREATE A PUTHON PROGRAM CAPABLE OF GREETING YOU WITH GOOD MORNING, GOOD AFTERNOON AND GOOD EVENING. YOUR PROGRAM SHOULD USE TIME MODULE 
# TO GET THE CURRENT HOUR. HERE IS A SAMPLE PROGRAM AND DOCUMENTATION LINK FOR YOU:

import time 
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter hour: "))
print(hour)

if (hour>=0 and hour<12):
    print("Good Morning Sir!")
elif (hour>=12 and hour<17):
    print("Good Afternoon Sir!")
elif (hour>=17 and hour<0):
    print("Good Evening Sir!")

