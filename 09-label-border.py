from tkinter import *

my_window = Tk() # crea un objeto por defecto

# CODE GOES HERE
my_window.title("Label")

# Creamos label en nuestra ventana
# borderwidth = bd
label_1 = Label(my_window, text='Hello world', borderwidth=1, relief='solid', font='Times 12')
label_1.pack()
# se puede usar relief: solid, raised, sunken, ridge, groove, flat

# bucle principal
my_window.mainloop()