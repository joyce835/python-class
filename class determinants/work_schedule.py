#work schedule
#writing a python project whereby creating a work schedule plan for the user
#and inputing the days and times for the user.

#def checking_schedule(name):
name = input("enter your name:")
office=input("enter the name of your office:")
checking_schedule=input("do you want to check your schedule today?(no/yes)")
if checking_schedule == "yes":
 print("proceed")
else:
  exit()
day=input("what day it is?:")


def schedule(day):
  working_schedule=("monday","tuesday","Wednesday","Thrusday","Friday")
  if day in working_schedule:
    print("8:00am-5:00pm go to work")
  elif day =="Tuesday":
    print("9:00am -6:00pm still go to work")
  elif day=="wednesday":
    print("6:30pm-3:30pm go to work")
  elif day=="Thrusday":
    print("2:45pm-3:45pm go to work")
  elif day=="Friday":
    print("3:45pm-6:45pm still go to work")
  else:
    print("enjoy your day off")
  # elif checking_schedule == "no":
schedule(day)
 

