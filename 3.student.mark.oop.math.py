"""
Practical 3 objectives:
1.Use code of seconf practical(DONE)
2.Use math module to round-down student scores to 1-digit decimal upon input(DONE)
3.Use numpy module to calculate GPA for a given student and sort descending GPA for student list(DONE)
4.Use curses module(DONE)
"""

#define empty lists and import datetime package to show log after input information
courses_information = {}
students_information = {}
mark_subject_list = {}
mark_gpa_list = {}
GPA_sorted_list = {}
import datetime
#import floor function from math module and numpy
from math import floor
import numpy as numberpython
#Using curses module to import wrapper and window
import curses
from curses import window
from curses import wrapper
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
        students_information[self.get_StudentID()] = {'Student_Name': self.get_studentName(), 'Student_DateOfBirth': self.get_studentDOB()}
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
            Student_Content = Student_Info(student_ID, student_name, student_DateOfBirth)
            Student_Content.get_Student_List()
        student_info_time = datetime.datetime.now()
        print(f"You had input information for students at {student_info_time}")  
    #Function to send back student information
    def students_list_display():
        students_list_time = datetime.datetime.now()
        print(f"Here is the list of students information after selecting option 3 at {students_list_time}:")
        for student_ID in students_information:
            print(f"{student_ID}: {students_information[student_ID]['Student_Name'], students_information[student_ID]['Student_DateOfBirth']}")
#Define Course_Info class
class Course_Info:
    def __init__(self, course_ID, course_name, course_ECTs):
        self.__course_ID = course_ID
        self.__course_name = course_name    
        self.__course_ECTs = course_ECTs   
    def get_CourseName(self):
        return self.__course_name
    def get_CourseID(self):
        return self.__course_ID
    def get_CourseCredits(self):
        return self.__course_ECTs
    def get_CourseList(self):
        courses_information[self.get_CourseID()] = {"Course_Name": self.get_CourseName(), "Course_ECTS": self.get_CourseCredits()}
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
            course_ECTS = int(input("Enter course credits count: "))
            course_content = Course_Info(course_ID, course_name, course_ECTS)
            course_content.get_CourseList()
        course_info_time = datetime.datetime.now()
        print(f"You had input information for courses at {course_info_time}")
    #Function to send back courses list information
    def courses_list_display():
        courses_list_time = datetime.datetime.now()
        print(f"Here is the list of courses information after selecting option 4 at {courses_list_time}:")
        for course_ID in courses_information:
            print(f"{course_ID}: {courses_information[course_ID]['Course_Name'], courses_information[course_ID]['Course_ECTS']}")
class Mark_Info:
    def __init__(self, mark_student):
        self.__mark_student = mark_student
    def get_mark_student(self):
        return self.__mark_student
    def get_Mark_Subject(self, student_ID, course_ID):
        if student_ID not in mark_subject_list:
            mark_subject_list[student_ID] = {}
        mark_subject_list[student_ID][course_ID] = {'final_mark': [self.get_mark_student()]}
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
                mark_student = floor(mark_student * 10 / 10.0)
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
    #Define function to calculate GPA
    def GPA_calculator():
        ECTS_SUM = 0
        MARK_SUM = 0
        for student_ID in students_information:
            for course_ID in courses_information:
                MARK_SUM += sum(mark_subject_list[student_ID][course_ID]['final_mark'] * courses_information[course_ID]['Course_ECTS'])
                ECTS_SUM += courses_information[course_ID]['Course_ECTS']
            average_mark = floor(MARK_SUM / ECTS_SUM)
            mark_gpa_list[student_ID] = {'gpa_mark_got': average_mark}
            ECTS_SUM = 0
            MARK_SUM = 0
        mark_gpa_get = mark_gpa_list.items()
        final_result = list(mark_gpa_get)
        array_gpa = numberpython.array(final_result)
        print("Here is the gpa list that is calculated:")
        print(f"{mark_gpa_list}")
    #Define function to show sorted gpa list
    def show_info_gpa_sorted_list():
        GPA_sorted_list = sorted(mark_gpa_list.items(), key = lambda x:x[1]['gpa_mark_got'], reverse = True)
        print("Here is the sorted gpa list of all given students:")
        print(f"\n{GPA_sorted_list}")
#Name objects to all class to perform functions better 
student_info_function = Student_Info
course_info_function = Course_Info
mark_info_function = Mark_Info
#Executing functions for inputing information to courses and students
student_info_function.student_info()
course_info_function.course_info()
#Define output window class
class Output_window:
    def show_all_info(stdscr):
        curses.newwin(1, 20, 10, 10)
        stdscr.clear()
        stdscr.addstr("Information for Student Management System after getting from user:")
        stdscr.addstr(f"\nStudents Info: {students_information}")
        stdscr.addstr(f"\nCourses Info: {courses_information}")
        stdscr.addstr(f"\nSubject marks Info: {mark_subject_list}")
        stdscr.refresh()
        stdscr.getch()
screen_maker = Output_window
#While loop to show list of choices
Condition = True
while Condition:
    print("----------Welcome to Student Management System----------")
    print("Here is your list of choices:")
    print("1.Show all marks,courses & students information")
    print("2.Add marks for students")
    print("3.Calculate GPA for students")
    print("4.Show sorted GPA list")
    print("5.Exit system")
    option = int(input("Choose your option number: "))
    if option == 1:
        while len(students_information) == 0:
            print("!!!Empty information in students data!!!")
            break
        else:
            wrapper(screen_maker.show_all_info)
    elif option == 2:
        while len(courses_information) == 0 and len(students_information) == 0:
            print("!!!Empty information!!!")
            break
        else: 
            mark_info_function.mark_subject()
    elif option == 3:
        mark_info_function.GPA_calculator()
    elif option == 4:
        mark_info_function.show_info_gpa_sorted_list()
    elif option == 5:
        break
    else:
        print("You choose the wrong choice.You need to enter the number again.")
