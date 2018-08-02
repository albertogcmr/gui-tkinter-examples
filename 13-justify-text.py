from tkinter import *

my_window = Tk() # crea un objeto por defecto

# CODE GOES HERE
my_window.title("Label")
my_window.geometry('400x250')

# Creamos label en nuestra ventana
label_1 = Label(my_window,
                 text='spacer')
label_2 = Label(my_window,
                text='Text\nText Text\nText Text Text',
                borderwidth=1,
                relief='solid',
                font='Times 20')
label_3 = Label(my_window,
                 text='spacer')
label_4 = Label(my_window,
                text='Text\nText Text\nText Text Text',
                borderwidth=1,
                relief='solid',
                font='Times 20',
                justify=RIGHT)

label_1.pack()
label_2.pack()
label_3.pack()
label_4.pack()

# bucle principal
my_window.mainloop()