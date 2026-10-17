def average(a=9,b=1):
    print("The average is", (a+b)/2)

average(4,6)   
average(b=9)

def name(fname, mname="Ayesha", lname = "Khadija"):
    print("Hello,", fname, mname, lname)

name("Wania", "Khadija", "Ayesha")

def average(d,e,f=8):
    print("The average is", (d+e+f)/2)

average(5,2)

def average(*numbers):
    print(type(numbers))
    sum =0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))
average(6,9)
    
    