import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

def create_leave_table():
    conn = sqlite3.connect("Employee2.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS leave_requests (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        employee_id INTEGER,
                        leave_type TEXT,
                        start_date TEXT,
                        end_date TEXT,
                        status TEXT DEFAULT 'Pending')''')
    conn.commit()
    conn.close()

def apply_leave():
    emp_id = emp_id_entry.get()
    leave_type = leave_type_var.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    
    if not (emp_id and leave_type and start_date and end_date):
        messagebox.showerror("Error", "All fields are required!")
        return
    
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leave_requests (employee_id, leave_type, start_date, end_date) VALUES (?, ?, ?, ?)",
                   (emp_id, leave_type, start_date, end_date))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Leave applied successfully!")
    emp_id_entry.delete(0, tk.END)
    start_date_entry.delete(0, tk.END)
    end_date_entry.delete(0, tk.END)

def admin_approve_reject():
    def update_status():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select a request to update")
            return
        leave_id = tree.item(selected_item)['values'][0]
        new_status = status_var.get()
        
        conn = sqlite3.connect("employee.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE leave_requests SET status = ? WHERE id = ?", (new_status, leave_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Leave status updated!")
        admin_window.destroy()
        admin_approve_reject()
    
    admin_window = tk.Toplevel()
    admin_window.title("Approve/Reject Leaves")
    admin_window.configure(bg="#f8f9fa")
    
    tree = ttk.Treeview(admin_window, columns=("ID", "Emp ID", "Type", "Start", "End", "Status"), show='headings')
    for col in ("ID", "Emp ID", "Type", "Start", "End", "Status"):
        tree.heading(col, text=col)
    tree.pack(pady=10, padx=10)
    
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leave_requests")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)
    conn.close()
    
    status_var = tk.StringVar()
    ttk.Label(admin_window, text="Update Status:", background="#f8f9fa", font=("Verdana", 12, "bold")).pack()
    ttk.Combobox(admin_window, textvariable=status_var, values=["Approved", "Rejected"]).pack()
    ttk.Button(admin_window, text="Update", command=update_status, style="TButton").pack(pady=10)

def leave_application_ui():
    global emp_id_entry, leave_type_var, start_date_entry, end_date_entry
    root = tk.Tk()
    root.title("Leave Application")
    root.geometry("450x500")
    root.configure(bg="#ffebcd")
    
    style = ttk.Style()
    style.configure("TButton", font=("Verdana", 11, "bold"), padding=7, background="black", foreground="Red")
    
    tk.Label(root, text="Attendance System", bg="#ff4500", fg="white", font=("Arial", 18, "bold"), pady=10).pack(fill="x")
    
    tk.Label(root, text="Employee ID", bg="#ffebcd", font=("Verdana", 12, "bold")).pack(pady=5)
    emp_id_entry = tk.Entry(root, font=("Verdana", 11))
    emp_id_entry.pack(pady=5)
    
    tk.Label(root, text="Leave Type", bg="#ffebcd", font=("Verdana", 12, "bold")).pack(pady=5)
    leave_type_var = tk.StringVar()
    ttk.Combobox(root, textvariable=leave_type_var, values=["Sick Leave", "Casual Leave", "Annual Leave"], font=("Verdana", 11)).pack(pady=5)
    
    tk.Label(root, text="Start Date (YYYY-MM-DD)", bg="#ffebcd", font=("Verdana", 12, "bold")).pack(pady=5)
    start_date_entry = tk.Entry(root, font=("Verdana", 11))
    start_date_entry.pack(pady=5)
    
    tk.Label(root, text="End Date (YYYY-MM-DD)", bg="#ffebcd", font=("Verdana", 12, "bold")).pack(pady=5)
    end_date_entry = tk.Entry(root, font=("Verdana", 11))
    end_date_entry.pack(pady=5)
    
    ttk.Button(root, text="Apply Leave", command=apply_leave, style="TButton").pack(pady=10)
    ttk.Button(root, text="Admin Panel", command=admin_approve_reject, style="TButton").pack()
    
    root.mainloop()

create_leave_table()
leave_application_ui()
