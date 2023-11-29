from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)


def click():
    a = input_text.get()
    my_label.config(text=a)


# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Label"
my_label.config(text="Newwww")
# my_label.pack()
# my_label.place(x=450, y=250)
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click me", command=click)
# button.pack()
button.grid(column=1, row=1)
# Entry
input_text = Entry(width=10)
# input_text.pack()
input_text.grid(column=3, row=3)
# Button
new_button = Button(text="New Button", command=click)
# button.pack()
new_button.grid(column=2, row=0)
window.mainloop()
