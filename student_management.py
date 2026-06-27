students = {}




# Add Student
def add_student():
    try:
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            print(" Roll Number Already Exists!")
            return

        name = input("Enter Name: ")

        marks = []

        for i in range(1, 6):
            mark = float(input(f"Enter Subject {i} Marks: "))
            marks.append(mark)

        percentage = sum(marks) / 5
        grade = calculate_grade(percentage)

        students[roll] = {
            "name": name,
            "marks": marks,
            "percentage": percentage,
            "grade": grade
        }

        print(" Student Added Successfully!")

    except ValueError:
        print("Invalid Input!")

# Grade Calculation
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "F"



# View All Students
def view_all():
    if not students:
        print("No Records Found!")
        return

    sorted_students = sorted(
        students.items(),
        key=lambda x: x[1]["percentage"],
        reverse=True
    )

    print("\n" + "=" * 75)
    print(f"{'Rank':<6}{'Roll':<10}{'Name':<20}{'%':<15}{'Grade'}")
    print("=" * 75)

    rank = 1

    for roll, data in sorted_students:
        print(
            f"{rank:<6}{roll:<10}{data['name']:<20}"
            f"{data['percentage']:<15.2f}{data['grade']}"
        )
        rank += 1

    print("=" * 75)


# Search Student
def search_student():
    try:
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            data = students[roll]

            print("\nStudent Details")
            print("-" * 30)
            print("Roll Number :", roll)
            print("Name        :", data["name"])
            print("Marks       :", data["marks"])
            print("Percentage  :", round(data["percentage"], 2))
            print("Grade       :", data["grade"])

        else:
            print(" Student Not Found!")

    except ValueError:
        print(" Invalid Roll Number!")


# Update Student
def update_student():
    try:
        roll = int(input("Enter Roll Number: "))

        if roll in students:

            marks = []

            for i in range(1, 6):
                mark = float(input(f"Enter New Subject {i} Marks: "))
                marks.append(mark)

            percentage = sum(marks) / 5
            grade = calculate_grade(percentage)

            students[roll]["marks"] = marks
            students[roll]["percentage"] = percentage
            students[roll]["grade"] = grade

            print(" Record Updated Successfully!")

        else:
            print(" Student Not Found!")

    except ValueError:
        print(" Invalid Input!")


# Delete Student
def delete_student():
    try:
        roll = int(input("Enter Roll Number: "))

        if roll in students:

            confirm = input(
                "Are you sure? (yes/no): "
            ).lower()

            if confirm == "yes":
                del students[roll]
                print("Record Deleted Successfully!")

        else:
            print(" Student Not Found!")

    except ValueError:
        print(" Invalid Roll Number!")


# Class Report
def class_report():

    if not students:
        print("No Records Found!")
        return

    topper = max(
        students.items(),
        key=lambda x: x[1]["percentage"]
    )

    average = (
        sum(student["percentage"]
            for student in students.values())
        / len(students)
    )

    pass_count  =0
    fail_count = 0

    for student in students.values():
        if student["percentage"] >= 50:
            pass_count += 1
        else:
            fail_count += 1

    print("\n===== CLASS REPORT =====")
    print("Topper :", topper[1]["name"])
    print("Top Percentage :", round(topper[1]["percentage"], 2))
    print("Average Percentage :", round(average, 2))
    print("Pass Students :", pass_count)
    print("Fail Students :", fail_count)


# Rank List
def show_rank_list():

    if not students:
        print("No Records Found!")
        return

    sorted_students = sorted(
        students.items(),
        key=lambda x: x[1]["percentage"],
        reverse=True
    )

    print("\n===== RANK LIST =====")

    rank = 1

    for roll, data in sorted_students:

        print(
            f"Rank {rank} | "
            f"Roll: {roll} | "
            f"Name: {data['name']} | "
            f"Percentage: {data['percentage']:.2f}"
        )

        rank += 1



# Main Menu
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Class Report")
    print("7. Rank List")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_all()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        class_report()

    elif choice == "7":
        show_rank_list()

    else:
        print(" Invalid Choice!")