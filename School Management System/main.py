from school import School
from person import Teacher,Student
from Subject import Subject
from classroom import classroom

myschool = School("ABC school","Dhaka")
cls8 = classroom("Eight")
cls9 = classroom("Nine")
cls10 = classroom("Ten")
myschool.add_classroom(cls8)
myschool.add_classroom(cls9)
myschool.add_classroom(cls10)

st1 = Student("Student 1",cls8)
st2 = Student("Student 2",cls8)
st3 = Student("Student 3",cls9)
st4 = Student("Student 4",cls10)
st5 = Student("Student 5",cls10)

myschool.add_student(st1)
myschool.add_student(st2)
myschool.add_student(st3)
myschool.add_student(st4)
myschool.add_student(st5)

tcr1 = Teacher("Masud sir ")
tcr2 = Teacher("Murad sir ")
tcr3 = Teacher("Al Imtiaz sir ")
tcr4 = Teacher("Sakib sir ")

sbj1 = Subject("English",tcr1)
sbj2 = Subject("Math",tcr2)
sbj3 = Subject("Physics",tcr3)
sbj4 = Subject("Chemistry",tcr4)

myschool.add_teacher(sbj1,tcr1)
myschool.add_teacher(sbj2,tcr2)
myschool.add_teacher(sbj3,tcr3)
myschool.add_teacher(sbj4,tcr4)

cls8.add_subject(sbj1)
cls9.add_subject(sbj2)
cls9.add_subject(sbj3)
cls10.add_subject(sbj3)
cls10.add_subject(sbj4)

cls8.take_exam()
cls9.take_exam()
cls10.take_exam()
print(myschool)