from person import Teacher
from school import School
class Subject:
    def __init__(self,name,teacher):
        self.name = name
        self.teacher = teacher
    
    def exam(self,students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.grade_calculation(mark)
            