
frontend_students = {"varshini", "varsha", "karunya", "prardhana"}
backend_students = {"saran", "adharsh", "Vishnu"}
backend_students.add("Sneha")
frontend_students.remove("prardhana")
both_courses = frontend_students & backend_students
print("Students in both courses:", both_courses)
only_backend = backend_students - frontend_students
print("Only Backend students:", only_backend)
all_students = frontend_students | backend_students
print("Total unique students:", len(all_students))
course_students = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}
for course, students in course_students.items():
    print(f"Course: {course}, Students: {students}")

course_with_fullstack = course_students.copy()

course_with_fullstack["Fullstack"] = (
    course_students["Frontend"] + course_students["Backend"]
)

print("Course with Fullstack:", course_with_fullstack)