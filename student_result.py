students = {}


def add_student():
    name = input("Enter student name: ")

    python = int(input("Enter Python marks: "))
    maths = int(input("Enter Maths marks: "))
    evs = int(input("Enter EVS marks: "))

    total = python + maths + evs
    percentage = total / 3

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    students[name] = [python, maths, evs, total, percentage, grade]

    print("Student added successfully.")


def display_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        for name in students:
            data = students[name]

            print("\nName:", name)
            print("Python:", data[0])
            print("Maths:", data[1])
            print("EVS:", data[2])
            print("Total:", data[3])
            print("Percentage:", data[4])
            print("Grade:", data[5])


def search_student():
    name = input("Enter student name: ")

    if name in students:
        data = students[name]

        print("\nStudent Found")
        print("Name:", name)
        print("Python:", data[0])
        print("Maths:", data[1])
        print("EVS:", data[2])
        print("Total:", data[3])
        print("Percentage:", data[4])
        print("Grade:", data[5])
    else:
        print("Student not found.")


def highest_percentage():
    if len(students) == 0:
        print("No student records found.")
    else:
        highest = 0
        highest_name = ""

        for name in students:
            if students[name][4] > highest:
                highest = students[name][4]
                highest_name = name

        print("\nHighest Percentage:", highest)
        print("Student:", highest_name)


def class_average():
    if len(students) == 0:
        print("No student records found.")
    else:
        total = 0

        for name in students:
            total = total + students[name][4]

        average = total / len(students)

        print("\nClass Average:", average)


while True:

    print("\n--------------------------------")
    print(" STUDENT RESULT MANAGEMENT SYSTEM")
    print("--------------------------------")

    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Find Highest Percentage")
    print("5. Find Class Average")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        highest_percentage()

    elif choice == 5:
        class_average()

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
