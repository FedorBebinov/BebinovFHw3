import random

from DiagonalMatrix import DiagonalMatrix
from SquareMatrix import SquareMatrix
from TriangleMatrix import TriangleMatrix


class Container:
    def __init__(self, amount):
        self.matrices = []
        self.amount = amount
        self.totalAver = 0

    def fill(self, inputFile):
        if self.amount > 100 or self.amount < 1:
            print("Incorrect amount")
            inputFile.close()
            exit()
        # если количество элементов, указанных в файле больше 10, происходит рандомная генерация элементов
        if self.amount > 10:
            for i in range(self.amount):
                matrType = random.randint(0, 2)
                if matrType == 0:
                    self.matrices.append(SquareMatrix(random.randint(1, 10)))
                    self.matrices[i].rndFill()
                elif matrType == 1:
                    self.matrices.append(DiagonalMatrix(random.randint(1, 10)))
                    self.matrices[i].rndFill()
                elif matrType == 2:
                    self.matrices.append(TriangleMatrix(random.randint(1, 10)))
                    self.matrices[i].rndFill()
        else:
            try:
                for i in range(self.amount):
                    matrType, dim = map(int, inputFile.readline().split())
                    if matrType > 2 or matrType < 0 or dim < 1 or dim > 100:
                        print("Incorrect matrix params")
                        exit()
                    if matrType == 0:
                        self.matrices.append(SquareMatrix(dim))
                        self.matrices[i].fill(inputFile)
                    elif matrType == 1:
                        self.matrices.append(DiagonalMatrix(dim))
                        self.matrices[i].fill(inputFile)
                    elif matrType == 2:
                        self.matrices.append(TriangleMatrix(dim))
                        self.matrices[i].fill(inputFile)
            except Exception:
                print("File error")
                inputFile.close()
                exit()

    def average(self):
        sum = 0
        length = 0
        for i in range(self.amount):
            sum += self.matrices[i].average() * self.matrices[i].dimension * self.matrices[i].dimension
            length += self.matrices[i].dimension * self.matrices[i].dimension
        self.totalAver = sum / length
        return self.totalAver

    def printInformation(self, outputFile):
        for i in range(self.amount):
            outputFile.write("Average of element  " + str(i + 1) + " = "
                             + "{:0.3f} ".format(self.matrices[i].average()) + '\n')
        outputFile.write("Total average = " + "{:0.3f} ".format(self.average()) + '\n\n')

    def removeElementsLowerThanAverage(self):
        elemsAverage = self.totalAver
        i = 0
        while i < len(self.matrices):
            if self.matrices[i].aver + 0.0000001 < elemsAverage:
                self.matrices.pop(i)
            else:
                i += 1
        self.amount = len(self.matrices)

    def print(self, outputFile):
        try:
            outputFile.write("Amount of elements: " + str(len(self.matrices)) + '\n\n')
            for i in range(self.amount):
                self.matrices[i].print(outputFile)
                outputFile.write('\n')
        except FileNotFoundError:
            print("File does not exist")
            outputFile.close()
            exit()
