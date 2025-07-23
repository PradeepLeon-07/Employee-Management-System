import tkinter as tk
from tkinter import messagebox
from db import Database  # Assuming db.py contains the Database class

def run_employee_app():
    # Initialize the Database
    db = Database("Employee2.db")  # Use your existing database file here

    def fetch_employee():
        """Fetch employee details using the employee ID."""
        try:
            emp_id = int(emp_id_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid employee ID.")
            return
        
        employee_data = db.fetch_employee_by_id(emp_id)
        
        if employee_data:
            show_employee_details(employee_data)
        else:
            messagebox.showerror("Error", "Employee not found!")

    def show_employee_details(employee_data):
        """Display the details of the employee in a new window."""
        emp_window = tk.Toplevel(root)
        emp_window.title("Employee Details")
        emp_window.geometry("600x500")  # Increased window size for better content layout
        emp_window.config(bg="#f0f8ff")  # Background color for the new window
        
        # Adding a title for the details window
        details_title = tk.Label(emp_window, text="Employee Information", font=("Segoe UI", 20, "bold"), fg="#2e8b57", bg="#f0f8ff")
        details_title.grid(row=0, column=0, columnspan=2, pady=20)

        details = [
            ("ID", employee_data[0]),
            ("Name", employee_data[1]),
            ("Age", employee_data[2]),
            ("DOJ", employee_data[3]),
            ("Email", employee_data[4]),
            ("Gender", employee_data[5]),
            ("Contact", employee_data[6]),
            ("Address", employee_data[7]),
            ("Role", employee_data[8]),
            ("Salary", employee_data[9])
        ]
        
        # Display employee details in the new window with better padding and font
        for i, (label, value) in enumerate(details):
            tk.Label(emp_window, text=f"{label}: {value}", font=("Arial", 14), bg="#f0f8ff", fg="#00008B").grid(row=i+1, column=0, padx=20, pady=10, sticky="w")
            # Adding some nice spacing and color contrast for text
            
        # Adding a close button with a stylish design
        close_button = tk.Button(emp_window, text="Close", font=("Segoe UI", 12, "bold"), bg="#f44336", fg="white", relief="raised", command=emp_window.destroy)
        close_button.grid(row=len(details)+1, column=0, columnspan=2, pady=20, padx=50)

    def create_main_window():
        """Create the main window for the application."""
        global root, emp_id_entry
        
        root = tk.Tk()
        root.title("Employee Details Retrieval")
        root.geometry("600x400")  # Increased window size for more content
        root.config(bg="#f0f8ff")  # Background color (AliceBlue)
        
        # Title Label for the Application
        title_label = tk.Label(root, text="APAC Financial Services", font=("Segoe UI", 24, "bold"), fg="#2e8b57", bg="#f0f8ff")
        title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Short Description or Company Info
        info_label = tk.Label(root, text="Welcome to the Employee Details Retrieval System.\nPlease enter an Employee ID to view details.", font=("Calibri", 12), fg="#4B0082", bg="#f0f8ff", wraplength=500, justify="center")
        info_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Employee ID Entry Section with more stylish fonts and spacing
        emp_id_label = tk.Label(root, text="Enter Employee ID", font=("Segoe UI", 16, "bold"), fg="#2e8b57", bg="#f0f8ff")
        emp_id_label.grid(row=2, column=0, padx=20, pady=40, sticky="w")

        emp_id_entry = tk.Entry(root, font=("Arial", 14), width=20, bd=3, relief="sunken", fg="black")
        emp_id_entry.grid(row=2, column=1, padx=20, pady=40)

        # Button to Fetch Employee Data with a stylish design
        fetch_button = tk.Button(root, text="Fetch Details", font=("Segoe UI", 14, "bold"), bg="#4CAF50", fg="white", relief="raised", bd=5, command=fetch_employee)
        fetch_button.grid(row=3, column=0, columnspan=2, pady=20, padx=50)
        
        # Start the Tkinter main loop
        root.mainloop()

    # Run the main window
    create_main_window()


