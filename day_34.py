# ep = employee ID
ep1 = {123: 23, 456: 45, 432: 90, 862: 76}
ep2 = {321: 98, 423: 32, 657: 50}
ep1.update(ep2)
print(ep1)

ep1.clear()
print(ep1)

empt = {}
print(empt)

ep1.pop(123)
print(ep1)

ep1.popitem
print(ep1)

del ep1[456]
print(ep1)
