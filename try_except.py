from mod import area_of_a_triangle, area_of_rectangle, area_of_circle
print(area_of_a_triangle(10, 5))
try:
    print(area_of_circle(10))
except:
    print("Error occured in circle area")
try:
    print(area_of_a_triangle(10, 5))
except:
    print("Error occured in circle area")
