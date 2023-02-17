#define three empty database
courses_information = {}
students_information = {}
mark_subject_list = {}

def student_info():
    #This function ask user to input information for a specific number of students
    student_number_count = int(input("Enter a number that represent the amount of students(must be POSITIVE): "))
    answer = True
    while student_number_count < 0:
        student_number_count = int(input("Please reenter the right positive number of students: "))
    if student_number_count > 0:
        print(f"We have to fill information for {student_number_count} students")
    for i in range(student_number_count):
        student_id = str(input("Enter student's id: "))
        student_name = str(input("Enter student's name: "))
        student_DateOfBirth = str(input(f"Enter student's date of birth: "))
        students_information[student_id] = {'Student_Name"=': student_name, 'Student_DateOfBirth': student_DateOfBirth}

def course_info():
    #This function ask user to input information for course information
    course_number = int(input("Enter a number of courses which are positive: "))
    while course_number < 0: 
        course_number = int(input("Please reenter the valid POSITIVE number!: "))
    if course_number > 0:
        print("Congratulations!You enter the valid number!")
        print(f"We need to fill information for {course_number} courses")
    for j in range(course_number):
        course_id = str(input("Enter course's id: "))
        course_name = str(input("Enter course's name: "))
        courses_information[course_id] = {'Course_Name': course_name}

def mark_subject():
    #Here is the function to input mark for student 
    course_check = str(input("Please enter course's id/course's name to fill mark: "))
    while course_check not in courses_information:
        course_check = str(input("Please reenter the valid course's id/course's name in course list info: "))
    if course_check in courses_information:
        print("You enter the right course's id.Please continue.")
    for student_id in students_information:
        mark_student = float(input(f"Enter marks for student: {mark_student}"))
        while mark_student < 0 and mark_student > 20:
            mark_student = float(input(f"You need to enter the mark again: {mark_student}"))
        else: 
            if student_id not in mark_subject_list:
                mark_subject_list[student_id] = {}
            mark_subject_list[student_id][course_check] = mark_subject_list

#Define functions to show list of courses and list of students
def courses_list():
    print("Here is the list of courses information")
    print(courses_information)
def students_list():
    print("Below is the list of students information")
    print(students_information)

#Function below to present mark transcipt for student
def mark_receive():
    course_identify = input("Enter course ID/course name to check: ")
    while course_identify not in courses_information:
        print("Course ID/Course name not exist.Please enter again")
    else: 
        print("You enter the valid input")
    for student_id in students_information:
        if student_id in mark_subject_list and course_identify in mark_subject_list[student_id]:
            print(f"{students_information[student_id]['Student_Name']}: {mark_subject_list[student_id][course_identify]}")
        else:
            print(f"{students_information[student_id]['Student_Name']}: N/A")

#While loop to show list of choices
student_info()
course_info()
Condition = True
while Condition:
    print("----------Student Management System welcome users----------")
    print("Here is your list of choices:")
    print("1.Show list of courses")
    print("2.Show list of students")
    print("3.Input student's result of courses")
    print("4.Show final result of courses")
    print("5.Exit system")
    option = int(input("Choose your option number: "))
    if option == 1:
        courses_list()
    elif option == 2:
        students_list()
    elif option == 3:
        mark_subject()
    elif option == 4:
        mark_receive()
    elif option == 5:
        break
    else:
        print("Invalid choice.You need to enter again.")