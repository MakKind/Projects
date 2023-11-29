from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def click():
    try:
        a = int(input_text.get())
        my_label.config(text=round(a*1.609, 1))
    except Exception as e:
        messagebox.showerror("Enter a valid Number")


input_text = Entry(width=10)
input_text.grid(column=1, row=0)

my_label = Label(text="0", font=("Arial", 12))
my_label.grid(column=1, row=1)
my_label1 = Label(text="Miles", font=("Arial", 12))
my_label1.grid(column=2, row=0)
my_label2 = Label(text="is equal to", font=("Arial", 12))
my_label2.grid(column=0, row=1)
my_label4 = Label(text="Kilometer", font=("Arial", 12))
my_label4.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=click)
button.grid(column=1, row=2)

window.mainloop()
