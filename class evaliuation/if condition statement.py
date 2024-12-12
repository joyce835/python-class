#IF conditions
#types of if conditions
#if else statements
#else if statements
#nested if statements

"""
syantax of if statements
if condition:
   statement 1
   statement 2
   statement 3
"""

"""
syantax of if else statement
if condition:
   statement 1
   statement 2
   statement 3
else:
statament 4
statement 5
"""

"""
syntax of else statement
if condition:
   statement 1
elif condition 2:
   statement 2
elif condition 3:
   statement 3
elif condition 4:
   statement 4
elif condition 5:
   statement 5
elif condition 6:
   statement 6
"""


if 3<=2:
   print("stop drinking 33")
 
battery_level=int(input("enter the battery level?:"))
if battery_level <=15:
    print("battery low!!")


username=input("enter your name:")
user_salary=int(input("enter your salary:"))
if user_salary>=50000:
   print("they are rich")
else:
   print("they are poor")


grade=int(input("enter your grade:"))
if grade>=70:
   print("excellent result!!")
username=input("enter your name:")
grade=int(input("enter your grade:"))
if grade>=70:
   print("excellent result!!")
else:
   print("good result")
print("Hello,"+ (username) + " your result is good ")

battery_level=int(input("enter the battery level:"))  
if battery_level <= 15 and battery_level >= 0:
   print("battery low!!")
elif battery_level <=50 and battery_level >=16:
   print("battery is getting low!!")
elif battery_level <=80 and battery_level >=51:
   print("battery is well charged!!")
elif  battery_level <=99  and battery_level >=81:
   print("battery almost fully charged!!")
elif battery_level ==100:
   print("battery is fully charged!!")
else:
  print("ensure you input the right value")

username=input("enter your name:")
grade=int(input("enter your grade:"))
if grade <=40 and grade >=0:
   print("fail")
elif grade <=50 and grade >=40:
   print("poor")
elif grade <=59 and grade >=51:
   print("credit")
elif grade <=69 and grade >=60:
   print("Good")
elif grade <=79 and grade >=70:
   print("very Good")
elif grade <=100 and grade >= 80:
   print("Excellent")
else:
   print("any other value=Wrong score")