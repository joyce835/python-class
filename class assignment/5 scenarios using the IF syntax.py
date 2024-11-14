#write out 5 real life scenraios using "IF statement"


age=int(input("enter your age:"))
if age>=5 and age <=6:
    print("enter daycare")
if age >=7 and age <=10:
    print("apply for elementry school")
if age >=11 and  age <=18:
    print("apply for high school")
if age >=19 and  age <=29:
    print("apply for college")

number_of_books=int(input("enter the books to school:"))
if number_of_books>=10:
    print("don't carry ")
if number_of_books<=8:
    print("carry")

weather=input("enter weather(sunny/cloudy):")
if weather=="sunny":
    print("go outside and play")
if weather== "cloudy":
    print("stay at home")