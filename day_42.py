marks = [45, 67, 87, 98, 1, 76]
index = 0 
for mark in marks:
    print(mark)
    if (index == 3) :
        print("Ayesha, Awesome!")
    index += 1

for index, mark in enumerate (marks, start = 1):
    print(mark)
    if (index == 3) :
        print("Ayesha, Awesome!")
