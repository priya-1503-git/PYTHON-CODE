students = {}

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    students[roll] = name
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
    else:
        print("\n--- Student List ---")
        for roll, name in students.items():
            print("Roll:", roll, "| Name:", name)

def delete_student():
    roll = input("Enter roll number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice")