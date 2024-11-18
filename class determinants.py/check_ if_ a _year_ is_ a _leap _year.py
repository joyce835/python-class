# write a function is leap year (year)
#that check if a year is a leap year

def is_leap_year(year):
    return year %4 ==0 and (year % 100 !=0 or year %400==0 )
year=int(input("enter your year:"))
print(is_leap_year(year))
#output:2024
#true