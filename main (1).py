from tkinter import *
import employeeManage
import attendance
import leave_module
import search_employee
'''import get_info
import customer_info/'''
import os


class Hotel:
    def __init__(self, base):
        self.base = base
        pad = 3
        self.base.title("ABC Software Solutions")
        self.base.geometry(
            "{0}x{1}+0+0".format(self.base.winfo_screenwidth() - pad, self.base.winfo_screenheight() - pad))

        # create mainframe to add message
        top = Frame(self.base)
        top.pack(side="top")

        # create frame to add buttons
        bottom = Frame(self.base)
        bottom.pack(side="top")

        # display message
        self.label = Label(top, font=('arial', 50, 'bold'), text="APAC Financial Services", fg="light grey", anchor="center")
        self.label.grid(row=0, column=3)

        # create check in button
        self.check_in_button = Button(bottom, text="Employee Management", font=('', 20), bg="black", relief=RIDGE, height=2,
                                      width=50,
                                      fg="light grey", anchor="center",
                                      command=employeeManage.main2) 
        self.check_in_button.grid(row=0, column=2, padx=10, pady=10)

        # create check out button
       
        self.check_out_button = Button(bottom, text="Attendance", font=('', 20), bg="black", relief=RIDGE, height=2,
                                   width=50, fg="light grey", anchor="center",
                                   command=attendance.open_mark_attendance_window)  # call check_out_ui function from check_out.py file
        self.check_out_button.grid(row=1, column=2, padx=10, pady=10)
    
        # create show list button
        self.room_info_button = Button(bottom, text="Apply for leave", font=('', 20), bg="black", relief=RIDGE,
                                       height=2,
                                       width=50, fg="light grey", anchor="center",
                                       command=leave_module.leave_application_ui)  # call get_info_ui function from get_info.py file
        self.room_info_button.grid(row=2, column=2, padx=10, pady=10)
    
        # create get information of all the guest
        self.get_info_button = Button(bottom, text="Search Employee", font=('', 20), bg="black",
                                      relief=RIDGE,
                                      height=2, width=50, fg="light grey", anchor="center",
                                      command=search_employee.run_employee_app)
        # call customer_info_ui function from customer_info.py file
        self.get_info_button.grid(row=3, column=2, padx=10, pady=10)
'''
        # button to exit the program
        self.exit_button = Button(bottom, text="EXIT", font=('', 20), bg="#15d3ba", relief=RIDGE, height=2, width=50,
                                  fg="black",
                                  anchor="center", command=quit)
        self.exit_button.grid(row=4, column=2, padx=10, pady=10)

         '''
def home_ui():
    base = Tk()
    application = Hotel(base)
    
home_ui()
