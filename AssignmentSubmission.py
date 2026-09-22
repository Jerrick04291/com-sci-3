class AssignmentSubmission:
    def __init__(self, student_name:str, student_id:str, assignment_title, due_date:str,):
        self._assignment_title = assignment_title
        self.student_id = student_id
        self.student_name = student_name
        self._due_date = due_date
        self.__is_submitted = bool
        self.__grade = 0.0
        self.__submitted_files = [str]

    def __validate_grade(self, score:float):
        if not 0 <= score <= 100:
            raise ValueError("Grade must be between 0 and 100")
        return score

    def __check_submission_status(self):
        if not self.__is_submitted:
            print("Assignment has not been submitted yet.")
        return self.__is_submitted

    def __is_duplicate(self, filename: str):
        if filename in self.__submitted_files:
            print(f"File '{filename}' has already been submitted.")
        return False

    def add_file(self, filename: str):
        self.__is_duplicate(filename)
        self.__submitted_files.append(filename)

    def remove_file(self, filename:str):
        self.__check_submission_status()
        if filename in self.__submitted_files:
            self.__submitted_files.remove(filename)
        else:
            print(f"File '{filename}' not found in the submission.")

    def assign_grade(self, score: float):
        self.__validate_grade(score)
        self.__grade = score

    def get_grade(self):
        self.__check_submission_status()
        return self.__grade

    def view_files(self):
        self.__check_submission_status()
        return self.__submitted_files

    def get_status_report(self):
        status = "Submitted" if self.__is_submitted else "Not Submitted"
        return {
            "Assignment Title": self._assignment_title,
            "Student ID": self.student_id,
            "Student Name": self.student_name,
            "Due Date": self._due_date,
            "Submission Status": status,
            "Grade": self.__grade if self.__is_submitted else "Not Graded",
            "Submitted Files": self.__submitted_files if self.__is_submitted else []
        }


print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmission(student_name="Juan Dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date="2026-10-01")
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-101", due_date="2026-10-01")
print()

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.docx")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py")  # This should not be added again
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")  # This should not be allowed
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
