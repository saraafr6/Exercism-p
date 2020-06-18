class School():
    def __init__(self):
        self.students_grade = {}

    def add_student(self, name, grade):
        self.students_grade[name] = grade

    def roster(self):
        student=list(self.students_grade.items())
        sorted_student=sorted(student,key=lambda x:(x[1],x[0]))
        new_list=[]
        for i in range(len(sorted_student)):
                new_list.append(sorted_student[i][0])
        return new_list

    def grade(self, grade_number):
        return [i for i in sorted(self.students_grade.keys()) if self.students_grade[i] == grade_number]