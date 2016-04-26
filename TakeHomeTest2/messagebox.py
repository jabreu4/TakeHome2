from Tkinter import *
import tkMessageBox

def messageBox(m):
	root = Tk().withdraw()  # hiding the main window

	tkMessageBox.showinfo("Execution in seconds  ", "Execution time = " + str(m)  )

	root.destroy()


