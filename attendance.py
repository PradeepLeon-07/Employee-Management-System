import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

def open_mark_attendance_window():
    # Create Attendance table if it doesn't exist
    with sqlite3.connect('Employee2.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Attendance (
                            att_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            emp_id INTEGER,
                            date DATE,
                            status TEXT,
                            FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
                        )''')

    def mark_attendance():
        emp_id = entry_att_emp_id.get().strip()
        status = attendance_status.get().strip()

        if not emp_id.isdigit():
            messagebox.showerror("Error", "Employee ID must be a number.")
            return
        if not status:
            messagebox.showerror("Error", "Please select an attendance status.")
            return

        date = datetime.now().date()

        # Insert into database
        with sqlite3.connect('Employee2.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Attendance (emp_id, date, status) VALUES (?, ?, ?)", (emp_id, date, status))
            conn.commit()

        messagebox.showinfo("Success", f"Attendance marked as {status} for Employee ID {emp_id}")
        mark_att_window.destroy()

    # Create Attendance Window
    mark_att_window = tk.Toplevel()
    mark_att_window.title("Mark Attendance")
    mark_att_window.geometry("550x400")
    mark_att_window.config(bg="#1B2631")  # Dark background

    # Date
    current_date = datetime.now().strftime("%A, %d %B %Y")

    # Title Label
    title_label = tk.Label(mark_att_window, text="📌 ATTENDANCE SYSTEM 📌", font=("Algerian", 26, "bold"), fg="#F1C40F", bg="#2E4053", pady=10)
    title_label.pack(fill="x")

    # Date Label
    date_label = tk.Label(mark_att_window, text=f"📅 {current_date}", font=("Comic Sans MS", 14, "bold"), fg="white", bg="#1B2631")
    date_label.pack(pady=5)

    # Welcome Message
    welcome_label = tk.Label(mark_att_window, text="🔹 Welcome! Mark attendance easily & securely. 🔹", 
                             font=("Verdana", 12, "italic"), fg="#AAB7B8", bg="#1B2631")
    welcome_label.pack(pady=10)

    # Employee ID
    tk.Label(mark_att_window, text="🔹 Employee ID:", font=("Verdana", 12, "bold"), fg="white", bg="#1B2631").pack(pady=5)
    entry_att_emp_id = tk.Entry(mark_att_window, font=("Arial", 14), bg="white", fg="black", bd=3, relief="ridge", width=20)
    entry_att_emp_id.pack(pady=5)

    # Attendance Status
    tk.Label(mark_att_window, text="🔹 Select Status:", font=("Verdana", 12, "bold"), fg="white", bg="#1B2631").pack(pady=5)
    attendance_status = ttk.Combobox(mark_att_window, values=["Present ✅", "Absent ❌", "Leave 🏖"], font=("Arial", 12))
    attendance_status.pack(pady=5, ipadx=10, ipady=5)
    attendance_status.set("Present ✅")  # Default value

    # Mark Attendance Button
    mark_btn = tk.Button(mark_att_window, text="✅ Mark Attendance", command=mark_attendance, font=("Arial", 14, "bold"), 
                         bg="#28B463", fg="white", activebackground="#1E8449", activeforeground="white", bd=3, relief="raised", width=20)
    mark_btn.pack(pady=15, ipadx=10, ipady=5)

    # Footer Message
    footer_label = tk.Label(mark_att_window, text="✔ Data is securely stored ✔", 
                            font=("Verdana", 10, "italic"), fg="#D5D8DC", bg="#1B2631")
    footer_label.pack(pady=10)

   

open_mark_attendance_window()
