#Defines the value of pi
pi = 3.14159
#calculates the area of a circle for a given radius
def circle_area(radius):
    #pi multiplied by r squared
    return pi*radius**2
r = int(input('Enter the radius of a circle:'))
area = circle_area(r)
print(area)