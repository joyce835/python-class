def grade(subject):
    if subject >= 70:
        return "A"
    elif subject <=69:
        return "B"
    elif subject <=59:
        return "C"
    elif subject <=49:
        return "D"
    elif subject <=39:
        return "E"
    else:
        return "F"
    

question = input(f"statement of result(yes or no):")

if question == "yes":
    student_first_name=input("enter your first name:")
    student_last_name=input("enter your last name:")
    student_full_name= student_first_name.title() + " " + student_last_name.title()
    student_school=input("enter your school name: ")
    student_gender=input("enter your gender:")
    student_seat_number=input("enter your seat number:")
    student_exam_number=input("enter your exam number:")

    user_score_in_English=int(input("enter your score for English:"))
    user_score_in_Math=int(input("enter your score for Math:"))
    user_score_in_Chemistry=int(input("enter your score for Chemistry:"))
    user_score_in_Physics=int(input("enter your score for Physics:"))
    user_score_in_ICT=int(input("enter your score for ICT:"))

    English_grade = grade(user_score_in_English)
    Math_grade = grade(user_score_in_Math)
    Chemistry = grade(user_score_in_Chemistry)
    Physics = grade(user_score_in_Physics)
    ICT = grade(user_score_in_ICT)

elif question == "no":
    print("no")  #print(ok)


def grade_calculation():
    cumulative_grade = user_score_in_English + user_score_in_Math + user_score_in_Chemistry + user_score_in_Physics + user_score_in_ICT
    number_of_subjects=5
    Average_score=cumulative_grade/number_of_subjects
    if Average_score >=50:
      print(f"Status : pass")
    elif Average_score< 50 :
        print("Status : Fail")
    print(f'Your average score is {Average_score}')
    print(f"""
        This is to inform you that {student_full_name} a student of {student_school} with the examination number {student_exam_number}
        and seat number {student_seat_number} successfully wrote this exam at {student_school} 
        Below is the result summary: \n
    
        English - {user_score_in_English} - {English_grade} 
        Mathematics - {user_score_in_Math} - {Math_grade} 
        Physics - {user_score_in_Physics} - {Physics} 
        Chemistry - {user_score_in_Chemistry} - {Chemistry} 
        ICT - {user_score_in_ICT} - {ICT} 
        Average_score -{Average_score} 
        Thank you 
        Signed by {student_school} 
        Designed by Joy
        """)
grade_calculation()


        # elif:
        # print("no")

#  print("yes")
