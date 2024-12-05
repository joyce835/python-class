#write a python program to determined the perfromance of a student at college
#Ask the necessary infromantion from the student

#And write userfriendly sentences
def student_detail():
    student_first_name=input("enter your first name:")
    student_last_name=input("enter your last name:")
    student_full_name= student_first_name + " " + student_last_name 
    student_gender=input("enter your gender:")
    student_seat_number=input("enter your seat number:")
    student_exam_number=input("enter your exam number:")
    print(f'Full name : {student_full_name}')
    print(student_gender)
    print(student_seat_number)
    print(student_exam_number)

student_detail()
def student_detail():
    user_score_in_English=int(input("enter your score for English:"))
    if user_score_in_English>=70 :
       print("A - Excellent result")
    elif  user_score_in_English <69 and user_score_in_English>=60:
        print("B-good result")
    elif user_score_in_English <59 and user_score_in_English >=50:
        print("C-cerdit result")
    elif user_score_in_English <49 and user_score_in_English >=40:
        print("D-fair result")
    elif user_score_in_English <39 and user_score_in_English >=30:
        print("E-pass result")
    else:
        print("FAIL")
    
    user_score_in_Math=int(input("enter your score for Math:"))
    if user_score_in_Math>=70:
        print("A-Excellent result")
    elif user_score_in_Math <69 and user_score_in_Math >=60:
       print("B-good result")
    elif user_score_in_Math <59 and user_score_in_Math >=50:
        print("C-cerdit result")
    elif user_score_in_Math <49 and user_score_in_Math >=40:
        print("D-fair result")
    elif user_score_in_Math <39 and user_score_in_Math >= 30:
        print("E-pass result")
    else:
        print("FAIL")

    user_score_in_Chemistry=int(input("enter your score for Chemistry:"))
    if user_score_in_Chemistry>=70:
        print("A-Excellent result")
    elif user_score_in_Chemistry <69 and user_score_in_Chemistry >=60:
       print("B-good result")
    elif user_score_in_Chemistry <59 and user_score_in_Chemistry >=50:
        print("C-cerdit result")
    elif user_score_in_Chemistry <49 and user_score_in_Chemistry >=40:
        print("D-fair result")
    elif user_score_in_Chemistry <39 and user_score_in_Chemistry >=30:
        print("E-pass result")
    else:
        print("FAIL")
    
    user_score_in_Physics=int(input("enter your score for Physics:"))
    if user_score_in_Physics>=70:
        print("A-Excellent result")
    elif user_score_in_Physics <69 and user_score_in_Physics >=60:
       print("B-good result")
    elif user_score_in_Physics <59 and user_score_in_Physics >=50:
        print("C-cerdit result")
    elif user_score_in_Physics <49 and user_score_in_Physics >=40:
        print("D-fair result")
    elif user_score_in_Physics <39 and user_score_in_Physics >=30:
        print("E-pass result")
    else:
        print("FAIL")
    
    user_score_in_ICT=int(input("enter your score for ICT:"))
    if user_score_in_ICT>=70:
        print("A-Excellent result")
    elif user_score_in_ICT <69 and user_score_in_ICT >=60:
       print("B-good result")
    elif user_score_in_ICT <59 and user_score_in_ICT >=50:
        print("C-cerdit result")
    elif user_score_in_ICT <49 and user_score_in_ICT >=40:
        print("D-fair result")
    elif user_score_in_ICT <39 and user_score_in_ICT >=30:
        print("E-pass result")
    else:
        print("FAIL")
    return student_detail()
    
def grade_calculation():
    #cumulative_grade = user_score_in_English + user_score_in_Math + user_score_in_Chemistry + user_score_in_Physics + user_score_in_ICT
    number_of_subjects = 5
    #Average_score = cumulative_grade/number_of_subjects
    #print(Average_score)
    #if Average_score >=50:
      # print("pass")
