#write a python program to determined the perfromance of a student at college
#Ask the necessary infromantion from the student

#And write userfriendly sentences
def student_detail():
    student_first_name=input("enter your first name:")
    student_last_name=input("enter your last name:")
    student_gender=input("enter your gender:")
    student_seat_number=input("enter your seat number:")
    student_exam_number=input("enter your exam number:")
student_detail()
def student_subject( ):
    user_score_in_English=int(input("enter your score for English:"))
    if user_score_in_English>=70:
       print("A - Excellent result")
    else:
        print("B-good result")
    user_score_in_Math=int(input("enter your score for Math:"))
    if user_score_in_Math>=80:
        print("A-Excellent result")
    else:
        print("B-good result")
    user_score_in_Chemistry=int(input("enter your score for Chemistry:"))
    if user_score_in_Chemistry>=75:
        print("A-Excellent result")
    else:
        print("B-good result")
    user_score_in_Physics=int(input("enter your score for Physics:"))
    if user_score_in_Physics>=89:
        print("A-Excellent")
    else:
        print("C-fair")
    user_score_in_ICT=int(input("enter your score for ICT:"))
    if user_score_in_ICT<=50:
        print("F-poor")
