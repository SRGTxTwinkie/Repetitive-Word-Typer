import pyautogui as pag
import time

def init():
    init = open("init.txt", "r")
    isInit = init.read()
    if isInit == "0":
        file = open("MacroNames.txt", "x")
        file.write("5Colums5Rows;5Colums5RowsToPog;")
        file.close()
        init.close()
        init = open("init.txt", "w")
        init.write("1")
        init.close()
        
    getInfo()



def getInfo():

    print()
    newOrSaved = input("New or saved Macro, (1/2): ")

    if newOrSaved == "2":
        macroNames = open("MacroNames.txt", "r")
        names = macroNames.read().split(';')
        number = 1
        print()
        for i in names:
            if i == "":
                continue
            else:
                print(str(number) + ": " + i)
                number += 1
        print()
            
        macroNames.close()

        print("Use the number correlating")
        macroToUse = input("Which macro to use: ")

        macroUse = open(names[(int(macroToUse) -1)] + ".txt", "r")
        information = macroUse.read().split(',')
        macroUse.close()

        main(information[0], information[1], information[2], int(information[3]), int(information[4]), int(information[5]), information[6])

    else:
        
        toWrite = input("What to write: ")

        placeHolder = input("Are there placeholders, (Yes/No): ")
        
        isAcending = input("Increment each time, (Yes/No): ")

        lineNumber = input("How many lines are you writing: ")
        
        if placeHolder.upper() == "YES":
            placeHolderAmount = input("How many chars: ")
        else:
            placeHolderAmount = -1
            
        if isAcending.upper() == "YES":
            startNumber = input("Starting number to increment: ")
        else:
            startNumber = -1

        isSaved = 0

        main(toWrite, placeHolder, isAcending, lineNumber, placeHolderAmount, startNumber, isSaved);

def main(toWrite, placeHolder, isAcending, lineNumber, placeHolderAmount, startNumber, isSaved):
    print()
    increment = int(startNumber)
    
    for i in range(-5, 0, 1):
        print(str((abs(i))) + " Second(s) Remaining");
        time.sleep(1)

    if placeHolder.upper() == "YES":

        for i in range(int(lineNumber)):
            
            for i in range(int(placeHolderAmount)):
                pag.press("backspace")

            if isAcending.upper() == "YES":
                pag.write(toWrite + str(increment))

                if len(toWrite) < int(placeHolderAmount):
                    for i in range(int(placeHolderAmount) - len(toWrite)):
                        pag.press("space")
                
                pag.press("down")
                increment += 1
                
            else:
                pag.write(toWrite)
                
                if len(toWrite) < int(placeHolderAmount):
                    for i in range(int(placeHolderAmount) - len(toWrite)):
                        pag.press("space")
                        
                pag.press("down")

    else:
        
        for i in range(int(lineNumber)):
            if isAcending.upper() == "YES":
                pag.write(toWrite + str(increment))
                increment += 1
            else:
                pag.write(toWrite)

            pag.press("enter")

    if isSaved == "1":
        getInfo()
    else:
        save = input("Do you want to save this output: ")

    if save.upper() == "YES":
        macroName = input("What to name macro: ")

        macro = [toWrite, placeHolder, isAcending, lineNumber, placeHolderAmount, startNumber]
        
        macroMaker(macro, macroName)

    else:
        getInfo()
    

def macroMaker(toWrite, name):
    file = open(name + ".txt", "x")

    for i in toWrite:
        file.write(str(i) + ",")
        
    file.close()
    file = open(name + ".txt", "a")
    file.write("1")
    file.close()

    macroName = open("MacroNames.txt", "a")
    macroName.write(str(name + ";"))
    macroName.close()
    getInfo()
    

init()

