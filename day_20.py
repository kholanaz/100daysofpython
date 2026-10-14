# Two types of function 
# Built in function (we don't have to use the term "def")
# User defined function (we have to use the  term "def")
a= 9
b= 8
gmean1= (a*b)/(a+b)
print(gmean1)

c= 6
d= 4
gmean2= (c*d)/(c+d)
print(gmean2)

def calculateGmean(e,f):
    mean= (e*f)/(e+f)
    print(mean)
e= 5
f=3
calculateGmean(e,f)

g= 2
h= 7
if(g>h):
    print("First number is greater")
else:
    print("Second number is greater or equal")

def isGreater(c,d):
    if(c>d):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(c,d):
    pass
