"""
Code illustrating a vilation of the single responsibility principle (Solid).
"""


class Student:
    """Class to represent students."""
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = []

    def add_grade(self, grade):
        """Add grade."""
        self.grades.append(grade)

    def generate_report(self):
        """Generate a report on this student."""
        # Violation of SRP: Mixing student information and report generation
        average_grade = sum(self.grades) / len(self.grades)
        return f"Student: {self.name}, Roll Number: {self.roll_number}, Average Grade: {average_grade}"


class Classroom:
    """Class to represent classrooms."""
    def __init__(self):
        self.students = []

    def add_student(self, student):
        """Add student to this classroom."""
        self.students.append(student)

    def generate_student_report(self, student):
        """Generate a student report."""
        average_grade = sum(student.grades) / len(student.grades)
        return f"Student: {student.name}, Roll Number: {student.roll_number}, Average Grade: {average_grade}"


class Teacher:
    """Class to represent teachers."""
    def __init__(self):
        self.classroom = Classroom()

    def add_student(self, student):
        """Add a student to a classroom."""
        self.classroom.add_student(student)

    def generate_student_report(self, student):
        """Generate a student report."""
        # Violation of SRP: Teacher is generating the student report
        average_grade = sum(student.grades) / len(student.grades)
        return f"Student: {student.name}, Roll Number: {student.roll_number}, Average Grade: {average_grade}"


# Example usage:
student1 = Student("Alice", "A101")
student1.add_grade(1)
student1.add_grade(2)
student1.add_grade(1)

student2 = Student("Bob", "B202")
student2.add_grade(1)
student2.add_grade(1)
student2.add_grade(3)

teacher = Teacher()
teacher.add_student(student1)
teacher.add_student(student2)

for student in teacher.classroom.students:
    report = teacher.generate_student_report(student)
    print(report)
