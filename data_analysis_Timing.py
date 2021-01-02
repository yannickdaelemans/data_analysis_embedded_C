import random
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# This is the data analysis for the timings
# protocol will look like:
# 1.    0xFFFF
# 2.    ID of the method tested
# 3.    timer_begin
# 4.    timer_end
# 5.    time
# 6.    0xFFFF

calculatedTimeuintfun = np.array([])
calculatedTimeintfun = np.array([])
calculatedTimeuscfun = np.array([])
calculatedTimescfun = np.array([])
calculatedTimecfun = np.array([])
calculatedTimesint8fun = np.array([])
calculatedTimeusint8fun = np.array([])

calculatedTimefunction_no_constants = np.array([])
calculatedTimefunction_constants = np.array([])
calculatedTimeadd = np.array([])
calculatedTimeaddconst = np.array([])
calculatedTimefunction_constants_ptr = np.array([])
calculatedTimeexamplefunction_ptr_constants = np.array([])

calculatedTimeconversion_union = np.array([])
calculatedTimeconversion_shift = np.array([])

calculatedTimecompare_to_zero = np.array([])
calculatedTimecompare_to_reg = np.array([])
calculatedTimecompare_to_num = np.array([])
calculatedTimenot_compare_to_zero = np.array([])
calculatedTimebigger_to_zero = np.array([])
calculatedTimesmaller_to_zero = np.array([])


calculatedTimewhile_function = np.array([])
calculatedTimewhile_function_0 = np.array([])
calculatedTimewhile_function_const = np.array([])


# reading from the file, putting it in an array, and checking the lines afterwards
def getFromFile(fileName, ID):
    home = str(Path.home())
    file = open(home + "\\" + fileName, "r")
    i = 0
    lines = []
    for x in file:
        if i < 6:
            lines.append(x.rstrip())
            i = i + 1
        if i == 6:
            checkLines(lines, ID)
            lines.clear()
            i = 0
        elif i == 7:
            i = 0

    file.close()

#check if the lines are okay, and put in the right array
def checkLines(lines, ID):
    global calculatedTimeuintfun
    global calculatedTimeintfun
    global calculatedTimeuscfun
    global calculatedTimescfun
    global calculatedTimecfun
    global calculatedTimesint8fun
    global calculatedTimeusint8fun

    global calculatedTimefunction_no_constants
    global calculatedTimefunction_constants
    global calculatedTimeadd
    global calculatedTimeaddconst
    global calculatedTimefunction_constants_ptr
    global calculatedTimeexamplefunction_ptr_constants

    global calculatedTimeconversion_union
    global calculatedTimeconversion_shift

    global calculatedTimecompare_to_zero
    global calculatedTimecompare_to_reg
    global calculatedTimecompare_to_num
    global calculatedTimenot_compare_to_zero
    global calculatedTimebigger_to_zero
    global calculatedTimesmaller_to_zero

    global calculatedTimewhile_function
    global calculatedTimewhile_function_0
    global calculatedTimewhile_function_const

    if lines[0] != ID:
        print("file ID", lines[0] , "and ID", ID)
        print("Error in file beginning protocol")
        return

    if lines[5] != ID:
        print("Error in file ending protocol")
        print(lines[5])
        return

    timeBegin = int(lines[2], 2)
    timeEnd = int(lines[3], 2)
    time = int(lines[4], 2)

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

    if lines[1] == uintfun:
        calculatedTimeuintfun  = np.append(calculatedTimeuintfun, time)
    elif lines[1] == intfun:
        calculatedTimeintfun  = np.append(calculatedTimeintfun, time)
    elif lines[1] == uscfun:
        calculatedTimeuscfun  = np.append(calculatedTimeuscfun, time)
    elif lines[1] == scfun:
        calculatedTimescfun  = np.append(calculatedTimescfun, time)
    elif lines[1] == cfun:
        calculatedTimecfun = np.append(calculatedTimecfun, time)
    elif lines[1] == sint8fun:
        calculatedTimesint8fun = np.append(calculatedTimesint8fun, time)
    elif lines[1] == usint8fun:
        calculatedTimeusint8fun = np.append(calculatedTimeusint8fun, time)

    elif lines[1] == function_no_constants:
        calculatedTimefunction_no_constants = np.append(calculatedTimefunction_no_constants , time)
    elif lines[1] == function_constants:
        calculatedTimefunction_constants = np.append(calculatedTimefunction_constants, time)
    elif lines[1] == add:
        calculatedTimeadd = np.append(calculatedTimeadd, time)
    elif lines[1] == addconst:
        calculatedTimeaddconst = np.append(calculatedTimeaddconst, time)
    elif lines[1] == function_constants_ptr:
        calculatedTimefunction_constants_ptr = np.append(calculatedTimefunction_constants_ptr, time)
    elif lines[1] == function_ptr_constants:
        calculatedTimeexamplefunction_ptr_constants = np.append(calculatedTimeexamplefunction_ptr_constants, time)

    elif lines[1] == conversion_union:
        calculatedTimeconversion_union = np.append(calculatedTimeconversion_union, time)
    elif lines[1] == conversion_shift:
        calculatedTimeconversion_shift = np.append(calculatedTimeconversion_shift, time)

    elif lines[1] == compare_to_zero:
        calculatedTimecompare_to_zero = np.append(calculatedTimecompare_to_zero, time)
    elif lines[1] == compare_to_reg:
        calculatedTimecompare_to_reg = np.append(calculatedTimecompare_to_reg, time)
    elif lines[1] == compare_to_num:
        calculatedTimecompare_to_num = np.append(calculatedTimecompare_to_num, time)
    elif lines[1] == not_compare_to_zero:
        calculatedTimenot_compare_to_zero = np.append(calculatedTimenot_compare_to_zero, time)
    elif lines[1] == bigger_to_zero:
        calculatedTimebigger_to_zero = np.append(calculatedTimebigger_to_zero, time)
    elif lines[1] == smaller_to_zero:
        calculatedTimesmaller_to_zero = np.append(calculatedTimesmaller_to_zero, time)

    elif lines[1] == while_function:
        calculatedTimewhile_function = np.append(calculatedTimewhile_function, time)
    elif lines[1] == while_function_0:
        calculatedTimewhile_function_0 = np.append(calculatedTimewhile_function_0, time)
    elif lines[1] == while_function_const:
        calculatedTimewhile_function_const = np.append(calculatedTimewhile_function_const, time)

    return


def getListLengths():
    print("The amount of list uintfun   = ", len(calculatedTimeuintfun))
    print("The amount of list intfun    = ", len(calculatedTimeintfun))
    print("The amount of list uscfun    = ", len(calculatedTimeuscfun))
    print("The amount of list scfun     = ", len(calculatedTimescfun))
    print("The amount of list cfun      = ", len(calculatedTimecfun))
    print("The amount of list sint8fun  = ", len(calculatedTimesint8fun))
    print("The amount of list usint8fun = ", len(calculatedTimeusint8fun))
    print("The amount of list function_no_constants    = ", len(calculatedTimefunction_no_constants))
    print("The amount of list function_constants       = ", len(calculatedTimefunction_constants))
    print("The amount of list add                      = ", len(calculatedTimeadd))
    print("The amount of list addconst                 = ", len(calculatedTimeaddconst))
    print("The amount of list function_constants_ptr   = ", len(calculatedTimefunction_constants_ptr))
    print("The amount of list function_ptr_constants   = ", len(calculatedTimeexamplefunction_ptr_constants))
    print("The amount of list union     = ", len(calculatedTimeconversion_union))
    print("The amount of list shift     = ", len(calculatedTimeconversion_shift))
    print("The amount of list compare to               = ", len(calculatedTimecompare_to_zero))
    print("The amount of list compare to reg           = ", len(calculatedTimecompare_to_reg))
    print("The amount of list compare to num           = ", len(calculatedTimecompare_to_num))
    print("The amount of list bigger than 0            = ", len(calculatedTimebigger_to_zero))
    print("The amount of list smaller than 0           = ", len(calculatedTimesmaller_to_zero))
    print("The amount of list not 0                    = ", len(calculatedTimenot_compare_to_zero))
    print("The amount of list while_function           = ", len(calculatedTimewhile_function))
    print("The amount of list while_function_0         = ", len(calculatedTimewhile_function_0))
    print("The amount of list while_function_const     = ", len(calculatedTimewhile_function_const))

def getAverage():
    print("The average of list uintfun   = ", calculatedTimeuintfun.mean())
    print("The average of list intfun    = ", calculatedTimeintfun.mean())
    print("The average of list uscfun    = ", calculatedTimeuscfun.mean())
    print("The average of list scfun     = ", calculatedTimescfun.mean())
    print("The average of list cfun      = ", calculatedTimecfun.mean())
    print("The average of list sint8fun  = ", calculatedTimesint8fun.mean())
    print("The average of list usint8fun = ", calculatedTimeusint8fun.mean())
    print("The average of list function_no_constants    = ", calculatedTimefunction_no_constants.mean())
    print("The average of list function_constants       = ", calculatedTimefunction_constants.mean())
    print("The amount of list add                       = ", calculatedTimeadd.mean())
    print("The amount of list addconst                  = ", calculatedTimeaddconst.mean())
    print("The average of list function_constants_ptr   = ", calculatedTimefunction_constants_ptr.mean())
    print("The average of list function_ptr_constants   = ", calculatedTimeexamplefunction_ptr_constants.mean())
    print("The average of list union     = ", calculatedTimeconversion_union.mean())
    print("The average of list shift     = ", calculatedTimeconversion_shift.mean())
    print("The average of list compare to               = ", calculatedTimecompare_to_zero.mean())
    print("The average of list compare to reg           = ", calculatedTimecompare_to_reg.mean())
    print("The average of list compare to num           = ", calculatedTimecompare_to_num.mean())
    print("The average of list bigger than 0            = ", calculatedTimebigger_to_zero.mean())
    print("The average of list smaller than 0           = ", calculatedTimesmaller_to_zero.mean())
    print("The average of list not 0                    = ", calculatedTimenot_compare_to_zero.mean())
    print("The average of list while_function           = ", calculatedTimewhile_function.mean())
    print("The average of list while_function_0         = ", calculatedTimewhile_function_0.mean())
    print("The average of list while_function_const     = ", calculatedTimewhile_function_const.mean())



#method ID's
# sign extensions
uintfun = "0000000000000001"
intfun = "0000000000000010"
uscfun = "0000000000000011"
scfun = "0000000000000100"
cfun = "0000000000000101"
sint8fun = "0000000000000110"
usint8fun = "0000000000000111"
# constants
function_no_constants = "0000000000001000"
function_constants = "0000000000001001"
add = "0000000000010001"
addconst = "0000000000010010"
function_constants_ptr = "0000000000001010"
function_ptr_constants = "0000000000001011"
# unions
conversion_union = "0000000000001100"
conversion_shift = "0000000000001101"
# compare to 0
compare_to_zero = "0000000000010011"
compare_to_reg = "0000000000010100"
compare_to_num = "0000000000010101"
not_compare_to_zero = "0000000000010110"
bigger_to_zero = "0000000000010111"
smaller_to_zero = "0000000000011000"
# loops
while_function = "0000000000001110"
while_function_0 = "0000000000001111"
while_function_const = "0000000000010000"


getFromFile("big_test.txt", "1111111111111111")

#printList()
getListLengths()
getAverage()