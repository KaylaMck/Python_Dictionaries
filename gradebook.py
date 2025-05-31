student_grades = {}

def add_student(name, grade):
    student_grades[name] = grade
    print(f"'{name}' was added to the gradebook and received a {grade}.")

def removed_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"'{name}' was removed from the gradebook")
    else:
        print(f"'{name}' was not found")

def display_students():
    print("Student Grades:")
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")

def update_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s grade has been updated to a {grade}.")
    else:
        print(f"{name} not found.")

add_student("Alice", "90")
add_student("Bob", "65")
add_student("Charlie", "88")

display_students()

update_grade("Alice", "99")

display_students()

removed_student("Bob")

display_students()