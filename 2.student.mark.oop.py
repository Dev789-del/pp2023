#define three empty database and import datetime package to show log after input information
courses_information = {}
mark_subject_list = {}
import datetime
class StudentINFO:
    def __init__(self):
        #This function set student number to 0 and initialize an empty list of students_information
        self.__student_number = 0
        self.student_information = {}
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
            self.student_information[student_ID] = {'Student_Name': student_name, 'Student_DateOfBirth': student_DateOfBirth}
        student_info_time = datetime.datetime.now()
        print(f"You had input information for students at {student_info_time}")
    def students_list(self):
        #This function show the list of students
        if len(self.student_information) == 0:
            print("Empty students list!")
        else:
            students_list_time = datetime.datetime.now()
            print(f"Here is the list of students information after selecting option 2 at {students_list_time}:")
            print("{:24} | {:24}".format("Student_Name", "Student_DoB"))
            spacebard = 0
            for v in self.student_information:
                print(f"{self.student_information[v]}")
                spacebard += 1
                if spacebard % 3 == 0:
                    print(f"\n{self.student_information[v]}")
class Course_Parameter:
    #This class make reference to specify courses_information list dictionary line 68
    def __init__(self, course_ID, course_name):
        self.course_ID = course_ID
        self.course_name = course_name
class CourseINFO:
    def __init__(self):
        self.__courses_number = 0
        self.courses_information = []
    def _get_courses_count(self):
        return self.__courses_number
    def _set_courses_quantity(self, course_number_count):
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
            course_content = Course_Parameter(course_ID, course_name)
            self.courses_information.append(course_content)
            return self.courses_information
        course_info_time = datetime.datetime.now()
        print(f"You had input information for courses at {course_info_time}")
    def courses_list(self):
        #This function show the list of courses
        courses_list_time = datetime.datetime.now()
        if len(self.courses_information) == 0:
            print("Empty courses list!")
        else:
            print(f"Here is the list of courses information after selecting option 1 at {courses_list_time}:")
            print("{:5} | {:12} | {:24}".format("Number", "Course_ID", "Course_Name"))
            for i in range(len(self.courses_information)):
                print("{:5} | {:12} | {:24}".format(str(i + 1), self.courses_information[i].course_ID, self.courses_information[i].course_name))

class Exam_Result:
    def __init__(self, course_ID, course_name, mark_input):
        self.course_ID = course_ID  
        self.course_name = course_name
        self.mark_input = mark_input   

def course_verification(courses_information):
    while len(courses_information) == 0:
        print("No course available!")
        break
    else:
        course_check = str(input("Please enter course's ID to fill mark: "))
        for i in range(len(courses_information)):
            if course_check == courses_information[i].course_ID:
                return courses_information[i]
        return "No course found!"
class Result_INFO:
    def __init__(self):
        self.mark_subject_list = {}
    def mark_subject(self, courses_information, students_information):
        #Here is the function to input mark for students
        course_checker = course_verification(courses_information)
        if course_checker == "No course found!":
            print("No course exist!")
        else: 
            result_information = []
            for i in range(len(students_information)):
                mark_input = float(input(f"Student ID: {students_information[i].student_ID} - Student Name: {students_information[i].student_name} \n Mark result: "))
                while mark_input < 0.0 and mark_input > 20.0:
                    mark_input = float(input(f"Student ID: {students_information[i].student_ID} - Student Name: {students_information[i].student_name} \n Mark result: "))
                else: 
                    mark_final_result = Exam_Result(students_information[i].student_ID, students_information[i].student_name, mark_input)
                    result_information.append(mark_final_result)
            self.mark_subject_list[course_checker.course_ID] = result_information
            return self.mark_subject_list
        mark_subject_time = datetime.datetime.now()
        print(f"You had input information for subject mark at {mark_subject_time}")

    #Function below to display mark transcipt for student
    def mark_receive(self, courses_information, students_information):
        course_check = course_verification(courses_information)
        course_result = self.mark_subject_list[course_check.course_ID]
        if course_check == "No course found":
            print("Course's ID not exist.Please enter again!")
        else: 
            print("You enter the valid course's ID!")
            mark_receive_time = datetime.datetime.now()
            print(f"Student Marks return at {mark_receive_time}")
            print(f"Course {course_check.course_name} final result:")
            print("{:5} | {:12} | {:24} | {:12}".format("Number", "Student_ID", "Student_name", "Final result"))
            if len(course_result) == 0:
                print("No mark available!")
            else:
                for i in range(len(students_information)):
                    print("{:5} | {:12} | {:24} | {:12}".format(str(i + 1), course_result[i].course_ID, course_result[i].course_name, course_result[i].mark_input))
  
#Define three custom function operator
student_info_function = StudentINFO()
course_info_function = CourseINFO()
mark_info_function = Result_INFO()
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
        students_information = student_info_function.student_info()
    elif option == 2:
        courses_information = course_info_function.course_info()
    elif option == 3:
        course_info_function.courses_list()
    elif option == 4:
        student_info_function.students_list()
    elif option == 5:
        while len(courses_information) == 0 and len(students_information) == 0:
            print("!!!Empty information.Please select adding information option!!!")
            break
        else:
            mark_info_function.mark_subject(courses_information, students_information)
    elif option == 6:
        while len(courses_information) == 0 and len(students_information) == 0:
            print("!!!Empty information.Please select adding information option!!!")
            break
        else:
            mark_info_function.mark_receive(courses_information, students_information)
    elif option == 7:
        break
    else:
        print("!!!You choose the wrong choice.You need to enter the number again!!!")