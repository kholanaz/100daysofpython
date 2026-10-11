# (i) is denoted to write a word in separate letters.
name= "Ayesha"
for e in name:
    print(e)
    if(e =="b"):
        print("This is something special!")

colors= ["Red", "Yellow", "Brown", "Green"]
for colors in colors:
    print(colors)
    for i in colors:
        print(i)

# RANGE()
# Range to write a big number like 20,000 easily ina one go
for k in range(5):
    print(k)

for k in range(6):
    print(k+1)

for k in range(1, 9):
    print(k)

for k in range(1, 20001):
    print(k)

for k in range(1, 15, 2):
    print(k)