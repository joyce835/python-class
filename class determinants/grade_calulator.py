#grade calulator
#writing a python project whereby calulating the grade marks of a student.
#and grading the marks of the student

name_of_student=input("enter your name:")
name_of_school=input("enter the name of your school:")
name_of_class=input("enter the name of your class:")

def grade_calulator(marks):
    marks=int(input("enter your marks:"))
    if marks >= 90:
        print("A excellent")
    elif marks <= 89 and marks >=80:
        print("B Good  ")
    elif marks <= 79 and marks >=70:
         print("c credit")
    elif marks <=69 and marks >=60:
        print("D pass")
    else:
        print("F fail")
print(grade_calulator(f"your grade is: "))





