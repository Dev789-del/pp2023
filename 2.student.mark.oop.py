#import datetime package to show log after input information
courses_information = {}
students_information = {}
mark_subject_list = {}
import datetime
class StudentINFO:
    def __init__(self):
        #This function set student number to 0 and initialize an empty list of students_information
        self.__student_number = 0
    def get_number_of_students(self):
        return self.__student_number
    def set_number_of_students(self, student_number_count):
        self.__student_number = student_number_count
    def input_number_students(self):
        #This function ask user for input a number
        self.student_number_count = int(input("Enter a number that represent the amount of students(must be POSITIVE!): "))
        while self.student_number_count < 0:
            self.student_number_count = int(input("Please reenter the right positive number of students: "))
        if self.student_number_count > 0:
            print(f"We have to fill information for {self.student_number_count} students")
        return self.student_number_count
    def student_info(self):
        #This function ask user to input information for a specific number of students
        for i in range(self.input_number_students()):
            student_ID = str(input("Enter student's ID: "))
            student_name = str(input("Enter student's name: "))
            student_DateOfBirth = str(input("Enter student's date of birth(dd/mm/yy): "))
            students_information[student_ID] = {'Student_Name': student_name, 'Student_DateOfBirth': student_DateOfBirth}
        student_info_time = datetime.datetime.now()
        print(f"You had input information for students at {student_info_time}")
    def students_list():
        #This function show the list of students
        if len(students_information) == 0:
            print("Empty students list!")
        else:
            students_list_time = datetime.datetime.now()
            print(f"Here is the list of students information after selecting option 2 at {students_list_time}:")
            print("{:24} | {:24}".format("Student_Name", "Student_DoB"))
            spacebard = 0
            for v in students_information:
                print(f"{students_information[v]}")
                spacebard += 1
                if spacebard % 3 == 0:
                    print(f"\n{students_information[v]}")
    def get_student_list():
        return students_information
class CourseINFO:
    def __init__(self):
        self.__courses_number = 0
        self.courses_information = {}
    def get_courses_count(self):
        return self.__courses_number
    def set_courses_quantity(self, course_number_count):
        self.__courses_number = course_number_count
    def input_num_courses(self):
        self.course_number_count = int(input("Enter a number of courses which are positive: "))
        while self.course_number_count < 0: 
            self.course_number_count = int(input("Please reenter the valid POSITIVE number: "))
        if self.course_number_count > 0:
            print("Congratulations!You enter the correct number!")
            print(f"We need to fill information for {self.course_number_count} courses")
        return self.course_number_count
    def course_info(self):
        #This function ask user to input information for course list
        for j in range(self.input_num_courses()):
            course_ID = str(input("Enter course's ID: "))
            course_name = str(input("Enter course's name: "))
            courses_information[course_ID] = {'Course_Name': course_name}
        course_info_time = datetime.datetime.now()
        print(f"You had input information for courses at {course_info_time}")
    def courses_list():
        #This function show the list of courses
        courses_list_time = datetime.datetime.now()
        if len(courses_information) == 0:
            print("Empty courses list!")
        else:
            print(f"Here is the list of courses information after selecting option 1 at {courses_list_time}:")
            print(courses_information)
    def get_course_list(self):
        return self.courses_information
class Result_INFO:
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
  
#Define three custom function operator
student_info_function = StudentINFO()
course_info_function = CourseINFO()
mark_info_function = Result_INFO()
courses_information = course_info_function.get_course_list
students_information = student_info_function.get_student_list
#While loop to show list of choices
Condition = True
while Condition:
    print("----------Welcome to Student Management System----------")
    print("Here is your list of choices:")
    print("1.Add information for list of students")
    print("2.Add information for list of courses")
    print("3.Show courses information")
    print("4.Show students information")
    print("5.Add mark information")
    print("6.Show mark information")
    print("7.Exit system")
    option = int(input("Choose your option number: "))
    if option == 1:
        student_info_function.student_info()
    elif option == 2:
        course_info_function.course_info()
    elif option == 3:
        course_info_function.courses_list()
    elif option == 4:
        student_info_function.students_list()
    elif option == 5:
        mark_info_function.mark_subject()
    elif option == 6:
        mark_info_function.mark_receive()
    elif option == 7:
        break
    else:
        print("!!!You choose the wrong choice.You need to enter the number again!!!")