def say_hello():
    print('hello')
    print('kenai9')
say_hello()

def say_hello2(name):
    print('Hello'+ '' + name)
say_hello2('Kelvin')

def add_num(x, y):
    sum = x + y
    return sum
#z = add_num(30 + 20)
#print(z)

def calculate_PI():
    pi=22/7
    return pi
p = calculate_PI
print(p)

def calculate_area(pi, r):
    area = pi* r**2
    return area
a = calculate_area(22/7, 7)
print(a)

def calculate_area(r, pi=22/7):
    area = pi* r**2
    return area
a1 = calculate_area(7)
a2 = calculate_area(14)
print(a1)
print(a2)

#Sets
my_sets = {12, 3, 4, 4}
print(my_sets)

#Lists
my_list = [1, 2, 3, 4, 4]
print(my_list)
my_list.append(5)
print(my_list[0])