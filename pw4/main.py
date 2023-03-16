from curses import wrapper
from output import screen_maker
from domains.SystemClasses import students_information
from domains.SystemClasses import courses_information
from input import mark_info_function
from input import student_info_function
from input import course_info_function
#Executing functions for inputing information to courses and students
student_info_function.student_info()
course_info_function.course_info()
#While loop to show list of choices
Condition = True
while Condition:
    print("----------Welcome to Student Management System----------")
    print("Here is your list of choices:")
    print("1.Add marks for students")
    print("2.Calculate GPA for students")
    print("3.Show sorted GPA list")
    print("4.Show marks,courses & students information")
    print("5.Exit system")
    option = int(input("Choose your option number: "))
    if option == 1:
        while len(courses_information) == 0 and len(students_information) == 0:
            print("!!!Empty information!!!")
            break
        else: 
            mark_info_function.mark_subject()
    elif option == 2:
        
        mark_info_function.GPA_calculator()
    elif option == 3:
         mark_info_function.show_info_gpa_sorted_list()
        
    elif option == 4:
        while len(students_information) == 0:
            print("!!!Empty information in students data!!!")
            break
        else:
            wrapper(screen_maker.show_all_info)
    elif option == 5:
        break
    else:
        print("You choose the wrong choice.You need to enter the number again.")