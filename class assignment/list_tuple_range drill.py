#on list tuple and range write out real life scenarios for each of them.
#And use for loop for each of them.

list()
shopping_list=["milk" ,"eggs","bread"]
for item in shopping_list:
    print(f"buy{item}")
    print(f"{item} totally cost 456")
    print(f"{shopping_list} all together totally cost ")

student_name=["joy", "anna" ,"sam"]
for student in student_name:
    print(f"Hello,{student}")
    print(f"{student} is very good in class")

product_checking=["samsung","iphone","tenco"]
for product in product_checking:
    print(f"{product} is a great phone")
    print(f"{product} cost 100000k")

favourite_food=["rice","bread","egg"]
for food in favourite_food:
    print(f"{food} is my best food")

subject_in_class=["chemisty","math","ict"]
for subject in subject_in_class:
    print(f"{subject} is my best subject")

tuple()
favourite_food=("pizza","bread", "egg")
for food in favourite_food:
   print(f"{food} is my best food")

game_score=("player1" ,"player2")
for score in game_score:
    print(f"{score} won 445 points")

car_information=("toyota","corolla",2024)
for information in car_information:
    print(f"{information} is the best car information of the year")

phone_information=("tenco", "64gb ram")
for information in phone_information:
    print({information})

address=("123 peace st", "adetown")
for  address in address:
    print(address)



for page in range(1, 100):
    print(page)
print("end of first loop thanks for checking my software")
for agegroup in range(34,67,2):
    print(agegroup)
print("end of second loop thanks for checking my software")
for examgrade in range(65,70,2):
    print(examgrade)
print("end of third loop thanks for checking my software ")
for studentnumber in range(45,56,6):
    print(studentnumber)
print("end of fourth loop thanks for checking my sofware")
for even_number in range (2,56,8):
    print(f"{even_number} is an even number")
print("end of fifth loop thanks for checking my software")
    


student_name=("joy","john","ade")
grade_score=(80,34,67)
grades = list(zip(student_name, grade_score))
#print=''.join(grades)
print(f"{student_name[0]} got {grade_score[0]} score")
print(f"{student_name[1]} got {grade_score[1]} score")
print(f"{student_name[2]} got {grade_score[2]} score")
# for grade in grade_score:
#     for name in student_name:
#         print(f"{name} grade is {grade}")
# print(grades[0])
# for i in range(3):
#     print(i)
#     print(f"{student_name[i]} grade is {grade_score[i]}")
#     i += 1

#for result in grades:
#    print(f"{result[0]} score is {result[1]}")


def passive():
    pass
