#write a function total_cost(price,tax_rate)that calulate that total cost of a items including tax
#Tax is 6.5%

def total_cost(price,tax_rate):
    subtotal=sum(price)
    tax= subtotal * tax_rate
    total=subtotal +tax
price = [float(x) for x in input("enter prices(separated by space):"). split()]
tax_rate=float(input("enter tax rate (in decimal form, e.g 0.065):"))
result=total_cost(price,tax_rate)
print("Total cost:", result)
