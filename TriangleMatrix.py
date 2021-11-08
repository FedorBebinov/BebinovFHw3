import random

from Matrix import Matrix


class TriangleMatrix(Matrix):
    def __init__(self, dim):
        Matrix.__init__(self, dim)
        self.mtrx = []

    def average(self):
        sum = 0
        for i in range(self.dimension ** 2):
            sum += self.mtrx[i]
        self.aver = sum / self.dimension ** 2
        return self.aver

    def fill(self, inputFile):
        self.mtrx = []
        for i in range(self.dimension):
            self.mtrx += list(map(float, inputFile.readline().split()))

    def rndFill(self):
        for i in range(self.dimension ** 2):
            if i % self.dimension <= i // self.dimension:
                self.mtrx.append(random.uniform(-1000, 1000))
            else:
                self.mtrx.append(0.0)

    def print(self, outputFile):
        iter = 0
        outputFile.write("Triangle Matrix. Size:" + str(self.dimension) + "X" + str(self.dimension) + '\n')
        while iter < self.dimension * self.dimension:
            for i in range(self.dimension):
                outputFile.write("{:7.2f} ".format(self.mtrx[iter]))
                iter += 1
            outputFile.write('\n')
