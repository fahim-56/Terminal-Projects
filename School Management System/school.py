class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.teachers = {} 
        self.classrooms = {}

    def add_classroom(self,classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self,subject,teacher):
        self.teachers[subject] = teacher

    def add_student(self,student):
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)

    @staticmethod
    def grade_calculation(mark):
        if(mark < 0 or mark >100):
            return("Invalid input!")
        elif mark >=80 and mark <=100:
            return("A+")
        elif mark >=70 and mark <80:
            return("A")
        elif mark >=60 and mark <70:
            return("A-")
        elif mark >=50 and mark <60:
            return("B")
        elif mark >=40 and mark <50:
            return("C")
        elif mark >=33 and mark <40:
            return("D")
        else:
            return "F"
        
    @staticmethod
    def value_to_grade(value):
        if(value < 0 or value >5.00):
            return("Invalid input!")
        elif value == 5.00:
            return "A+"
        elif value >=4.00 and value <5.00:
            return("A")
        elif value >=3.50 and value <4.00:
            return("A-")
        elif value >=3.00 and value <3.50:
            return("B")
        elif value >=2.00 and value <3.00:
            return("C")
        elif value >=1.00 and value <2.00:
            return("D")
        else:
            return "F"
        
    @staticmethod
    def grade_to_GPA(grade):
        grade_map ={
            "A+" : 5.00,
            "A" : 4.00,
            "A-" : 3.50,
            "B" : 3.00,
            "C" : 2.00,
            "D" : 1.00,
            "F" : 0.00
        }
        return grade_map[grade]
    
    def __repr__(self):
        print("---All Classes---")
        for key in self.classrooms.keys():
            print(key)
        
        result = ""
        for key , value in self.classrooms.items():
            result += f"Class {key}'s students :\n"
            for student in value.students:
                result +=f"{student.name}\n"
        print(result)

        subject = ""
        for key , value in self.classrooms.items():
            subject += f"Class {key}'s subject : \n"
            for sub in value.subjects:
                subject +=f"{sub.name}\n"
        print(subject)

        print("Students results:\n")
        for key,val in self.classrooms.items():
            for student in val.students:
                print(student.name)
                for k,v in student.marks.items():
                    print(k,v,student.subject_grade[k])
                # print("Final Grade :",end =" ")
                print(student.final_grade())
        return ""