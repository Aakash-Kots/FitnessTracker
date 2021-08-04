import tkinter.ttk
from tkinter import *
from exercises import exercises
import mysql.connector as mysql
from tkcalendar import Calendar
import matplotlib.pyplot as plt
import pandas as pd
import os
from tkinter.ttk import *
from dotenv import load_dotenv

load_dotenv()
master = Tk()

master.geometry("600x350")
master.configure(bg='turquoise')
options = exercises



def connectDB():
    con = mysql.connect(host='localhost', user='root', password=os.getenv('password'), database='FitnessDB')
    custor = con.cursor()
    return custor



def save(reps, exercise, date, weight):
    label1.config(text=clicked.get() + ' - ' + str(repCounter.get()) + ' reps')
    date = date
    Exercise = exercise
    Repetitions = reps
    weight = weight
    con = mysql.connect(host='localhost', user='root', password=os.getenv('password'), database='FitnessDB')
    custor = con.cursor()
    custor.execute("insert into FitnessTB (Exercise,Weight, Reps, Date) values('" + str(Exercise) + "','" + weight + "','" + str(Repetitions) + "','" + str(date) + "')")
    custor.execute("commit")
    con.close()


def DoPlot(var, weight):
    var = var.get()
    con = mysql.connect(host='localhost', user='root', password=os.getenv('password'), database='FitnessDB')
    custor = con.cursor()
    custor.execute(f"SELECT * FROM FitnessTB WHERE Exercise='{var}'")
    value = custor.fetchall()
    x = []
    y = []

    for data in value:
        if int(data[2]) == int(weight):
            x.append(data[4])
            y.append(int(data[3]))


    # x = value[0]
    # y = value[1]
    plt.plot(x, y)
    plt.title(var)
    plt.xlabel('Weight')
    plt.ylabel('Reps')
    plt.show()
    con.close()


def showAllData():
    con = mysql.connect(host='localhost', user='root', password=os.getenv('password'), database='FitnessDB')
    custor = con.cursor()
    custor.execute("SELECT * FROM FitnessTB")
    Exercise = []
    Weight = []
    Repetitions = []
    Date = []
    values = custor.fetchall()
    for value in values:
        Weight.append(value[2])
        Exercise.append(value[1])
        Repetitions.append(value[3])
        Date.append(value[4])
    d = {'Exercise':Exercise,'Weight':Weight,'Repetitions':Repetitions,'Data':Date}
    df = pd.DataFrame(data=d)
    file_name = 'AllData.xlsx'
    df.to_excel(file_name)

    os.system(os.getenv('dataurl'))


def openPlot():
    plot = Toplevel()
    plot.title('Plotting Page')
    dropVar2 = StringVar()
    drop2 = OptionMenu(plot, dropVar2, *options).grid(column=0)
    weightToPlot = Spinbox(plot,from_=0,to_=1000,width=4)
    weightToPlot.grid(row=1,column=0)
    drawGraph = Button(plot, text='Plot Graph', command=lambda: DoPlot(dropVar2, weightToPlot.get()))
    drawGraph.grid(row=2, column=0)


exerciseLabel = Label(master,text='Chose your exercise').grid(row=0,column=0)
calenderLabel = Label(master,text='Chose the date').grid(row=0,column=1, pady=(5,5))
weightLabel = Label(master,text='Chose the weight').grid(row=0,column=2, pady=(5,5))
repsLabel = Label(master,text='Chose the reps').grid(row=0,column=3, pady=(5,5))



clicked = StringVar()
btn = Button(master, text='Open Plot Page', command=openPlot).grid(column=2, row=2,pady=(5,5))
clicked.set("Exercise")
cal = Calendar(master,selectmode='day',year=2021,mosnth=8,day=1)
cal.grid(row=1,column=1)
reps = IntVar()

drop = OptionMenu(master,clicked,*options)
drop.grid(row=1,column=0,pady=(0,0))
showAll = Button(master,text='Show all data', command=showAllData).grid(row=2, column=1,pady=(5,5))

weightVal = Spinbox(master,from_=0, to_=1000, width=2)
weightVal.grid(row=1,column=2,padx=(5,5))

repCounter = Spinbox(master,from_=0, to_=99, width=2)
repCounter.grid(row=1,column=3)

button = Button(master,text='Log Data',command=lambda: save(repCounter.get(),clicked.get(),cal.get_date(),weightVal.get())).grid(row=2,column=0,pady=(5,5))
# button2 = Button(master,text='Plot', command=newWindow).grid()
label1 = Label(master,text="Select exercise,weight,reps and date")

label1.grid(pady=(10,10), padx=(10,10),row=3,column=1)

mainloop()

