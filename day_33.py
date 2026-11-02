dic = {
    "Ayesha" : "Prohet's Last Wife",
    "Khadija" : "Prophet's First Wife"
}
print(dic["Khadija"])

# EMPLOY ID
dic = {
    342 : "Fatima",
    543 : "Aleena",
    654 : "Armish",
    980 : "Hashir"
}
print(dic[543])

info = {'name' : 'Kainat', 'age' : 19, 'eligible' : True}
print(info)
print(info['name'])
#print(info['name2'])
print(info.get("name2"))

# need all keys
print(info.keys())

for keys in info.keys():
    print(info[keys])
    print(f"the value corresponding to the keys {keys} is {info[keys]}")
print(info.values())
print(info.items())