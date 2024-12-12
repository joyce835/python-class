
#write a python program to determined the performance of a student at college

#Ask the necessary information from the student

#And write userfriendly sentences
def student_detail():
    student_first_name=input("enter your first name:")
    student_last_name=input("enter your last name:")
    student_full_name= student_first_name.title() + " " + student_last_name.title()
    student_school=input("enter your school name: ")
    student_gender=input("enter your gender:")
    student_seat_number=input("enter your seat number:")
    student_exam_number=input("enter your exam number:")
    print(f'Full name : {student_full_name}')
    print(f'Gender : {student_gender.title()}')
    print(f"Seat number : Seat number {student_seat_number}")
    print(f'Student exam number : {student_exam_number}')
    print(f'Student school":{student_school.title()}')
student_detail()

user_score_in_English=int(input("enter your score for English:"))
user_score_in_Math=int(input("enter your score for Math:"))
user_score_in_Chemistry=int(input("enter your score for Chemistry:"))
user_score_in_Physics=int(input("enter your score for Physics:"))
user_score_in_ICT=int(input("enter your score for ICT:"))
def English():
    #user_score_in_English=int(input("enter your score for English:"))
    if user_score_in_English>=70 :
       print("A - Excellent result")
    elif  user_score_in_English <=69 and user_score_in_English>=60:
        print("B-good result")
    elif user_score_in_English <=59 and user_score_in_English >=50:
        print("C-cerdit result")
    elif user_score_in_English <=49 and user_score_in_English >=40:
        print("D-fair result")
    elif user_score_in_English <=39 and user_score_in_English >=30:
        print("E-pass result")
    else:
        print("F-fail")
def Maths():
    
    if user_score_in_Math>=70:
        print("A-Excellent result")
    elif user_score_in_Math <=69 and user_score_in_Math >=60:
       print("B-good result")
    elif user_score_in_Math <=59 and user_score_in_Math >=50:
        print("C-cerdit result")
    elif user_score_in_Math <=49 and user_score_in_Math >=40:
        print("D-fair result")
    elif user_score_in_Math <=39 and user_score_in_Math >= 30:
        print("E-pass result")
    else:
        print("F-fail")
def Chemistry():
    #user_score_in_Chemistry=int(input("enter your score for Chemistry:"))
    if user_score_in_Chemistry>=70:
        print("A-Excellent result")
    elif user_score_in_Chemistry <=69 and user_score_in_Chemistry >=60:
       print("B-good result")
    elif user_score_in_Chemistry <=59 and user_score_in_Chemistry >=50:
        print("C-cerdit result")
    elif user_score_in_Chemistry <=49 and user_score_in_Chemistry >=40:
        print("D-fair result")
    elif user_score_in_Chemistry <=39 and user_score_in_Chemistry >=30:
        print("E-pass result")
    else:
        print("F-fail")
def Physics():
    #user_score_in_Physics=int(input("enter your score for Physics:"))
    if user_score_in_Physics>=70:
        print("A-Excellent result")
    elif user_score_in_Physics <=69 and user_score_in_Physics >=60:
       print("B-good result")
    elif user_score_in_Physics <=59 and user_score_in_Physics >=50:
        print("C-cerdit result")
    elif user_score_in_Physics <=49 and user_score_in_Physics >=40:
        print("D-fair result")
    elif user_score_in_Physics <=39 and user_score_in_Physics >=30:
        print("E-pass result")
    else:
        print("F-fail")
def ICT():  
    #user_score_in_ICT=int(input("enter your score for ICT:"))
    if user_score_in_ICT>=70:
        print("A-Excellent result")
    elif user_score_in_ICT <=69 and user_score_in_ICT >=60:
       print("B-good result")
    elif user_score_in_ICT <=59 and user_score_in_ICT >=50:
        print("C-cerdit result")
    elif user_score_in_ICT <=49 and user_score_in_ICT >=40:
        print("D-fair result")
    elif user_score_in_ICT <=+39 and user_score_in_ICT >=30:
        print("E-pass result")
    else:
        print("F-Fail")
def grade_calculation():
    cumulative_grade = user_score_in_English + user_score_in_Math + user_score_in_Chemistry + user_score_in_Physics + user_score_in_ICT
    number_of_subjects = 5
    Average_score = cumulative_grade/number_of_subjects
    Grade_remark = {"English":English(), "Maths": Maths(), "Physics": Physics(), "Chemistry":Chemistry(), "ICT":ICT()}
    #print(f"Grade Remark \n {Grade_remark}")
    print(f'Your average score is {Average_score}')
    if Average_score >=50:
      print(f"Status : pass")
    elif Average_score< 50 :
        print("Status : Fail")
        #     #def grade(subject):
#     #if subject >= 70:
#         return "A"
#     #elif subject <=69:
#         return "B"
#     elif subject <=59:
#         return "C"
#     elif subject <=49:
#         return "D"
#     elif subject <=39:
#         return "E"
#     else:
#         return "F"
    

# question = input(f"statement of result(yes or no):")


# if question == "yes":
#     student_first_name=input("enter your first name:")
#     student_last_name=input("enter your last name:")
#     student_full_name= student_first_name.title() + " " + student_last_name.title()
#     student_school=input("enter your school name: ")
#     student_gender=input("enter your gender:")
#     student_seat_number=input("enter your seat number:")
#     student_exam_number=input("enter your exam number:")

#     user_score_in_English=int(input("enter your score for English:"))
#     user_score_in_Math=int(input("enter your score for Math:"))
#     user_score_in_Chemistry=int(input("enter your score for Chemistry:"))
#     user_score_in_Physics=int(input("enter your score for Physics:"))
#     user_score_in_ICT=int(input("enter your score for ICT:"))

#     English_grade = grade(user_score_in_English)
#     Math_grade = grade(user_score_in_Math)
#     Chemistry = grade(user_score_in_Chemistry)
#     Physics = grade(user_score_in_Physics)
#     ICT = grade(user_score_in_ICT)

# elif question == "no":
#     print("ok")  #print(no)


# def grade_calculation():
#     cumulative_grade = user_score_in_English + user_score_in_Math + user_score_in_Chemistry + user_score_in_Physics + user_score_in_ICT
#     number_of_subjects=5
#     Average_score=cumulative_grade/number_of_subjects
#     if Average_score >=50:
#       print(f"Status : pass")
#     elif Average_score< 50 :
#         print("Status : Fail")
#     print(f'Your average score is {Average_score}')
#     print(f"""
#         This is to inform you that {student_full_name} a student of {student_school} with the examination number {student_exam_number}
#         and seat number {student_seat_number} successfully wrote this exam at {student_school} 
#         Below is the result summary: \n
    
#         English - {user_score_in_English} - {English_grade} 
#         Mathematics - {user_score_in_Math} - {Math_grade} 
#         Physics - {user_score_in_Physics} - {Physics} 
#         Chemistry - {user_score_in_Chemistry} - {Chemistry} 
#         ICT - {user_score_in_ICT} - {ICT} 
#         Average_score -{grade_calculation}
#         Thank you 
#         Signed by {student_school} 
#         Designed by Joy
#         """)
# grade_calculation()


        # elif:
        # print("no")

#  print("yes")
grade_calculation()





