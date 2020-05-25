class Matrix:
    def __init__(self, matrix_string):
        myrow=matrix_string.split("\n")
        self.mymatrix=[[int(col) for col in row.split()] for row in myrow]

    def row(self, index):
        return self.mymatrix[index-1]

    def column(self, index):
        return [i[index-1] for i in self.mymatrix]