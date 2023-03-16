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
class Student_Inheritance(Student):
    def __init__(self, student_ID, Student_Name, Student_DoB):
        super().__init__(Student_Name, Student_DoB)
        self.__Student_ID = student_ID
    def get_StudentID(self):
        return self.__Student_ID
    def get_Student_List(self):
        students_information[self.get_StudentID()] = {'Student_Name': self.get_studentName(), 'Student_DateOfBirth': self.get_studentDOB()}
    
#Define Course_Info class
class Course_Main_Class:
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
class Mark_Factor:
    def __init__(self, mark_student):
        self.__mark_student = mark_student
    def get_mark_student(self):
        return self.__mark_student
    def get_Mark_Subject(self, student_ID, course_ID):
        if student_ID not in mark_subject_list:
            mark_subject_list[student_ID] = {}
        mark_subject_list[student_ID][course_ID] = {'final_mark': [self.get_mark_student()]}
    