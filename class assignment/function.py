#def name_department(name, department):
  #statement = ('You are welcome ' + str(name) + " \nThe " + str(department) + " department welcomes you to Linar ")
  #print (statement)
#name_department("Joy", " Python")
#name_department ("Peace", " 3D Animation")
#name_department ('Enoch', 'Web development')
#name_department ('Samson', 'ICT Fundamentals')

#Ask or create a function to determine student details: first name, last name, school name, exam number and seat number
def student_details(fname, lname, examno, seatno, gender, school):
  statement1 = (f'EXAM REPORT SHEET \n Student Name:{fname} {lname} \n Exam Number: {examno}\n Seat No: {seatno} \n Gender: {gender} \n School: {school}')
  return statement1
print(student_details(" Ali", 'Baba', 454, 913, "Male", "Linar" )) #Arg/para
# Determine 5 subject grading
English = int(input("Enter English Score: "))
Maths = int(input("Enter Maths Score: "))
Physics = int(input("Enter Physics Score: "))
Chemistry = int(input("Enter Chemistry Score: "))
ICT = int(input("Enter ICT Score: "))

if English >= 70:
  print (f'English:{English} Grade: A-Excellent!')
elif English <70 and English >= 60:
    print (f'English:{English} Grade: B- Very Good!')
elif English <60 and English >=50:
    print (f'English:{English} Grade: C- Good!') 
elif English <50 and English >=40:
    print (f'English:{English} Grade: D- Poor!') 
elif English <40 and English >=0:
    print (f'English:{English} Grade: F- Fail!') 
if Maths >= 70:
     print (f'Maths:{Maths} Grade: A-Excellent!')
elif Maths <70 and Maths >= 60:
    print (f'Maths:{Maths} Grade: B- Very Good!') 
elif Maths <60 and Maths >=50:
    print (f'Maths:{Maths} Grade: C- Good!') 
elif Maths <50 and Maths >=40:
    print (f'Maths:{Maths} Grade: D- Poor!') 
elif Maths <40 and Maths >=0:
    print (f'Maths:{Maths} Grade: F- Fail!') 
if Physics >= 70:
     print (f'Physics:{Physics} Grade: A-Excellent!')
elif Physics <70 and Physics >= 60:
    print (f'Physics:{Maths} Grade: B- Very Good!') 
elif Physics <60 and Physics >=50:
    print (f'Physics:{Maths} Grade: C- Good!') 
elif Physics <50 and Physics >=40:
    print (f'Physics:{Maths} Grade: D- Poor!') 
elif Physics <40 and Physics >=0:
    print (f'Physics:{Maths} Grade: F- Fail!') 
if Chemistry >= 70:
    print (f'Chemistry:{Chemistry} Grade: A-Excellent!')
elif Chemistry <70 and Chemistry >= 60:
    print (f'Chemistry:{Chemistry} Grade: B- Very Good!')
elif Chemistry <60 and Chemistry >=50:
    print (f'Chemistry:{Chemistry} Grade: C- Good!') 
elif Chemistry <50 and Chemistry >=40:
    print (f'Chemistry:{Chemistry} Grade: D- Poor!') 
elif Chemistry <40 and Chemistry >=0:
    print (f'Chemistry:{Chemistry} Grade: F- Fail!')
if ICT >= 70:
    print (f'ICT:{ICT} Grade: A-Excellent!')
elif ICT <70 and ICT >= 60:
    print (f'ICT:{ICT} Grade: B- Very Good!')
elif ICT <60 and ICT >=50:
    print (f'ICT:{ICT} Grade: C- Good!') 
elif ICT <50 and ICT >=40:
    print (f'ICT:{ICT} Grade: D- Poor!') 
elif ICT <40 and ICT >=0:
    print (f'ICT:{ICT} Grade: F- Fail!') 
#determine the,cummulative score, average score and status of student as either pass or fail
totalscore = English + Maths + Physics + Chemistry + ICT
print (f'Total score is: {totalscore}')
Averagescore = totalscore / 5
print (f'Average score is: {Averagescore}')
if Averagescore >= 50:
  print ('PASS!!!')
else:
  print ('FAIL!')


  



  

  

  