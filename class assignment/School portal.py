
# Create a school portal for checking students grades asking for student details and making it user friendly
Is_user_a_student_of_this_school = str(input("Are you a student of this school input 'yes' or 'no' : "))
if Is_user_a_student_of_this_school.upper() == "YES":
    print("PORTAL LOADING !!! " * 3)
elif Is_user_a_student_of_this_school.upper() == "NO":
    print("Exiting...")
    exit()

    

def student_details():
    student_first_name = input('Input your first name : ')
    student_last_name = input('Input your last name : ')
    student_full_name = student_first_name.title() + " " + student_last_name.title()
    student_school = input("Enter school name : ")
    student_gender = input("Enter your gender (Male or Female) : ")
    student_exam_number = input(f"{student_full_name}, Please enter your registration/exam number : ")
    student_seat_number = input("Enter your seat number : ")
    print()
    print()
    print()
    print(f'Fullname : {student_full_name.title()}')
    print(f'SCHOOL NAME : {student_school.title()}')
    print(f'Gender : {student_gender.title()}')
    print(f'Exam/registration number : {student_exam_number}')
    print(f"Seat number : seat number {student_seat_number}")

def grade_calculation():
    print("The score inputed is from a scale of 1 - 100 !!!")
    English = int(input("Input your english score : "))
    Mathematics = int(input("Input your Mathematics score : "))
    Physics = int(input("Input your Physics score : "))
    Chemistry = int(input("Input your Chemistry score : "))
    ICT = int(input("Input your ICT score : "))
    subject_and_grade = {"English":English , "Mathematics":Mathematics, "Physics":Physics,"Chemistry":Chemistry,"ICT":ICT}
    
    print()
    print()
    print()
    print(f"Subjects: \n {subject_and_grade}")
    pass_mark = 50
    import math
    Cummulative_score = sum(subject_and_grade.values())
    number_of_subjects = len(subject_and_grade.values())
    Average_score = Cummulative_score/number_of_subjects
    print(f'your cummulative average grade score is {Average_score}')
    
    
    if Average_score>= 50 :
        print(f'Status : Pass !!!')
    elif Average_score< 50 :
        print(f'Status : Fail ')

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

        
student_details()
grade_calculation()




user_try_again = str(input("Do you want to check your score again (yes or no) ? "))
user_trial = 0
max_trial = 5
while user_trial<max_trial:
    if user_try_again.title() == "Yes":
        user_try_again
    user_trial+=1
    print(f'You have {max_trial - user_trial} trials left !!!')
    
    if user_try_again.title() == "No":
        print("Thank you!!")
        exit()

    if user_trial == max_trial:
        print("You've exceeded your maximum trial\n rerun to use portal !!")
        print("LOGGING OUT !!!")
        exit()
# Created by dami and enoch...
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


    