#write a python prgram to calulate the body mass index(BMI)
#get the username
username=input("enter your name:")
print("THE FORMULA OF BMI=weight(kg)/height(m)^2")
weight=int(input("enter your weight(kg):"))
height=float(input("enter your height(m):"))

#calulate the BMI
BMI= weight/(height)*2
print(BMI)
print("Hello," +str(username) +" the calulation of your weight and height is:" +str(BMI))