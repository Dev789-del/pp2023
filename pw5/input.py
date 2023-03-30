from domains.SystemClasses import Student_Inheritance
from domains.SystemClasses import Course_Main_Class
from domains.SystemClasses import Mark_Factor
from domains.SystemClasses import students_information
from domains.SystemClasses import courses_information
from domains.SystemClasses import mark_subject_list
from domains.SystemClasses import mark_gpa_list
import numpy as numberpython
from math import floor
import datetime
import pickle
#define class Student_Info
class Student_Info:
    def input_student_info():
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
            Student_Content = Student_Inheritance(student_ID, student_name, student_DateOfBirth)
            Student_Content.set_Student_List()
        student_info_time = datetime.datetime.now()
        print(f"You had input information for students at {student_info_time}")  
    #Function to send back student information
    def display_student_info():
        students_list_time = datetime.datetime.now()
        print(f"Here is the list of students information after selecting option 3 at {students_list_time}:")
        for student_ID in students_information:
            print(f"{student_ID}: {students_information[student_ID]['Student_Name'], students_information[student_ID]['Student_DateOfBirth']}")
    def save_student_list():
        #Function to save student list to a text file created
        for x in range(len(students_information)):
            student_out_file = open('students.txt', 'w')
            print(students_information, file = student_out_file)
            student_out_file.close()

#define class Course_Info
class Course_Info:
    def input_course_info():
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
            course_content = Course_Main_Class(course_ID, course_name, course_ECTS)
            course_content.set_CourseList()
        course_info_time = datetime.datetime.now()
        print(f"You had input information for courses at {course_info_time}")
    #Function to send back courses list information
    def display_course_info():
        courses_list_time = datetime.datetime.now()
        print(f"Here is the list of courses information after selecting option 4 at {courses_list_time}:")
        for course_ID in courses_information:
            print(f"{course_ID}: {courses_information[course_ID]['Course_Name'], courses_information[course_ID]['Course_ECTS']}")
    def save_course_list():
        #Function to save course list to a text file created
        for x in range(len(courses_information)):
            course_out_file = open('courses.txt', 'w')
            print(courses_information, file = course_out_file)
            course_out_file.close()
#Define mark_info class
class Mark_Info:
    def input_course_mark():
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
                mark_content = Mark_Factor(mark_student)
                mark_content.set_Mark_Subject(student_ID, course_check)
        mark_subject_time = datetime.datetime.now()
        print(f"You had input information for subject mark at {mark_subject_time}")
    #Function below to display mark transcipt for students
    def display_mark_student():
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
    def save_marks_list():
        #Function to save mark list to a text file created
        for x in range(len(mark_subject_list)):
            mark_out_file = open('marks.txt', 'w')
            print(mark_subject_list, file = mark_out_file)
            mark_out_file.close()
    #Define function to calculate GPA
    def calculate_GPA():
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
        print(f"{GPA_sorted_list}")
#Name objects to all class to perform functions better 
student_info_function = Student_Info
course_info_function = Course_Info
mark_info_function = Mark_Info
