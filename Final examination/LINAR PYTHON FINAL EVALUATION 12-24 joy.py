"""FINAL EVALUATION
PYTHON PROGRAMMING LANGUAGE
DURATION: 1:45 MINS
Instructions: Answers 7 questions, Number 1, 5 and 9 is compulsory, Pick any 4 others. 
Remember, this evaluation has a lot to do with your certification.

"""

"""
You are advised not to cheat in any for, its an advice and not a must, since it’s not a must you get certified too.  
1)	Variable Data Types 
a) Create a variable called "Date_Of_Birth" and assign it the year you were born (or any random year) using the right datatype. Print the value of the variable. 
b) What is the difference between an integer and a floating-point number in Python? Backup your explanation with an example for each.
c) Explain the types of Logical operators with scenerios.

# QUestion 1 answer goes in here:
"""
("a")

Date_of_birth=23
print(type(Date_of_birth))
year_of_birth=2008
print(type(year_of_birth))


("b")
"integer:this can define as wholes numbers or number.this also converts interger to wholes numbers"
number_of_books=12 #this actually means the total numbers of books is 12
"Floating-points numbers :this can be define as a number that consist with decimal point(.)"
rate_of_taxs=12.3 # this actually means the rate of taxs is 12.3%


("c")
"logical operators this can be as a basic tool ones use to compare on or two things in life"
"and" "or" "not"
"NOT: this simply means a scenerios not true or not false"
"or:this simply means a scenerios having to situation two possiblities of being true or false"
#if i have cash with me or if i have a bike with me i will be able to go to school
"and:this simply means adding a condition or a scenerios to make it becomes true or false"
#if my dad gives my allowance and my tutor call me for class i will go
"""
2)	Basic Operations 
a) Write a Python program that adds two numbers together and prints the result. 
b) Write a Python program that takes a number as input and multiplies it by 10. Print the result.



# QUestion 2 answer goes in here:

"""
("a")
additions_of_number=34+45
print(additions_of_number)
("b")
total_numnber_of_books=34+45
print(total_numnber_of_books*10)
"""
3)	Control Structures 
a) Write a Python program that checks if a number is even or odd. If the number is even, print "Even", otherwise print "Odd". 
b) Write a Python program that takes a number as input and checks if it is positive, negative, or zero. Print the result.

(a)



# QUestion 3 answer goes in here:

"""
("a")

def is_even():
    number=int(input("enter a number:"))
    if number in range(2,50,2):
        print(number)
        print(is_even)
    else:
        return "odd"

("b")
def check_postive_negative(number):
   return f"postive"
if -10 >0 :
    print("postive")
else:
    "negative"

#output : negative

"""
4)	Lists, Loops and Data Structure
a) Create a list of numbers from 1 to 10. Print each number in the list using a loop. 
b) Write a Python program that takes a list of numbers as input and returns the sum of all the numbers in the list.
c) Create a dictionary ‘colleague_name’ storing all your colleague names. Hint: Use sequence of numbers as their key.  





# QUestion 4 answer goes in here:

"""


"""
5)	Functions 
a) Write a Python function that takes three numbers as input and return their multiplication. 
b) Write a Python function that takes a list of numbers as input and returns the average of all the numbers in the list.
c) Greet a User: Write a function greet_user(name) that takes a person's name as input and returns a greeting message.
Example: Output: "Hello, Alice! Welcome!"
d) Calculate Simple Interest: Write a function simple_interest(principal, rate, time) that calculates simple interest.
Example: Input: simple_interest(1000, 5, 2)
Output: 100.0

e) Convert Minutes to Seconds: Write a function minutes_to_seconds(minutes) that converts a given number of minutes into seconds.
Example:
Input: minutes_to_seconds(5)
Output: 300





# QUestion 5 answer goes in here:

"""
("a")
total_numbers=12+13+14
print(total_numbers*2)
("b")
list_of_number=[1,2,3,4,5,6,7,8,9,10]
total_list_of_numbers=1+2+3+4+5+6+7+8+9+10
print(total_list_of_numbers)
sum_of_average=total_list_of_numbers
("c")
def greet_user(name):
    """
    """
    return f"Hello,{name} ! welcome"
print(greet_user("alice"))
("d")

def simple_interest(prinical,rate,time):
    """
    """
    print(prinical * rate * time)/100
prinical=int(input("enter your princical amount:"))
rate=int(input("enter your rate amount:"))
time=int(input("enter your time amount:"))
print(simple_interest)
print(prinical * rate * time)/100

("e")

def minutes_to_seconds(minutes):
    return f"{minutes * 60}"
print(minutes_to_seconds(5))
# output:300


"""
6)	Libraries and Modules 
a) Install and Import the "math" module and use its "sqrt" function to calculate the square root of a number. 
b) Install and Import the "random" module and use its "randint" function to generate a random number between 1 and 10.
c) Install and Import the "pywhatkit" module and use its "whatsapp" function to send a DM to your tutor with the body “Good Day Sir”



# QUestion 6 answer goes in here:

"""
"""
7)	 Explain the following terms relating to Python programming Language with examples where needed
a)	Escape Sequence
b)	Keywords
c)	Datatypes
d)	Dictionary 
e)	Module
f)	Interpreter
g)	Give a brief history of python, who built it, what led to Python and others, state the current version of python you are using.




# QUestion 7 answer goes in here:

"""
("7a")
#Escape sequence: this can be define as datatype with a non charater but they are represented with a backslah(/)
"e.g are newline(/n),tabline(/) and backskah(//)"
#keywords :this can be define as words or tool or keys that are used in pythons 
"e.g else nonlocal if pass break elif none"
#datatypes :this can be define as a collation of data or association of data resources which tells or help the computer to interpret it's value
"e.g sting ingerter boolean float none"
name="joy"#string
print(name)
numbers=12 #interger
print(numbers)
is_admin_in=True #boolean
print(is_admin_in)
rate_of_taxs=12.45 #flaot
print(rate_of_taxs)
favourite_food=None #none
print(favourite_food)
#Dictionary:This can be define as a relate information of a person or a details of a person
person={"name":"Joy", "age":30}
#Module:This can be define a related collection of function,variables,class(blueprint) to build up a module
"e.g pandas, beautifulsoup "
# inpterpret:This can be define as a machine whereby the user passes a series of code into the machine and therefore the machine access the code line by line and give it to the user and therefore if it finds out there is an error in a particular line of code in gives it back to the user indicating the error and giving some solutions to that line.


"""
8)	Mentions some tools used the career listed below, write extensively on the career you are choosing after this course. Explain what the career entails and the problem skilled professionals in the career solve in the real-world market.
a)	Data Scientist
b)	Software Engineer
c)	Data Engineer
d)	Data Analytics
e)	Web Developer (Backend Developer)
f)	Machine Learning Engineer




# QUestion 8 answer goes in here:

"""


"""
9)	Give a feedback on this Python course, your instructor and this examination.


Question 9 answer goes in here:
This python course so far.
Is very easy to understand:The course was explained in a complex yet easy to understand manner through simplfied notes
In this python course, there are also alot of practical aspect in this python course making it easy for beginners to  understand what they have been taught so far during the course of their training
In this python course there were Too much theory, at times this course focuses more on theorethical aspect making it harder to understand for example "FOR LOOP" function
In this python course they were topics that were rush quite a bit.
This python course is highly suitable for beginners or those people who are in it.
Our instructor is a nice person and a very educative person he taught us about the necessary things and also some tools that we need a pythonistas.
And examination is a great one .

BEST OF LUCK
"""