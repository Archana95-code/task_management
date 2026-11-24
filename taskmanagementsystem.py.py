import sqlite3

# DATABASE CONNECTION
def connect_db():
    return sqlite3.connect("task.db")


# CREATE TABLES
conn = connect_db()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    taskname TEXT,
    taskdescription TEXT
)
""")

conn.commit()
conn.close()


# ADMIN LOGIN
def admin_login():
     username = input("Enter admin username: ")
     password = input("Enter admin password: ")

     if username == "admin" and password == "admin123":
        print("Admin Login Successful!")
        return True

     else:
        print("Invalid Admin Username or Password!")
        return False
# USER REGISTRATION
def register():

    conn = connect_db()
    cursor = conn.cursor()

    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        cursor.execute("""
            INSERT INTO users(username, password)
            VALUES(?, ?)
        """, (username, password))
        conn.commit()
        print("Registration Successful!")

    except sqlite3.IntegrityError:
        print("Error: Username already exists!")

    finally:
        conn.close()


# USER LOGIN
def login():
    conn = connect_db()
    cursor = conn.cursor()

    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute("""
        SELECT * FROM users
        WHERE username = ? AND password = ?
    """, (username, password))
    result = cursor.fetchone()

    conn.close()

    if result:
        print("Login Successful!")
        print("Welcome", username)
        return result[0]

    else:
        print("Invalid username or password!")
        return None
# ADD TASK - ADMIN ONLY
def addtask():
  conn = connect_db()
  cursor = conn.cursor()
  name =input("Enter task name:---")
  des = input("Enter task description:---")
     
  cursor.execute('''
                     INSERT into tasks(taskname,taskdescription) VALUES(?,?)
                     ''',
                     (name,des,))
  conn.commit()

  print("Task Added Successfully!")
  conn.close()
 

    # VIEW TASKS - ADMIN AND USER
def viewtasks():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    data = cursor.fetchall()

    if data:
        print("\n========== TASK DETAILS ==========")

        for i in data:
            print("Task ID:", i[0])
            print("Task Name:", i[1])
            print("Description:", i[2])
            print("--------------------------------")

    else:
        print("No Tasks Found!")

    conn.close()


# SEARCH TASK - ADMIN AND USER
def searchtask():

    conn = connect_db()
    cursor = conn.cursor()
    name = input("Enter task name to search: ")

    cursor.execute("""
        SELECT * FROM tasks
        WHERE taskname LIKE ?
    """, ('%' + name + '%',))

    result = cursor.fetchall()

    if result:
        print("\n========== SEARCH RESULTS ==========")

        for task in result:
            print("Task ID:", task[0])
            print("Task Name:", task[1])
            print("Description:", task[2])
            print("--------------------------------")

    else:
        print("Task Not Found!")

    conn.close()


# UPDATE TASK - ADMIN ONLY
def updatetasks():

    conn = connect_db()
    cursor = conn.cursor()

    taskid = input("Enter task ID: ")
    new_taskname = input("Enter new task name: ")

    cursor.execute("""
        UPDATE tasks
        SET taskname = ?
        WHERE id = ?
    """, (new_taskname, taskid))

    conn.commit()

    if cursor.rowcount > 0:
        print("Task Updated Successfully!")
    else:
        print("Task ID Not Found!")

    conn.close()


# DELETE TASK - ADMIN ONLY
def deletetasks():

    conn = connect_db()
    cursor = conn.cursor()

    taskid = input("Enter task ID: ")

    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (taskid,))

    conn.commit()

    if cursor.rowcount > 0:
        print("Task Deleted Successfully!")
    else:
        print("Task ID Not Found!")

    conn.close()

    # ADMIN MENU
def adminmenu():

    while True:

        print("\n========== TASK MANAGEMENT SYSTEM/ADMIN MENU ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Search Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Logout")

        ch = input("Enter your choice: ").strip()
        if ch == "1":
            addtask()

        elif ch == "2":
            viewtasks()

        elif ch == "3":
            searchtask()

        elif ch == "4":
            updatetasks()

        elif ch == "5":
            deletetasks()
        elif ch == "6":
            print("Admin Logout Successful!")
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid Choice!")


# USER MENU
def usermenu():
      while True:

        print("\n========== USER MENU ==========")
        print("1. View Tasks")
        print("2. Search Task")
        print("3. Logout")

        ch = input("Enter your choice: ")

        if ch == "1":
            viewtasks()

        elif ch == "2":
            searchtask()

        elif ch == "3":
            print("User Logout Successful!")
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid Choice!")


# MAIN MENU
def main():

    while True:

        print("\n================================")
        print("MAIN MENU")
        print("================================")

        print("1. Admin Login")
        print("2. User Registration")
        print("3. User Login")
        print("4. Exit")

        ch = input("Enter your choice: ").strip()

        if ch == "1":

            if admin_login():
                adminmenu()

        elif ch == "2":
            register()

        elif ch == "3":

            userid = login()

            if userid is not None:
                usermenu()

        elif ch == "4":
            print("Thank you for using Task Management System!")
            break

        else:
            print("Invalid Choice! Please try again.")


# RUN PROGRAM
main()
