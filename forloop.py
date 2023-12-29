for i in range(5, 10):
    print(i)

x = 50
if x > 50:
    print("x is greater than 50")
else:
    print("x is less than 50")

#while true
#do
names = {"wei", "Nikki", "Akua"}
for name in names:
    newName = name.capitalize()
    print (newName)

def capitalize(name):
    return name.capitalize()
names = {"wei", "Nikki", "Akua"}
for name in names:
    newName = capitalize(name)
    print (newName) 

if 20 > 30:
    print("Too High!")
elif 20 < 30:
    print("Too low")
else:
    print("Exactly right")

if (name=="Juan"):
    bonus= 300
else:
    bonus= 0