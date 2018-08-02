from tkinter import *

def salute():
    """ modify lable_2's saludo """
    var_saludo.set('Hola ' + var_name.get()) # modificamos var_1

# variables
my_window = Tk()
var_saludo = StringVar()
var_name = StringVar()

# build the GUI
label_1 = Label(my_window, text='¿Cómo te llamas?')
entry_1 = Entry(my_window, textvariable=var_name)
button_1 = Button(my_window, text='Salute', command=salute)
label_2 = Label(my_window, textvariable=var_saludo)

label_1.grid(row=0, column=0)
entry_1.grid(row=0, column=1)
button_1.grid(row=1, column=0)
label_2.grid(row=1, column=1)

my_window.mainloop()
