#write a function area of circle using the formula 
import math
def area_of_circle():
    radius=int(input("enter the radius of circle:"))
    print (math.pi * radius ** 2)
print(area_of_circle())