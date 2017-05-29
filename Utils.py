import sys


class Utils:
    @staticmethod
    def writeInFile(str, fileName="saida.dot"):
        try:
            # open file stream
            file = open(fileName, "w")
            file.write("digraph G{")
            file.write(str)
            file.write("}")
        except IOError:
            print("There was an error writing to", fileName)
            sys.exit()

    @staticmethod
    def loadStringFromFile(nameOfFile):
        try:
            file = open(nameOfFile, "r")
        except IOError:
            print("Error in opening File")
        textOfFile = file.read()
        file.close()
        return textOfFile
