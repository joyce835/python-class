#calulation base on the discount on original price
#getting the original price and discount percentage from the user
original_price=int(input("enter the original price:$"))
discount_percentage=int(input("enter the discount percentage(%)"))
#calulate the discount amount
discount_amount=original_price*(discount_percentage/100)
print("discount amount:$",discount_amount)

#calulate the final price
final_price=original_price-discount_amount
print("the price of the item after the discount is:$", final_price)

