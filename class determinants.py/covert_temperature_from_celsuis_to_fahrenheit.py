#write a fucntion celsuis to fahrenheit(celsius) that's coverts the temperture from  celsuis to fahrenheit

def celsius_to_fahrenheit(celsius):
    return(celsius * 9/5)+32
celsius=float(input("enter temperature in celsuis:"))
print("temperature in fahrenheit:",celsius_to_fahrenheit(celsius))