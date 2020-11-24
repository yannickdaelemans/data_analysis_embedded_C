import random
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# This is the data analysis for the RAM extension module


calculatedTimeOKWrite = np.array([])
calculatedTimeOKRead = np.array([])
calculatedTimeNW = np.array([])
calculatedTimeNR = np.array([])
calculatedTimeNO = np.array([])
calculatedTimeAllReading = np.array([])
calculatedTimeAllWriting = np.array([])


def getFromFile(fileName, ID):
    home = str(Path.home())
    file = open(home + "\\" + fileName, "r")
    i = 0
    lines = []
    for x in file:
        if i < 8:
            lines.append(x.rstrip())
            i = i + 1
        if i == 8:
            checkLines(lines, ID)
            lines.clear()
            i = i + 1
        elif i == 9:
            i = 0

    file.close()


def checkLines(lines, ID):
    global calculatedTimeOKWrite
    global calculatedTimeNW
    global calculatedTimeOKRead
    global calculatedTimeNR
    global calculatedTimeNO
    global calculatedTimeAllReading
    global calculatedTimeAllWriting

    readWrite = "0"
    if lines[0] != ID:
        print("file ID", lines[0] , "and ID", ID)
        print("Error in file beginning protocol")
        return
    if lines[1] == write:
        readWrite = "Write"
    elif lines[1] == read:
        readWrite = "Read"
    if int(lines[7], 2) != 0:
        print("Error in file ending protocol")
        return

    address = int(lines[2], 2)
    response = lines[3]
    timeBegin = int(lines[4], 2)
    timeEnd = int(lines[5], 2)
    time = int(lines[6], 2)

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

    if readWrite == "Write":
        calculatedTimeAllWriting = np.append(calculatedTimeAllWriting, time)
        if response == OKWrite:
            calculatedTimeOKWrite = np.append(calculatedTimeOKWrite,time)
        elif response == NotWrite:
            calculatedTimeNW = np.append(calculatedTimeNW, time)
    elif readWrite == "Read":
        calculatedTimeAllReading = np.append(calculatedTimeAllReading, time)
        if response == OKRead:
            calculatedTimeOKRead = np.append(calculatedTimeOKRead, time)
        elif response == NotResponse:
            calculatedTimeNR = np.append(calculatedTimeNR, time)
        elif response == WrongResponse or response == AllZeroesResponse:
            checkIfInRange(address)
            calculatedTimeNO = np.append(calculatedTimeNO, time)

    return

def printList():
    print(calculatedTimeOKWrite)


def getListLengths():
    print("The amount of list OK Writing = ", len(calculatedTimeOKWrite))
    print("The amount of list OK Reading = ", len(calculatedTimeOKRead))
    print("The amount of list Not Writing = ", len(calculatedTimeNW))
    print("The amount of list Not Response = ", len(calculatedTimeNR))
    print("The amount of list Wrong reading response = ", len(calculatedTimeNO))
    print()
    print("total amount writings = ", len(calculatedTimeOKWrite) + len(calculatedTimeNW))
    print("total amount Readings = ", len(calculatedTimeOKRead) + len(calculatedTimeNR) + len(calculatedTimeNO))
    print("total amount writings = ", len(calculatedTimeAllWriting))
    print("total amount Readings = ", len(calculatedTimeAllReading))

def getAverage():
    print(calculatedTimeOKWrite.mean())

def checkIfInRange(address):
    if address < 0x2000 or address > 0x37FF:
        print()




def printBarChart():
    ax = plt.subplot()
    (uniqueValues, counts) = np.unique(np.sort(calculatedTimeAllReading), return_counts=True)
    print(uniqueValues)
    print(counts/len(calculatedTimeAllReading))
    x_pos = [i for i, _ in enumerate(np.around(uniqueValues))]

    plt.bar(x_pos, counts/len(calculatedTimeAllReading)*100, width=1)
    plt.xlabel("clock cycles")
    plt.ylabel("amount of tests [%]")
    plt.xticks(x_pos, uniqueValues)
    plt.title("Reading timings", None, 'right', 10)
    labels = np.around(counts/len(calculatedTimeAllReading)*100, 2)

    rects = ax.patches
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
                ha='center', va='bottom')


    plt.show()
    return



write = "0000000000000010"
read = "0000000000000001"
OKWrite = "0101011101001011"
NotWrite = "0101011101001110"
OKRead = "0100101101001111"
NotResponse = "0101001001001110"
WrongResponse = "0100111101001110"
AllZeroesResponse = "0011000000110000"

getFromFile("TesterMSP.txt", "0000000000000000")

#printList()
getListLengths()
getAverage()
printBarChart()
