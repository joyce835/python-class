#calulation base on simple interest
#username
username=input("enter your name:")

#collect the principle amount,rate of interest,and time rate
principal=int(input("enter the principal amount:"))
rate=int(input("enter the rate of interest(%):"))
time=int(input("enter the time(years):"))

#formula of simple interest
simple_interest=(principal*rate*time)/100

#calulate the total amount(principal+ interest)
total_amount=principal+simple_interest
#print the total amount
print("Hello,{username},your total amount is:${total_amount}")