#Strings are immutable means that it cannot be changed.
a = "Ayesha"
print(len(a))

#upper case= to write your word in capital letter.
print(a.upper())

# Lower case means to write a string in small letter.
print(a.lower())

# RSTRIP()
b= "Fatima!!!!!!!!"
print(b)
print(b.rstrip("!"))
c= "!!!!!Khadija!!!!!"
print(c.rstrip("!"))

# Replace()
print(a.replace("Ayesha","Haniya"))

# SPLIT()
d= "!!!!! Haniya !!!!!!"
print(d.split(" "))

# Capitalize()
blogHeading= "introduction tO js"
print(blogHeading.capitalize())

# CENTER ()
e= "Welcome to the console!!!!!"
print(e.center(50)) 

# COUNT ()
print(a.count("Ayesha"))

# ENDS WITH()
f= "Welcome to the console!!!"
print(f.endswith("!!!"))

# FIND ()
g= "He's name is Den.He is seven years old."
print(g.find("is"))

# ISALNUM()
h="WelcomeToTheConsole"
print(h.isalnum())

# ISALPHA()
i= "Welcome"
print(i.isalpha())

# ISLOWER
j= "hello world"
print(j.islower())

# ISPRINTABLE()
k= "We wish you a happy birthday"
print(k.isprintable())

# ISSPACE()
l= "        "
print(l.isspace())

# ISTITLE
m= "World health organization"
print(m.istitle())

# STARTSWITH ()
n= "Python is an Interpreted Language"
print(n.startswith("Python"))

# SWAPCASE()
o= "Today is Friday"
print(o.swapcase())

# TITLECASE()
p= "September is a hot month"
print(p.title())
