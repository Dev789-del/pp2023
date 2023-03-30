from domains.SystemClasses import students_information
from domains.SystemClasses import courses_information
from domains.SystemClasses import mark_subject_list
import curses
import zipfile
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
    def compress_txt_files():
        with zipfile('info.dat', 'w') as mydatfile:
            mydatfile.write('students.txt')
            mydatfile.write('courses.txt')
            mydatfile.write('marks.txt')
screen_maker = Output_window