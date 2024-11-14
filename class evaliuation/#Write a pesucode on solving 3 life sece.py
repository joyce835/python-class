#Write a pesucode on solving 3 life secenario(problems) and give their solutions
#Scenario 1: Going to the beach or not
""
username=input("enter your name:")
weather_condtion=input("enter weather(sunny/cloudy):")
if weather_condtion=="sunny" or weather_condtion=="cloudy":
    print("go to beach")
else:
    print("stay at home")

#Scenario 2: Taking a bus or taxi to go to your destination 
""
username=input("enter your name:")  
distance=int(input("enter your distance for your destination:"))
if distance<=5:
    print("take bus")
else:
    print("take taxi")

#scenario 3: Paying the bill if less than the actual price if not don't pay
"" 
username=input("enter your name:")
payment=int(input("enter your payment:"))
if payment<=50000: 
    print("pay")
else:
    print("don't pay")