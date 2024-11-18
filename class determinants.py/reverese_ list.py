#write a function reverse list that reversed the order of elements in a list

def reverse_list(numbers):
    number=input("enter numbers separated by space:")
    spacing=[int(num) for num in number.split()]
print(reverse_list([1,2,3,4,5]))

#output[5, 4 ,3 ,2 ,1]