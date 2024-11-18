#write the function of max of three (a b c) that returns the maximum of three numbers

def max_of_three():
    a=int(input("enter your first number:"))
    b=int(input("enter your second number:"))
    c=int(input("enter your third number:"))
    return max(a,b,c)
print(max_of_three())