#attendence of student
#writing a python project whereby creating the a dictionary of each student 
#searching for a particular student in a list
#if name found print the things that associate with that particular student and import a module called datetime
# To record the searching and give the hour,year,mintues,seconds of searching it.
import datetime  #importing time module to record the start time and the end time of searching the student record.
print("\nWelcome to a Attendence reportsheet")
#Creating a dictionary for each of the student
student_joy={
    "name":"Joy",
    "class": "Physics",
    "Department":"Science",
    "School":"Sunshine High School",
    "Attendance":120
}


student_peace={
    "name":"Peace",
    "class": "Business",
    "Department":"Commerce",
    "School":"Townsend College",
    "Attendance":70
}

student_john={
    "name":"John",
    "class": "English",
    "Department":"Art",
    "School":"Rivers highschool",
    "Attendance":80
}

student_alice={
    "name":"Alice",
    "class": "Computer",
    "Department":"Ict",
    "School":"Hilltop school",
    "Attendance":90
}
#Total attendence mark for the student
max_attendence=120
#Storing the names of the student in a list
records=[student_joy,student_peace,student_john,student_alice]
name=input("enter your name:  ")# asking the student to input their name
found=False
#Acessing the student name, if the student name is part of the of the dictionary above
for record in records:
    if name==record.get("name"):
        found=True #if it's part of the dictionary print found and access the things that are relating to the student
        now=datetime.datetime.now() #using datetimes to record the research of the student
        print(now)
        print("name found")
        print("-------------")
        print("\nStudent summary")
        print(record.get("name"))
        print(record.get("class"))
        print(record.get("Department"))
        print(record.get("School"))
        attendance=record.get("Attendance")
        print(attendance)
# grading the attendance of the student base on their attendence mark
        if attendance < max_attendence:
            print("Not punctual")
        else:
            print("punctual")
    
        break     

if found !=True: #if the name is not part of the dictionary above print not found
    print("name not found")



















