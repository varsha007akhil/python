
python_students = {"Anu", "Rahul", "Meera"}
data_science_students = {"Rahul", "Meera", "Arjun"}
python_students.add("Vishnu")
data_science_students.remove("Arjun")
both_courses = python_students & data_science_students
print("Students in both courses:", both_courses)
only_python = python_students - data_science_students
print("Only Python students:", only_python)
all_students = python_students | data_science_students
print("All students:", all_students)
course_students = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}
print(course_students)
for course, students in course_students.items():
    print(f"Course: {course}, Students: {students}")
expected_growth = {
    course: students * 2
    for course, students in course_students.items()
}
print("Expected Growth:", expected_growth)