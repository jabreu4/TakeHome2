from easygui import *
import sys

while True:
#test
    msgbox("Welcome to Exam #2 Take Home. Please hit ok to enter the image")
    imagePath = fileopenbox()
    print(imagePath)

    msg ="What image processing algorithm you want to  work with?"
    title = "Image Processing Algorithms"
    choices = ["MedianFilter", "WeinerFilter", "MarrHildrethEdgeDetector"]
    choice = choicebox(msg, title, choices)
    print(choice)
    numberThreads = integerbox(msg="What is the number of threads you want to work with"
                  , title = "Number Of Threads"
                  , default = 0
                  , lowerbound = 0
                  , upperbound = 200)
    print(numberThreads)
    numberCores = integerbox(msg="What is the number of cores you want to work with"
                  , title = "Number Of Cores"
                  , default = 0
                  , lowerbound = 0
                  , upperbound = 300)
    print(numberCores)
    numberThreadsPerCore = integerbox(msg="What is the number of threads per core you want to work with"
                  , title = "Number Of Threads per Core"
                  , default = 0
                  , lowerbound = 0
                  , upperbound = 400)
    print(numberThreadsPerCore)

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)

