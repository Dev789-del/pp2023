course_list_info = []
student_list_info = []
mark_subject_single = []
#The next below line ask user to input a number that represents the quantity of student list
student_number_count = int(input("Enter a positive number: "))
answer = True
while student_number_count < 0:
    student_number_count = int(input("Please reenter the right positive number: "))
if student_number_count > 0:
    print(f"We have to fill information for {student_number_count} students")
def student_info():
    #This function ask user to input information for a specific number of students
    for i in range(student_number_count):
        student_id = str(input("Enter student's id: "))
        student_name = str(input("Enter student's name: "))
        student_DateOfBirth = str(input(f"Enter student's date of birth: "))
        student_list_info.append(student_id)
        student_list_info.append(student_name)
        student_list_info.append(student_DateOfBirth)
    return student_list_info
print(f"Here is the information of student list after input from user: {student_info()}")
def course_info():
    #This function ask user to input information for course information
    course_number = int(input("Enter a number of course which are positive: "))
    while course_number < 0: 
        course_number = int(input("Please reenter the valid POSITIVE number!: "))
    if course_number > 0:
        print("Congratulations!You enter the valid number!")
        print(f"We need to fill information for {course_number} courses")
    for j in range(course_number):
        course_id = str(input("Enter course's id: "))
        course_name = str(input("Enter course's name: "))
        course_list_info.append(course_id)
        course_list_info.append(course_name)
    return course_list_info
print(f"Here is the course list's information after receiving content from user: {course_info()}")
def mark_subject():
    #Here is the function to input mark for student 
    course_check = str(input("Please enter course's id/course's name to fill mark: "))
    while course_check not in course_list_info:
        course_check = str(input("Please reenter the valid course's id/course's name in course list info: "))
    if course_check in course_list_info:
        print("You enter the right course's id.Please continue.")
        mark_subject_single.append(course_check)
    student_check = str(input("Please enter student's id or student's name to check if it exists: "))
    while student_check not in student_list_info:
        student_check = str(input("Please reenter student's name or id to access next step: "))
    if student_check in student_list_info:
        mark_subject_single.append(student_check)
    mark_student = float(input("Please input positive mark for subject: "))
    while mark_student < 0:
        mark_student = float(input("Please reenter the right positive number for subject's mark: "))
    if mark_student > 0:
        mark_subject_single.append(mark_student)
    return mark_subject_single    
print(f"Here is the final result of course: {mark_subject()}")