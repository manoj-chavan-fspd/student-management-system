class Student:

    def __init__(self, name, age, roll_no, marks, out_of_marks):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.marks = marks
        self.out_of_marks = out_of_marks

    def percentage(self):
        percent = self.marks / self.out_of_marks * 100
        return percent

    def result(self):
        if self.percentage() >= 40:
            return "PASS"
        else:
            return "FAIL"

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No.:", self.roll_no)
        print("Marks:", self.marks, "/", self.out_of_marks)
        print("Percentage:", round(self.percentage(), 2), "%")
        print("Result:", self.result())


# Create initial students

s1 = Student("Manoj", 23, 21, 87, 100)
s2 = Student("Rahul", 22, 22, 35, 100)
s3 = Student("Amit", 23, 23, 72, 100)


# Create students list

students = [s1, s2, s3]


# Display all students

def display_students():

    if len(students) == 0:
        print("\nNo students found.")
        return

    print("\n========== ALL STUDENTS ==========")

    for student in students:
        student.display()
        print("----------------------------------")


# Add new student

def add_student():

    print("\n========== ADD STUDENT ==========")

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    roll_no = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))
    out_of_marks = float(input("Enter maximum marks: "))

    student = Student(
        name,
        age,
        roll_no,
        marks,
        out_of_marks
    )

    students.append(student)

    print("\nStudent added successfully!")


# Search student by roll number

def search_student():

    print("\n========== SEARCH STUDENT ==========")

    roll_no = int(input("Enter roll number to search: "))

    found = False

    for student in students:

        if student.roll_no == roll_no:
            print("\nStudent found!")
            print("----------------------------------")
            student.display()
            print("----------------------------------")

            found = True
            break

    if found == False:
        print("\nStudent not found.")


# Delete student by roll number

def delete_student():

    print("\n========== DELETE STUDENT ==========")

    roll_no = int(input("Enter roll number to delete: "))

    found = False

    for student in students:

        if student.roll_no == roll_no:

            students.remove(student)

            print("\nStudent deleted successfully!")

            found = True
            break

    if found == False:
        print("\nStudent not found.")


# Update student details

def update_student():

    print("\n========== UPDATE STUDENT ==========")

    roll_no = int(input("Enter roll number to update: "))

    found = False

    for student in students:

        if student.roll_no == roll_no:

            print("\nStudent found!")
            print("Enter new details:")

            student.name = input("Enter new name: ")
            student.age = int(input("Enter new age: "))
            student.marks = float(input("Enter new marks: "))
            student.out_of_marks = float(
                input("Enter maximum marks: ")
            )

            print("\nStudent updated successfully!")

            found = True
            break

    if found == False:
        print("\nStudent not found.")


# Main menu

while True:

    print("\n")
    print("========================================")
    print("       STUDENT MANAGEMENT SYSTEM")
    print("========================================")

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    print("========================================")

    choice = input("Enter your choice: ")


    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nThank you for using Student Management System!")
        break

    else:
        print("\nInvalid choice! Please try again.")   
    
