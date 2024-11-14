#create a program to calulate the user monthly tax by asking the following.......
#Name , office, month, salary, expenses.
#Do this by calulating leftover first and thereafter note the tax is 3% of the leftover
#make it user friendly by asking the for Name....

#Get user input
name=input("enter your name:")
office=input("enter your office:")
month=input("enter your month:")
salary= float = int(input("enter your salary:"))
expenses= float = int(input("enter your expenses:"))

#calulate tax(3% of leftovers)
tax=int(leftovers)*0.30

#Calulate leftovers(salary_expenses)
leftovers= salary-expenses

#calulate tax
tax= leftovers*0.03

#print result
print(str("name"))
print(str("office"))
print(str("month"))
print(int(salary))
print(int(expenses))
print(int(leftovers))
print(int(tax))

tax= salary * 0.03
print("hello((user_name)),your monthly tax in the (user_office) department for (user_monthly_tax)..")