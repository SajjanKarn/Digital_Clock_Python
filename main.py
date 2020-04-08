# Author: Sajjan Karn
from tkinter import *
from time import strftime

# Initialise Root Window
root = Tk()

# Main Code Begins From Here......


def show_time():
    current_time = strftime("%I:%M:%S %p")
    # print(current_time)
    label = Label(root, text=current_time, font=(
        "Arial", 32, 'bold'), fg="black")
    label.after(200, show_time)
    label.grid(row=0, column=1)


# Root Window Configuratiomn
root.resizable(False, False)
root.title("Digital Clock")
show_time()
root.mainloop()
