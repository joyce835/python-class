#write a function factorial (n) that returns the factorial of a given number
def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)
num=int(input("enter a number:"))
print("factorial of", num ,"is",factorial(num))
