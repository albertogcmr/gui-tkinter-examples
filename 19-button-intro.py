from tkinter import *

def add_label():
    lable_1 = Label(my_window,
                    text='Botón pulsado')
    lable_1.pack()

my_window = Tk() # crea un objeto por defecto
my_window.geometry('200x100')

button_1 = Button(my_window,
                  relief='solid',
                  font='Times 22 bold',
                  text='Clic Me',
                  command=add_label)    # nombre de la función, sin invocar
                                        # sin paréntesis

button_1.pack()

# bucle principal
my_window.mainloop()
