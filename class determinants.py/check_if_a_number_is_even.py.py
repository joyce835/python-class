#write a function is even (number) that checks if a given number is even

def is_even():
    number=int(input("enter a number:"))
    if number % 2==0:
        print(True)
    else:
        print(False)
print(is_even())