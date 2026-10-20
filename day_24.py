tup = (3,5,7)
print(type(tup), tup)

tup = (2,)
print(type(tup), tup)

tup=[32,45,67,87]
tup[0]=90
print(type(tup), tup)

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

print(len(tup))

if 45 in tup:
    print("Yes 45 is present in this tup")
else:
    print("No 45 is snot present in this tup")

tup2= tup[1:4]
print(tup2)

#TUPLES ARE IMMUTABLE
