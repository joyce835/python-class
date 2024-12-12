#write a program to calulate the average allowance of a undergradutes
#weekly income for 4 week. make it user friendly by asking for name and department
username=input("kindly input your name?")

user_dapartment=input("kindly input your dapartment\n")
month=input("what month are we calulating?")

#method 1
wk1_allowance=input("enter your week 1 allowance:")
print(type(wk1_allowance))
converted_wk1_allowance=int(wk1_allowance)
print(type("converted_wk1_allowance"))

#method 2
wk2_allowance=int(input("enter your week 2 allowance:"))
wk3_allowance=int(input("enter your week 3 allowance:"))
wk4_allowance=int(input("enter your week 4 allowance:"))
total_allowance=converted_wk1_allowance+wk2_allowance+wk3_allowance+wk4_allowance

average_allowance=(total_allowance/4)
#print("Hello" + str(username) + "of" +str(user_dapartment)   + "dapartment .\n"
"Thanks for using my calutator.\nYour avarage allowance for the month of"+ str(month)
#str(avarage_allowance))


                   
                   
                   