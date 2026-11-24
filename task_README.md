# Task Management System (Python + SQLite)

## 📌 Project Description

The **Task Management System** is a simple console-based application developed using Python and SQLite. It allows administrators to manage tasks and registered users to view and search tasks.

The project demonstrates Python fundamentals, functions, conditional statements, loops, database connectivity, and CRUD operations using SQLite.

## 🚀 Technologies Used

- Python 3
- SQLite3
- VS Code / Jupyter Notebook

## ✨ Features

### 1. Admin Module
- Admin Login
- Add New Tasks
- View All Tasks
- Search Tasks
- Update Existing Tasks
- Delete Tasks
- Admin Logout

### 2. User Module
- User Registration
- User Login
- View Available Tasks
- Search Tasks
- User Logout

### 3. Main Menu
- Admin Login
- User Registration
- User Login
- Exit Application

## 🗄️ Database Structure

The project uses SQLite database (`task.db`) with two tables.

### Users Table

| Column | Description |
|---|---|
| userid | Primary Key (Auto Increment) |
| username | Unique Username |
| password | User Password |

### Tasks Table

| Column | Description |
|---|---|
| id | Primary Key (Auto Increment) |
| taskname | Task Name |
| taskdescription | Task Description |

## 📂 Project Structure

```text
Task-Management-System/
│
├── task_management.py
├── task.db
└── README.md
```

## ⚙️ Installation and Execution

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Clone the Repository

```bash
git clone https://github.com/your-username/Task-Management-System.git
```

### Step 3: Navigate to Project Folder

```bash
cd Task-Management-System
```

### Step 4: Run the Program

```bash
python task_management.py
```

**Note:** SQLite3 is included with standard Python installations. No separate installation is normally required.

## 🔑 Admin Login Details

```text
Username: admin
Password: admin123
```

## 📋 Application Menu

```text
================================
MAIN MENU
================================
1. Admin Login
2. User Registration
3. User Login
4. Exit

Enter your choice:
```

### Admin Menu

```text
1. Add Task
2. View Tasks
3. Search Task
4. Update Task
5. Delete Task
6. Logout
```

### User Menu

```text
1. View Tasks
2. Search Task
3. Logout
```

## 🛠️ Python Concepts Used

- Functions
- While Loops
- If-Else Conditions
- User Input and Output
- Exception Handling
- SQLite Database Connectivity
- SQL Queries
- CRUD Operations (Create, Read, Update, Delete)

## 🎯 Project Objective

The main objective of this project is to develop a simple task management application using Python and SQLite while understanding database operations and implementing basic user authentication.

## 👩‍💻 Author

**Archana K Raveendran**

## 📌 Future Enhancements

- Password Hashing for secure authentication
- Assign Tasks to Individual Users
- Task Status Management (Pending / Completed)
- Task Due Dates
- User Profile Management

---

**Thank you for visiting my project!**