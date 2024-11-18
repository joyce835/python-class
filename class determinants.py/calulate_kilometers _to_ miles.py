#write a function km to miles(km) that convert distance from kilometers to miles
#1km=0.621371 miles

def km_to_miles(km):
    return km * 0.621371
km=float(input("enter distance in km:"))
result=km_to_miles(km)
print("distance in miles:",result)
