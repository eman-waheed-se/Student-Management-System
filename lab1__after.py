# Student Record Management System

def get_student_record():
    """Take student information from the user."""
    student_name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    marks = int(input("Enter marks: "))

    return student_name, roll_number, marks


def display_student_record(student_name, roll_number, marks):
    """Display student details and result."""
    print("\n--- Student Record ---")
    print("Student Name:", student_name)
    print("Roll Number:", roll_number)
    print("Marks:", marks)

    if marks >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")


def main():
    student_name, roll_number, marks = get_student_record()
    display_student_record(student_name, roll_number, marks)


main()