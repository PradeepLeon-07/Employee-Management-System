from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from db import Database
import sqlite3

db = Database("Employee2.db")
def login():
     username=entry1.get()
     password=entry2.get()

     if username==""and password=="":
        messagebox.showerror("login","Blanks are not allowed")
     elif username=="pradeep" and password=="123":
        messagebox.showinfo("login","Login Successful")
        second_window()
        root.destroy()
     else:
        messagebox.showerror("login","Wrong Credentials")
        
def main2():
    root=Tk()
    root.title("Login Page")
    root.geometry("1920x1080+0+0")
    root.config(bg="cyan4")
    global entry1
    global entry2
    label1=Label(root,text="Login ",bg="cyan4",fg="cyan",font=("elephant",35))
    label1.place(x=570,y=20)
    label2=Label(root,text="User Name : ",font=("perpetua",20),bg="cyan4",fg="#CCCCFF")
    label2.place(x=420,y=200)
    label3=Label(root,text="Password : ",font=("perpetua",20),bg="cyan4",fg="#CCCCFF")
    label3.place(x=440,y=300)
    entry1=Entry(root,font=("courier",15),bg="#40B5AD",bd=3)
    entry1.place(x=600,y=207)


    entry2=Entry(root,font=("courier",15),bg="#40B5AD",show="*",bd=3)
    entry2.place(x=600,y=302)

    button=Button(root,text="Login",bg="cyan3",font=("COURIER",15),bd=10,command=login)
    button.place(x=600,y=400)
    

#second window
def second_window():
    second = Tk()
    second.title("Employee Management System")
    second.geometry("1920x1080+0+0")
    second.config(bg="#2c3e50")
    second.state("zoomed")

    name = StringVar()
    age = StringVar()
    doj = StringVar()
    gender = StringVar()
    email = StringVar()
    contact = StringVar()
    address=StringVar()
    role=StringVar()
    salary=StringVar()

# Entries Frame
    entries_frame = Frame(second, bg="#535c68")
    entries_frame.pack(side=TOP, fill=X)
    title = Label(entries_frame, text="Employee Management System", font=("chiller", 35, "bold"), bg="#535c68", fg="white")
    title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

    lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
    lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
    txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    lblAge = Label(entries_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
    lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
    txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=30)
    txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

    lbldoj = Label(entries_frame, text="D.O.J", font=("Calibri", 16), bg="#535c68", fg="white")
    lbldoj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    txtDoj = Entry(entries_frame, textvariable=doj, font=("Calibri", 16), width=30)
    txtDoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
    lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
    txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
    txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

    lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
    lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
    comboGender['values'] = ("Male", "Female")
    comboGender.grid(row=3, column=1, padx=10, sticky="w")

    lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
    lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
    txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
    txtContact.grid(row=3, column=3, padx=10, sticky="w")

    lblAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
    lblAddress.grid(row=5, column=0, padx=10, pady=10, sticky="w")
    txtAddress = Entry(entries_frame,textvariable=address, width=30, font=("Calibri", 16))
    txtAddress.grid(row=5, column=1, columnspan=4, padx=10, sticky="w")

    lblrole = Label(entries_frame, text="Role", font=("Calibri", 16), bg="#535c68", fg="white")
    lblrole.grid(row=6, column=0, padx=10, pady=10, sticky="w")
    txtrole = Entry(entries_frame, textvariable=role, font=("Calibri", 16), width=30)
    txtrole.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    lblsalary = Label(entries_frame, text="Salary", font=("Calibri", 16), bg="#535c68", fg="white")
    lblsalary.grid(row=6, column=2, padx=10, pady=10, sticky="w")
    txtsalary = Entry(entries_frame, textvariable=salary, font=("Calibri", 16), width=30)
    txtsalary.grid(row=6, column=3, padx=10, pady=10, sticky="w")

    def getData(event):
        selected_row = tv.focus()
        data = tv.item(selected_row)
        global row
        row = data["values"]
        #print(row)
        txtName.insert(END,row[1])
        txtAge.insert(END,row[2])
        txtDoj.insert(END,row[3])
        txtEmail.insert(END,row[4])
        comboGender.insert(END,row[5])
        txtContact.insert(END,row[6])
        txtAddress.insert(END, row[7])
        txtrole.insert(END,row[8])
        txtsalary.insert(END,row[9])

    def dispalyAll():
        tv.delete(*tv.get_children())
        for row in db.fetch():
            tv.insert("", END, values=row)


    def add_employee():
        if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get() == "" or txtrole.get()=="" or txtsalary.get()=="":
            messagebox.showerror("Erorr in Input", "Please Fill All the Details")
            return
        db.insert(txtName.get(),txtAge.get(), txtDoj.get() , txtEmail.get() ,comboGender.get(), txtContact.get(), txtAddress.get(),txtrole.get(),txtsalary.get())
        messagebox.showinfo("Success", "Record Inserted")
        clearAll()
        dispalyAll()



    def update_employee():
        if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == ""  or txtAddress.get() == ""or txtrole.get()=="" or txtsalary.get()=="":
            messagebox.showerror("Erorr in Input", "Please Fill All the Details")
            return
        db.update(row[0],txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(),txtAddress.get(),txtrole.get(),txtsalary.get())
        messagebox.showinfo("Success", "Record Update")
        clearAll()
        dispalyAll()


    def delete_employee():
        db.remove(row[0])
        clearAll()
        dispalyAll()


    def clearAll():
         txtName.delete(0,tk.END)
         txtAge.delete(0,tk.END)
         txtDoj.delete(0,tk.END)
         comboGender.set("")
         txtEmail.delete(0,tk.END)
         txtContact.delete(0,tk.END)
         txtAddress.delete(0,tk.END)
         txtrole.delete(0,tk.END)
         txtsalary.delete(0,tk.END)
         

    def retrieve():
        conn=sqlite3.connect("Employee2.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM employees")
        rows=cursor.fetchall()
        conn.close()
        display_window=Tk()
        display_window.title("USER DATA")
        display_window.geometry("1920x1080+0+0")
        display_window.config(bg="#2c3e50")
        display_window.state("zoomed")
   

        tree_frame = Frame(display_window, bg="#ecf0f1")
        tree_frame.place(x=0, y=0, width=1350, height=1000)
        style = ttk.Style()
        style.configure("mystyle.Treeview", font=('Calibri', 13),
                        rowheight=50)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13))  # Modify the font of the headings
        tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8,9,10), style="mystyle.Treeview",height=1000)
        tv.heading("1", text="ID")
        tv.column("1", width=5)
        tv.heading("2", text="Name")
        tv.column("2", width=10)
        tv.heading("3", text="Age")
        tv.column("3", width=5)
        tv.heading("4", text="D.O.J")
        tv.column("4", width=10)
        tv.heading("5", text="Email")
        tv.column("5", width=5)
        tv.heading("6", text="Gender")
        tv.column("6", width=10)
        tv.heading("7", text="Contact")
        tv.column("7", width=10)
        tv.heading("8", text="Address")
        tv.column("8", width=10)
        tv.heading("9", text="Role")
        tv.column("9", width=10)
        tv.heading("10", text="Salary")
        tv['show'] = 'headings'
        tv.bind("<ButtonRelease-1>", getData)
        tv.pack(fill=X)
            
        tv.delete(*tv.get_children())
        for row in db.fetch():
            tv.insert("", END, values=row)

   

    btn_frame = Frame(entries_frame, bg="#535c68")
    btn_frame.grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky="w")
    btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                    bg="#16a085", bd=0).grid(row=0, column=0)
    btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                     fg="white", bg="#2980b9",
                     bd=0).grid(row=0, column=1, padx=10)
    btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                       fg="white", bg="#c0392b",
                       bd=0).grid(row=0, column=2, padx=10)
    btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                      bg="#f39c12",
                      bd=0).grid(row=0, column=3, padx=10)
    btnRetrieve = Button(btn_frame, command=retrieve, text="Show all Records", width=15, font=("Calibri", 16, "bold"), fg="white",
                      bg="#ff1493",
                      bd=0).grid(row=0, column=4, padx=10)
# Table Frame
    tree_frame = Frame(second, bg="#ecf0f1")
    tree_frame.place(x=0, y=420, width=1350, height=520)
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 12),
                    rowheight=30)  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 12))  # Modify the font of the headings
    tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8,9,10), style="mystyle.Treeview")
    tv.heading("1", text="ID")
    tv.column("1", width=5)
    tv.heading("2", text="Name")
    tv.column("2", width=10)
    tv.heading("3", text="Age")
    tv.column("3", width=5)
    tv.heading("4", text="D.O.J")
    tv.column("4", width=10)
    tv.heading("5", text="Email")
    tv.column("5", width=5)
    tv.heading("6", text="Gender")
    tv.column("6", width=10)
    tv.heading("7", text="Contact")
    tv.column("7", width=10)
    tv.heading("8", text="Address")
    tv.column("8", width=10)
    tv.heading("9", text="Role")
    tv.column("9", width=10)
    tv.heading("10", text="Salary")
    tv['show'] = 'headings'
    tv.bind("<ButtonRelease-1>", getData)
    tv.pack(fill=X)

    dispalyAll()
    second.mainloop()

