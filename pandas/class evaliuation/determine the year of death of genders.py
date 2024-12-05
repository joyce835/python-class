

def yearofdeath(year_of_brith=int, gender=str)->str:
 """
determine gender terms base  on year of brith and gender.
Agr:
year of brith: The year at which the person was born
gender: The gender of the person ("Either male or female")

return:
the year of death base on(e.g year of brith and gender(" male" or "female"))

"""
 if gender =="female":
   return year_of_brith+104
 elif gender =="male":
   return year_of_brith+96
 else:
   return "unknown"


user_gender=yearofdeath(year_of_brith=int(input("enter your year of brith:")),gender=str(input("enter your gender:")) )
print(user_gender)



def price(price_of_fuel=int, number_of_liters=int)->str: 
  """
  Determine price terms base on price of fuel and number of liters.
  Agr:
  price of fuel: The amount of fuel at which the person bought
  number of liters: the number of fuel and liters at the which the bought 

  return:
  the price terms base on(e.g price of fuel and number of liters)
  """
  if price_of_fuel==456:
   price_of_fuel>=433
   print("buy") 
  else:
    print("don't buy")


  