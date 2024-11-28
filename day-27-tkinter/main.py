from tkinter import *


def button_clicked():
    my_label.config(text=input_label.get())


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # padding in the whole window

# Label
my_label = Label(text="I am Label", font=("Arial", 24, 'bold'))
my_label["text"] = 'New Text'
my_label.config(text='New text')
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)  # padding around widget

# Button 1
button_1 = Button(text='Click Me', command=button_clicked)
button_1.grid(column=1, row=1)

# Button 2
button_2 = Button(text='Click Me Also', command=button_clicked)
button_2.grid(column=2, row=0)

# Entry
input_label = Entry(width=10)
input_label.grid(column=3, row=2)


window.mainloop()
