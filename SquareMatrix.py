import random

from Matrix import Matrix


class SquareMatrix(Matrix):
    def __init__(self, dim):
        Matrix.__init__(self, dim)
        self.mtrx = []

    def average(self):
        sum = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                sum += self.mtrx[i][j]
        self.aver = sum / self.dimension ** 2
        return self.aver

    def fill(self, inputFile):
        self.mtrx = []
        for i in range(self.dimension):
            self.mtrx.append(list(map(float, inputFile.readline().split())))

    def rndFill(self):
        for i in range(self.dimension):
            self.mtrx.append([])
            for j in range(self.dimension):
                self.mtrx[i].append(random.uniform(-1000, 1000))

    def print(self, outputFile):
        outputFile.write("Square Matrix. Size:" + str(self.dimension) + "X" + str(self.dimension) + '\n')
        for i in range(self.dimension):
            for j in range(self.dimension):
                outputFile.write("{:7.2f} ".format(self.mtrx[i][j]))
            outputFile.write('\n')
