#write a fuction is_prime(number) that check if number is a prime
def is_prime(number):
    if number<=1:
        return False
    for i in range (2,int (number)**0.5+1):
        if number % i ==0:
            return False
        return True
    number=int(input("enter a number:"))
    
#if is_prime(number):
 
  #print("num is prime")
#else:
    print("is not prime")