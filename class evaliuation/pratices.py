# #import math
# #print(math.pi)

# #if 6>=5:
#     #print("6 is greater than 5"),
# #for x in range(5): print(9)
 
# #x=5
# #y="hello"
# #print(type(x))
# #print(type(y))
# """"
# x=True
# y=None
# print(type(True))
# print(type(None))
# x=5
# y=3
# print(5+3)


# my_name="Joy"
# greeting="hello"
# print(greeting + my_name)

# def greet(name):
#     print(" hello", "Joy")
# greet("name")
 

Number_list=(1, 2, 3, 4, 5 ,6 ,7 ,8, 9, 10)
print(Number_list[0])
Number_tuple=(1, 2, 3 ,4, 5, 6, 7, 8, 9, 10)
print(Number_tuple)

# def course_mate_name():
#     course_mate_name=input("enter your name:")

#     print(f'Course_mate_name : {course_mate_name.title()}')
# course_mate_name()

# my_dictionary={"name": "john", "age":30}
# print(my_dictionary["age"])


#list
# numbers = [1, 2, "three", 4, 5, 6, True]
# # print(numbers)


# print(numbers[0])
# numbers[0] = 9
# print(numbers)

# #tuple
# numbers_tuple = (1, 2, "three", 4)
# print(numbers_tuple)

# my_set = (1 , 2, 3)
# result=''.join(map(str, my_set))
# print(result)

# my_set = (1 , 2, 3)
#result=(my_set)
#print(*my_set)
for my_set in reversed(range(1,11)):
 print(my_set)
for my_set in range(1,5):
    print(1,5)
for my_set in reversed(range(1,11)):
     print(my_set)


# for number in range(1,11):
#     print(f"the number is {number}")
    
#for i in my_set:
#   print(i)

#for z in numbers:
#    print(z)


#def addition(a,b):
#    return a+b

#added_number = addition(10,5)
#print(added_number)

#syntax of for loop
#for variables in "sequence":
 #agrument1:
 #agrument2:
 #agrument3:


# name_of_student=["Enoch","Joy","peace","samson","dami"]

# #for variable in sequence:
# for student in name_of_student:
#     print(f"Student name is {student}")
#     print(f"{student} got a grade of 70")
# print("End of first loop, Thanks for checking out my software")

# #for variable in seqeunce:
# for even_number in range(2,101,2):
#     print(f"{even_number} is an even number")
# print("End of second loop,Thanks for checking my software")

#syntax of range
#range("stop")
#range("start","stop")
#range("start","stop",","step".)

# for i in range(5):
#     print(i)
# print("=============================")
# for i in range(2,5):
#     print(i)
      
# print("====================")
# for i in range(0,100,10):
#     print(i)
# count =0   # 0 < > <= >=
# while count<5:  cc
#     print(count)
#     count +=1 #count= count+=1 count = count + 1 count -= 1; count = count - 1

    #Another use case of augmented operator is -count -=1 #count =count-1

# if count < 5:
#     print(count)
#     count += 1
#     print(count)



#infinate loop this can b
#count=1
#while count>0:
    #print(f"counting {count}")
   # count+=1


# dozen=0
# count=1
# while count<20:
#      print(f"counting  {count}") 
#      if count% 12 ==0:
#          print(f"We have {dozen}  dozen of product")
#          dozen+=1
#    count+=1

#import math
#print(math)
#step=range(1,20,2)
#for a in range(1,20,2):
#    print(step)

# for i in range(1,10):
#     print(f"student number{i}")
#     if i ==5:
#         breaks



#pass this can be define as a keyword is to execute nothing or it stand as nothing
    #it can be use as a placeholder but not reguate

for i in range(1,10):
    # print(f"studentnumber{i}):
    if i==5:
        continue
    print(f"studentnumber{i}")

for i in range (1,10):
    #print(f"studentnumber{i}):
    if i==5:
        pass

        