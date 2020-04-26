import random
import pandas
import numpy as np
from pathlib import Path

calculatedTime = np.array([])


def getFromFile(fileName, ID):
    home = str(Path.home())
    file = open(home + "\\" + fileName, "r")
    i = 0
    lines = []
    for x in file:
        print(x)
        lines.append(x.rstrip())
        i = i + 1
        if i == 5:
            print("here")
            i = 0
            checkLines(lines, ID)
            lines.clear()

    #for x in file:

    file.close()


def checkLines(lines, ID):
    global calculatedTime
    if lines[0] != ID:
        print("file ID", lines[0] , "and ID", ID)
        print("Error in file, ID")
        return
    elif int(lines[4], 2) != 0:
        print("Error in file ending protocol")
        return
    timeBegin = int(lines[1], 2)
    timeEnd = int(lines[2], 2)
    time = int(lines[3], 2)

    calculate = timeEnd - timeBegin

    #if negative, compute two's complement
    if calculate < 0:
        calculate = (calculate * (-1)) - (1 << 16)

    if abs(calculate) != abs(time):
        print("Error in file calculation")
        print("time begin:", timeBegin)
        print("time end:", timeEnd)
        print("calculated:", calculate)
        print("time:", time)
        return

    calculatedTime = np.append(calculatedTime, time)
    print("line put in list")
    return


def getListLength():
    print(len(calculatedTime))
    return len(calculatedTime)

def getAverage():
    print(calculatedTime.mean())
    return calculatedTime.mean()


def debugFillList():
    global calculatedTime
    for i in range(0, 100):
        n = random.randint(1, 20)
        calculatedTime = np.append(calculatedTime, n)
    print(calculatedTime)


#getFromFile("name.txt", "0000000000000000")
#For debugging
debugFillList()
getListLength()
getAverage()
