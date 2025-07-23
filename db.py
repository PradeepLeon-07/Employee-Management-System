import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text,
            role text,
            salary text
            
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, age, doj, email, gender, contact, address,role,salary):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?,?,?)",
                         (name, age, doj, email, gender, contact, address,role,salary))
        self.con.commit()
    def fetch_employee_by_id(self, emp_id):
        self.cur.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
        row = self.cur.fetchone()
        return row  # Make sure the row is being returned
    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from employees where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, age, doj, email, gender, contact, address,role,salary):
        self.cur.execute(
            "update employees set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=?, role=?, salary=? where id=?",
            (name, age, doj, email, gender, contact, address,role,salary, id))
        self.con.commit()
