#Write a python prgram to calulate the fuel efficency of car in klilometer per liter
#write out the username first
username=input("enter your name:")
price=int(input("enter your price:"))
#get the tax rate
tax_rate=0.07
#calculate the tax 
tax=price*tax_rate
#calculate the total bill
total_bill=price+tax
#message result
print("Hello,"+username+"!Your total bill is:"+ str(total_bill))