l = [4,5,2]
print(l)
print(type(l))

marks = 8,6,9
print(marks[0])
print(marks[1])
print(marks[2])

details=["Ayesha", 6, "Fatima", 7]
print(details)

colors=["Red","Green","Yellow"]
# INDEX [0],    [1],    [2]
print(colors)
# length is 3 but index is 2

seasons=["Summer","Winter","Autumn","Spring"]
#       [-4],      [-3],    [-2],     [-1]
print(seasons[-2]) # Negative index
print(seasons[len(seasons)-2]) #Positive index

if "friday" in seasons:
    print("Yes")
else:
    print("No")

if "mmer" in "Summer":
    print("Yes")
else:
    print("No")

print(marks)
print(marks[1:])

lst= [i for i in range(6)]
print(lst)

lst= [i for i in range(6) if i%2==0]
print(lst)
