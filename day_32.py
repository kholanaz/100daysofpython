s1= {1,2,5,6,7}
s2= {3,6,8,9}

print(s1.union(s2))

s1.update(s2)

print(s1,s2)

cities1 = {"Tokyo","Delhi","Karachi","Islamabad"}
cities2 = {"London","Lahore","Islamabad"}

cities3 = cities1.intersection(cities2)

print(cities3)

cities1.intersection_update(cities2)

cities4= cities1.symmetric_difference(cities2)

print(cities1.isdisjoint(cities2))

print(cities1.issuperset(cities2))

print(cities1.issubset(cities2))

cities1.add("Istanbul")
print(cities1)

cities1.remove("Tokyo")
print(cities1)

cities1.discard("Tokyo")
print(cities1)

