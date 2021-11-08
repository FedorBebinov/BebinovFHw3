import sys

from Container import Container

if __name__ == '__main__':
    if len(sys.argv) == 3:
        inputFileName = sys.argv[1]
        outputFileName = sys.argv[2]
    elif len(sys.argv) == 2:
        inputFileName = sys.argv[1]
        outputFileName = "output.txt"
    elif len(sys.argv) == 1:
        print("Incorrect command line! You must write: python main <inputFileName> [<outputFileName>]")
        exit()

    # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки
    inputFile = open(inputFileName)
    outputFile = open(outputFileName, 'w+')
    elementAmount = int(inputFile.readline())
    if elementAmount < 1:
        print("Incorrect amount of elements")
        exit()
    else:
        elementContainer = Container(elementAmount)
        elementContainer.fill(inputFile)
        elementContainer.print(outputFile)
        elementContainer.printInformation(outputFile)
        elementContainer.removeElementsLowerThanAverage()
        outputFile.write("After removing lower than average elements:\n")
        elementContainer.print(outputFile)
    inputFile.close()
    outputFile.close()

    print('Program has finished correctly')
