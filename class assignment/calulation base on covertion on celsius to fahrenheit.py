#calulation base on convertion on celsius to fahrenheit
#get the username
username=input("enter your name:")

#Get the temperture in celsuis
celsuis=int(input("enter the temperture in celsuis:"))
#calculate the temperture in fahrenheit
fahrenheit=(celsuis*9/5) + 32
#print message result
print("Hello," + username + "!The temperature in fahrenhelt is:" + str(fahrenheit))