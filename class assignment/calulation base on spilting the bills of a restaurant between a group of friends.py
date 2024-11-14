#write a python program to spilt up a restaurant bill between a group of friends
print("You are Welcome to my simple calulator")
#get the username of some necessary information
username=input("enter your name:")
total_bill=int(input("enter your total bill amount:$"))
number_of_people=int(input("enter the number of people:(1-20)"))
tip_percentage=int(input("enter your tip percentage:%"))

#calulate the total of the things
total_amount=total_bill+(total_bill*(tip_percentage/100))
#calulate the amount of each person ownes per person
amount_per_person=total_amount/number_of_people
#print the ending result
print("Total bill:$"+ str(total_bill))
print("Tip percentage:%"+str(tip_percentage))
print("Total amount:$"+ str(total_amount))
print(" Amount each person ownes:$"+ str(amount_per_person))

#print the userfriendly greeting
print("Hello," + username +"Thanks for using my simple calulator:")