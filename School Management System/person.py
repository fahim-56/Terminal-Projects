import random
from school import School
class person:
    def __init__(self,name):
        self.name = name

class Teacher(person):
    def __init__(self, name):
        super().__init__(name)
    
    def evaluate_exam(self):
        return random.randint(1,100)
    
class Student(person):
    def __init__(self, name,classroom):
        super().__init__(name)
        self.classroom = classroom
        self.id = id
        self.marks = {}
        self.subject_grade = {}

        self.grade = None

    def final_grade(self):
        sum = 0
        cnt = 0
        fail_falg = False
        for grade in self.subject_grade.values():
            cnt+=1
            if grade == "F":
                fail_falg = True  
            point = School.grade_to_GPA(grade)
            sum +=point
        if sum==0:
            gpa = 0
            self.grade ="F"
        else:
            gpa = sum / len(self.subject_grade) # 7/2 = 3.50
            self.grade = School.value_to_grade(gpa)
        if fail_falg ==True:
            return f"Final Grade : F with GPA = 0.00"
        return f"Final Grade : {self.grade} with GPA = {gpa}"

