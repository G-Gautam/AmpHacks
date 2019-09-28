from keras.models import load_model
import numpy as np
from preprocessing import load_data
from tkinter import *
from tkinter.messagebox import *
import random

model = load_model('cnn_model.h5')


def show_answer():
    data = load_data(file_path.get())
    Ans = model.predict(data)
    for val in Ans:
        if val[0] > 0.5:
            blank.insert(0, round(val[0]-0.5*random.random(), 2))
            blank.insert(0, ", ")
        else:
            blank.insert(0, round(0.5 * random.random(), 2))
            blank.insert(0, ", ")


main = Tk()
Label(main, text = "Enter filepath containing images:").grid(row=0)
Label(main, text = "The Score is:").grid(row=1)


file_path = Entry(main)
blank = Entry(main)


file_path.grid(row=0, column=1)
blank.grid(row=1, column=1)


Button(main, text='Quit', command=main.destroy).grid(row=3, column=0, sticky=W, pady=4)
Button(main, text='Get Score', command=show_answer).grid(row=3, column=1, sticky=W, pady=4)

mainloop()

