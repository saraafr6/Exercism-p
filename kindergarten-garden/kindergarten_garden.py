class Garden:
    gardenplants = {'R': 'Radishes', 'G': 'Grass', 'C': 'Clover', 'V': 'Violets'}
    studentsname = [ "Alice",  "Bob",   "Charlie",   "David",  "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph",  "Kincaid", "Larry" ]

    def __init__(self, diagram, students = studentsname):
        self.diagram = [list(x) for x in diagram.split("\n")]
        self.students = sorted(students)

    def plants(self, student):
        index_of_student = self.students.index(student) * 2 
        studentPlants=[]
        for i in range(2):
          studentPlants += self.diagram[i][index_of_student:index_of_student+2] 
        return [Garden.gardenplants[x] for x in studentPlants]