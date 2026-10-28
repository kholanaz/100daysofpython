letter = "My name is {} and I am from {}"
country = "Pakistan"
name = "Ayesha"
print(letter.format(name,country))

numbers = "My cousin name is {1} and he is from {0}"
name= "Khadija"
country = "India"
print(numbers.format(country,name))
print(f"Hey my name is {name} and I am from {country}")

print(f"We use f-string like this:Hey my name is {{name}} and I am from {{country}}")

price = 49.09999999
txt = f"for only {price:.2f} dollars!"
print(txt)

print(f"{2 * 30}")
print(type(f"{2 * 30}"))