#write a function find_smallest(numbers) that returns the smallest element in a list
def find_smallest():
  numbers=input("enter numbers sparated by space:") 
  number= [int(num) for num in number.split()] 
  return min(numbers)
print(find_smallest())