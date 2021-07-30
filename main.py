from tkinter import *
from exercises import exercises
master = Tk()
print('Hello world!')
master.geometry("200x200")
master.configure(bg='blue')


def show():
    label1.config(text=clicked.get() + ' - ' + str(reps.get()) + ' reps')


options = exercises

clicked = StringVar()

clicked.set("Exercise")

reps = IntVar()


drop = OptionMenu(master,clicked,*options)
drop.grid(padx=(10,10))


repCounter = Spinbox(master,from_=0, to_=99, width=2)
repCounter.grid(row=0,column=1)

button = Button(master,text='Click',command=show,bg="blue").grid(pady=(10,10))

label1 = Label(master,text="NA")

label1.grid(pady=(10,10))

mainloop()

