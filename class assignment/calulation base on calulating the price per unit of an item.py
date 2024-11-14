#write a python program to calulate the price per unit of an item when bought in bulk

print("You are Welcome for using My calulator:")
#get the username,and some necessary infromation
username=input("enter your name:")
total_price=int(input("enter the total price:$"))
number_of_units=int(input("enter the number of units:"))

#calulate the price per unit
price_per_unit=total_price/number_of_units
#print the end result
print("/nResult")
print("Total price:$" + str(total_price))
print("Number of unit:"+ str(number_of_units))
print("price per unit:$"+ str(price_per_unit))

#userfriendly greeting
print("Hello,"+ username + "Thanks for using my calulator to calulate your price per unit")
