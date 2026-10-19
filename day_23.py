l=[1,2,3,4,5,6]
print(l)
l.append(8)
print(l)

l=[43,23,67,30]
l.sort()
print(l)

l.sort(reverse=True) 
print(l)

l=[21,89,67,54]
l.reverse()
print(l)

print(l.index(89))
print(l)

l=[1,2,3,4,5,3,6,3]
print(l.count(3))

m=l.copy()
m[0]=0
print(l)

l=[23,87,65,43]
l.insert(65, 655)
print(l)

m=[400,900,500]
l.extend(m)
print(l)
