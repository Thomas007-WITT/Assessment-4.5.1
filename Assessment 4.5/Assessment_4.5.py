from tkinter import *
import pyodbc
import Assessment_4 as cl
from Assessment_4 import BackEnd

# front end

dget1 = Tk()
    
dget1.title("Assessment 4 Main")

# create buttons

allRecords = Button(dget1, text="All Records", command=BackEnd.allRec).grid(row=5, column=1, padx=10, pady=5)
posGrowth = Button(dget1, text="Positive Growth", command=BackEnd.posGrowth).grid(row=5, column=3, padx = 10, pady=5)
queryBtn = Button(dget1, text="Query Record by Date").grid(row=5, column=4, padx = 10, pady = 5)
countBtn = Button(dget1, text="Count Companies Between Date").grid(row=10, column=3, padx = 10, pady=5)

dget1.mainloop()