#write a function to calulate_power(base)that calulate the power of a number

def calulate_power(base,exponent):
    return base * exponent
base=int(input("enter your base:"))
exponent=int(input("enter your exponent:"))
result=calulate_power(base,exponent)
print("The result is:",result)