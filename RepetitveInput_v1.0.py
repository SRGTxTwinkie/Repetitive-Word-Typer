import pyautogui as pag #pyautogui is required, that's why there is a compiled version
import time #count down timer only

def getInfo(): #gets all the basic information for the program

    #these are aligned like this so the user doesn't have to switch from
    #the keypad and keyboard
    #letters go first and numbers go second

    print()
    toWrite = input("What to write: ")

    placeHolder = input("Are there placeholders, (Yes/No): ")
    
    isAcending = input("Increment each time, (Yes/No): ")

    lineNumber = input("How many lines are you writing: ")
    
    if placeHolder.upper() == "YES": #I couldn't get true and false to work, so yes and no work too I guess
        placeHolderAmount = input("How many chars: ")
    else:
        placeHolderAmount = -1 #need to be defined because I pass them
        
    if isAcending.upper() == "YES":
        startNumber = input("Starting number to increment: ")
    else:
        startNumber = -1

    main(toWrite, placeHolder, isAcending, lineNumber, placeHolderAmount, startNumber);

def main(toWrite, placeHolder, isAcending, lineNumber, placeHolderAmount, startNumber):
    print()
    increment = int(startNumber)
    
    for i in range(-5, 0, 1): #countdown timer
        print(str((abs(i))) + " Second(s) Remaining");
        time.sleep(1)

    if placeHolder.upper() == "YES":

        for i in range(int(lineNumber)):

            #this is the place holder write function
            #the only difference is it deletes the placeholder before it writes
            
            for i in range(int(placeHolderAmount)):
                pag.press("backspace")

            if isAcending.upper() == "YES":
                pag.write(toWrite + str(increment))
                pag.press("down")
                increment += 1 #if we are incrementing it just goes up one everytime
                
            else:
                pag.write(toWrite)
                pag.press("down")

    else:

        #does the same thing as the top except no delete
        
        for i in range(int(lineNumber)):
            if isAcending.upper() == "YES":
                pag.write(toWrite + str(increment))
                increment += 1
            else:
                pag.write(toWrite)

            pag.press("enter")

    getInfo() #loops back to top


getInfo()
