from tkinter import *

my_window = Tk() # crea un objeto por defecto: fondo gris, maximizar, minimizar, etc.

# CODE GOES HERE
my_window.title("Demo1")

# my_window.geometry('width'x'heith'+'x_position'+'y_position')
my_window.geometry("400x200+500+50")
# modificaciones del tamaño de la ventana
my_window.resizable(width=False, height=True)

#bucle principal
my_window.mainloop()