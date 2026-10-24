countries= ("Pakistan","Turkey","Spain","Russia")
temp=list(countries)
temp.append("Italy")
temp.pop(3)
temp[2]="Finland"
countries=tuple(temp)
print(countries)

countries2= ("Japan", "China", "Bangladesh")
southEastAsia =countries + countries2 
print(southEastAsia)

tuple1=(0,1,2,3,2,3,1,3,2)
res= tuple1.count(3)
print('Count of 3 is:', res)

tuple2=(4,3,5,2,6)
res= tuple2.index(5)
print('Count of 3 is:', res)

res=len(tuple2)
