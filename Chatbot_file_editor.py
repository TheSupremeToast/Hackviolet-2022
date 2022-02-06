
class Outwriter:

    def __init__(self,fileName="commands.txt"):
        self.out_writer = open(fileName,"a")

    def writeToFile(self, command: str):
        self.out_writer.write(command)

    def writeToFile(self, commandlist: list):
        for c in commandlist:
            self.out_writer.write(c)

    def closeFile(self):
        self.out_writer.close()