#Guessing a number correctly
#writing a python project whereby creating a logical thinking with the user.
#asking the user the to input any number, if the number guess right.
#score them correct.

name = "joy"
print(f"Hello {name}, welcome to a guessing game, have a nice gaming session.")

print("let the game begin in:")
for number in reversed(range(1,6)):
    print(number)
    
user_first_guess = int(input("guess a number"))
number = 2 + 1   #pls ignore this

if user_first_guess == number:
    print("you guessed right, nice try")
elif user_first_guess != number:
    print("wrong guess, pls try again")  #first guess
else:
    exit()

user_second_guess = int(input("guess a number"))
number = 2 + 3   #pls ignore this
if user_second_guess == number:
    print("you guessed right, nice try")
elif user_second_guess != number:
    print("wrong guess, pls try again")   #second guess
else: 
    exit()

user_third_guess = int(input("guess a number"))
number = 4 - 1   #pls ignore this     
if user_third_guess == number:
    print("you guessed right, nice try")
elif user_third_guess != number:
    print("wrong guess, pls try again")   #third guess     
else:
    print("enter a positive value")
    exit()









