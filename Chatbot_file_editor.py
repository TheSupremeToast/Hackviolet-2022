
out_writer = open("commands.txt","w")

def writeToFile(command: str):
    out_writer(command)

def writeToFile(commandlist: list):
    for c in commandlist:
        out_writer(c)