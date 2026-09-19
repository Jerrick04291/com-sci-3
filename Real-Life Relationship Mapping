class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def enroll(self, course):
        course.add_student(self)

    def leave_course(self, course):
        course.students.remove(self)

student1 = Student("001", "Jerrick Jaralve")
course1 = Course("Comsci")

student1.enroll(course1)

print(course1.course_name)
print(course1.students[0].student_name)

student1.leave_course(course1)

print(len(course1.students))
