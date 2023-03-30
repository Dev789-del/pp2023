from curses import wrapper
from output import screen_maker
from domains.SystemClasses import students_information
from domains.SystemClasses import courses_information
from input import mark_info_function
from input import student_info_function
from input import course_info_function
#Executing functions for inputing information to courses and students
student_info_function.input_student_info()
course_info_function.input_course_info()
#While loop to show list of choices
Condition = True
while Condition:
    print("----------Welcome to Student Management System----------")
    print("Here is your list of choices:")
    print("1.Add marks for students")
    print("2.Calculate GPA for students")
    print("3.Show sorted GPA list")
    print("4.Save students list to txt file")
    print("5.Save courses list to txt file")
    print("6.Save marks list to txt file")
    print("7.Compress txt files to dat file")
    print("8.Show marks,courses & students information")
    print("9.Exit system")
    option = int(input("Choose your option number: "))
    if option == 1:
        while len(courses_information) == 0 and len(students_information) == 0:
            print("!!!Empty information!!!")
            break
        else: 
            mark_info_function.input_course_mark()
    elif option == 2:
        
        mark_info_function.calculate_GPA()
    elif option == 3:
        mark_info_function.show_info_gpa_sorted_list()
    elif option == 4:
        student_info_function.save_student_list()
    elif option == 5:
        course_info_function.save_course_list()
    elif option == 6:
        mark_info_function.save_marks_list()
    elif option == 7:
        screen_maker.compress_txt_files()
    elif option == 8:
        while len(students_information) == 0:
            print("!!!Empty information in students data!!!")
            break
        else:
            wrapper(screen_maker.show_all_info)
    elif option == 9:
        break
    else:
        print("You choose the wrong choice.You need to enter the number again.")