#attendence of student
#writing a python project whereby writing the number of times a student was present or absent
#calulating the attendence report sheet by using the offical attendence mark
#and grade the student by the number of times the student was present or absent.

name=["joy","peace","john","alice"]
name_of_student=input("enter your name:")
if name_of_student in name:
        print("Student name found!")
elif name_of_student not in name:
        print("student name is not found!")
        exit()
else:
     print("error")

name_of_class=input("enter the name of your class:")
student_school=input("enter the name of school")


offical_attendence_mark=120
student_times_absent=int(input("enter the number of times absent:"))
student_times_present = offical_attendence_mark - student_times_absent
print (f'Total attendance is 120 \n Your total attendance present is {student_times_present} days')

if student_times_present == 120:
       print("promoted")
elif student_times_present<= 119 and student_times_present >=60:
       print("can still be promoted")
elif student_times_present <= 59 and student_times_present>=30:
       print("can still be considered")
elif student_times_present <= 29 and student_times_present >=10:
       print("Attendance too poor for promotion")
else:
       print("repeat class")
        




