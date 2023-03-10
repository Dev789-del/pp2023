#define three empty database and import datetime package to show log after input information
courses_information = {}
students_information = {}
mark_subject_list = {}
import datetime
#Define class Student
class Student:
    def __init__(self, Student_Name, Student_DoB):
        self.__Student_Name =  Student_Name
        self.__Student_DoB = Student_DoB
    def get_studentName(self):
        return self.__Student_Name
    def get_studentDOB(self):
        return self.__Student_DoB
#Define class Student_Info
class Student_Info(Student):
    def __init__(self, student_ID, Student_Name, Student_DoB):
        super().__init__(Student_Name, Student_DoB)
        self.__Student_ID = student_ID
    def get_StudentID(self):
        return self.__Student_ID
    def get_Student_List(self):
        students_information[self.get_StudentID()] = {'Student_Name': self.get_studentName(), "Student_DateOfBirth": self.get_studentDOB()}
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
            Student_Content = Student_Info(student_ID, student_name, student_DateOfBirth)
            Student_Content.get_Student_List()
        student_info_time = datetime.datetime.now()
        print(f"You had input information for students at {student_info_time}")  
    #Function to send back student information
    def students_list_display():
        students_list_time = datetime.datetime.now()
        print(f"Here is the list of students information after selecting option 2 at {students_list_time}:")
        for student_ID in students_information:
            print(f"{student_ID}: {students_information[student_ID]['Student_Name'], students_information[student_ID]['Student_DateOfBirth']}")
#Define Course_Info class
class Course_Info:
    def __init__(self, course_ID, course_name):
        self.__course_ID = course_ID
        self.__course_name = course_name       
    def get_CourseName(self):
        return self.__course_name
    def get_CourseID(self):
        return self.__course_ID
    def get_CourseList(self):
        courses_information[self.get_CourseID()] = {'Course_Name': self.get_CourseName()}
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
            course_content = Course_Info(course_ID, course_name)
            course_content.get_CourseList()
        course_info_time = datetime.datetime.now()
        print(f"You had input information for courses at {course_info_time}")
    #Function to send back courses list information
    def courses_list_display():
        courses_list_time = datetime.datetime.now()
        print(f"Here is the list of courses information after selecting option 1 at {courses_list_time}:")
        for course_ID in courses_information:
            print(f"{course_ID}: {courses_information[course_ID]['Course_Name']}")
class Mark_Info:
    def __init__(self, mark_student):
        self.__mark_student = mark_student
    def get_mark_student(self):
        return self.__mark_student
    def get_Mark_Subject(self, student_ID, course_ID):
        if student_ID not in mark_subject_list:
            mark_subject_list[student_ID] = {}
        mark_subject_list[student_ID][course_ID] = [self.get_mark_student()]
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
                mark_content = Mark_Info(mark_student)
                mark_content.get_Mark_Subject(student_ID, course_check)
        mark_subject_time = datetime.datetime.now()
        print(f"You had input information for subject mark at {mark_subject_time}")
    #Function below to display mark transcipt for students
    def mark_receive_display():
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

#Name objects to all class to perform functions better
student_info_function = Student_Info
course_info_function = Course_Info
mark_info_function = Mark_Info
#While loop to show list of choices
Condition = True
while Condition:
    print("----------Welcome to Student Management System----------")
    print("Here is your list of choices:")
    print("1.Input information for students")
    print("2.Input information for courses")
    print("3.Show students information")
    print("4.Show courses information")
    print("5.Add marks for students")
    print("6.Show students mark information")
    print("7.Exit system")
    option = int(input("Choose your option number: "))
    if option == 1:
        student_info_function.student_info()
    elif option == 2:
        course_info_function.course_info()
    elif option == 3:
        while len(students_information) == 0:
            print("!!!Empty information in students data!!!")
            break
        else:
            student_info_function.students_list_display()
    elif option == 4:
        while len(courses_information) == 0:
            print("!!!Empty information in courses data!!!")
            break
        else: 
            course_info_function.courses_list_display()
    elif option == 5:
        while len(courses_information) == 0 and len(students_information) == 0:
            print("!!!Empty information!!!")
            break
        else: 
            mark_info_function.mark_subject()
    elif option == 6:
        while len(courses_information) == 0 and len(students_information) == 0:
            print("!!!Empty information!!!")
            break
        else: 
            mark_info_function.mark_receive_display()
    elif option == 7:
        break
    else:
        print("You choose the wrong choice.You need to enter the number again.")