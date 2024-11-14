#write a python program to calulate the total salary of an emloyee.
print("You are welcome to the simple Calulator")
#get the username and some necessary information from the user
username=input("enter your user name:")
base_salary=float(input("enter your base salary:$"))
bonus_percentage=float(input("enter your bonus percentage:%"))
tax_percentage=float(input("enter your tax percentage:%"))

#calulate the bonus amount and tax amount
bonus_amount=base_salary*(bonus_percentage/100)
tax_amount=base_salary*(tax_percentage/100)

#calulate the total salary
total_salary=base_salary+tax_percentage-tax_amount

print("Total salary is:$" + str(total_salary))
print("Bonus:$"+ str(bonus_amount))
print("Taxes:-$"+ str(tax_amount))

#print userfriendly greeting
print("Hello,"+ username + "Thanks for using my simple calulator to calulate your salary")

