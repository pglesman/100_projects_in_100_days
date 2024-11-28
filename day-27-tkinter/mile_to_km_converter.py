from tkinter import *


def button_clicked():
    miles = float(input_label.get())
    km = round(miles * 1.609, 2)
    km_label.config(text=f'{km}')


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # padding in the whole window

# Entry for 'miles'
input_label = Entry(width=10)
input_label.insert(END, string="0")
input_label.grid(column=1, row=0)

# Label 'Miles'
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label 'is equal'
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# Label for 'km'
km_label = Label(text="0")
km_label.grid(column=1, row=1)

# Label 'Km'
equal_label = Label(text="Km")
equal_label.grid(column=2, row=1)

# Button 'Calculate'
button_calc = Button(text='Calculate', command=button_clicked)
button_calc.grid(column=1, row=2)

window.mainloop()
