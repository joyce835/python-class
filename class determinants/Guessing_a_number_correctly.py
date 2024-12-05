#Guessing a number correctly
#writing a python project whereby creating a logical thinking with the user.
#asking the user the to input any number, if the number guess right.
#score them correct.

def guess_number():
 user_guess=int(input("guess a number:"))
 if user_guess > number_to_guess:
    print("Too high")
 elif user_guess < number_to_guess:
    print("Too low")
 else:
    print("you got it right")
guess_number()

number_to_guess=42