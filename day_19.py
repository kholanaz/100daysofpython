for i in range(12):
    if (i == 10):
        break
    print("5 X", i+1, "=", 5 * (i+1))

print("Loop ko chor diya ")


for i in range(12):
    if (i == 10):
        print("Skip the iteration")
        continue
    print("6 X", i, "=", 6 * i)


# DO-WHILE LOOP
i=0
while True:
    print(i)
    i= i+1 
    if(i%100 == 0):
        break

