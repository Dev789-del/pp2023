#define three empty database and import datetime package to show log after input information
courses_information = {}
students_information = {}
mark_subject_list = {}
import datetime
class Student_Info:
    def student_info():
        #This function ask user to input information for a specific number of students
        student_number_count = int(input("Enter a number that represent the amount of students(must be POSITIVE): "))
        while student_number_count < 0:
            student_number_count = int(input("Please reenter the right positive number of students: "))
        if student_number_count > 0:
            print(f"We have to fill information for {student_number_count} students")
        for i in range(student_number_count):
            student_ID = str(input("Enter student's ID: "))
            student_name = str(input("Enter student's name: "))
            student_DateOfBirth = str(input("Enter student's date of birth(e.g dd/mm/yy): "))
            day, month, year = student_DateOfBirth.split('/')
            Check_Valid_Date = True
            try:
                datetime.datetime(int(day), int(month), int(year))
            except ValueError:
                Check_Valid_Date = False
            while Check_Valid_Date:
                continue
            else:
                student_DateOfBirth = str(input("Enter student's date of birth with proper format(dd/mm/yy) again: "))
            students_information[student_ID] = {'Student_Name': student_name, 'Student_DateOfBirth': student_DateOfBirth}
        student_info_time = datetime.datetime.now()
        print(f"You had input information for students at {student_info_time}")
class Course_Info:
    def course_info():
        #This function ask user to input information for list of courses
        course_number_count = int(input("Enter a number of courses which are positive: "))
        while course_number_count < 0: 
            course_number_count = int(input("Please reenter the valid POSITIVE number!: "))
        if course_number_count > 0:
            print("Congratulations!You enter the correct number!")
            print(f"We need to fill information for {course_number_count} courses")
        for j in range(course_number_count):
            course_ID = str(input("Enter course's ID: "))
            course_name = str(input("Enter course's name: "))
            courses_information[course_ID] = {'Course_Name': course_name}
        course_info_time = datetime.datetime.now()
        print(f"You had input information for courses at {course_info_time}")
class Mark_Info:
    def mark_subject():
        #Here is the function to input mark for students
        course_check = str(input("Please enter course's ID to fill mark: "))
        while course_check not in courses_information:
            course_check = str(input("Please reenter the correct course's ID in course list's information: "))
        if course_check in courses_information:
            print("You enter the correct course's ID.")
        for student_ID in students_information:
            mark_student = float(input(f"Enter mark for student {students_information[student_ID]['Student_Name']}: "))
            while mark_student < 0.0 and mark_student > 20.0:
                mark_student = float(input(f"You need to enter the mark again for student {students_information[student_ID]['Student_Name']}: "))
            else: 
                if student_ID not in mark_subject_list:
                    mark_subject_list[student_ID] = {}
                    mark_subject_list[student_ID][course_check] = mark_student
        mark_subject_time = datetime.datetime.now()
        print(f"You had input information for subject mark at {mark_subject_time}")
    #Function below to display mark transcipt for students
    def mark_receive():
        course_identify = input("Enter course's ID to check: ")
        while course_identify not in courses_information:
            print("Course's ID not exist.Please enter again")
        else: 
            print("You enter the valid course's ID")
        mark_receive_time = datetime.datetime.now()
        print(f"Student Mark return at {mark_receive_time}")
        for student_ID in students_information:
            if student_ID in mark_subject_list and course_identify in mark_subject_list[student_ID]:
                print(f"----------Course {course_identify} final mark----------")
                print(f"{students_information[student_ID]['Student_Name']}: {mark_subject_list[student_ID][course_identify]}")
            else:
                print(f"{students_information[student_ID]['Student_Name']}: N/A")
#Define functions to show list of courses and list of students
def courses_list():
    courses_list_time = datetime.datetime.now()
    print(f"Here is the list of courses information after selecting option 1 at {courses_list_time}:")
    print(courses_information)
def students_list():
    students_list_time = datetime.datetime.now()
    print(f"Here is the list of students information after selecting option 2 at {students_list_time}:")
    print(students_information)
#Executing student_info and course_info functions
Student_Info.student_info()
Course_Info.course_info()
#While loop to show list of choices
Condition = True
while Condition:
    print("----------Welcome to Student Management System----------")
    print("Here is your list of choices:")
    print("1.Show list of courses")
    print("2.Show list of students")
    print("3.Input student's result of courses")
    print("4.Show final mark of all students")
    print("5.Exit system")
    option = int(input("Choose your option number: "))
    if option == 1:
        courses_list()
    elif option == 2:
        students_list()
    elif option == 3:
        Mark_Info.mark_subject()
    elif option == 4:
        Mark_Info.mark_receive()
    elif option == 5:
        break
    else:
        print("You choose the wrong choice.You need to enter the number again.")