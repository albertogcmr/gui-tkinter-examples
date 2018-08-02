from tkinter import *

my_window = Tk()

label_1 = Label(my_window, width='20', height='3', bg='red')
label_2 = Label(my_window, width='20', height='3', bg='green')
label_3 = Label(my_window, width='20', height='3', bg='blue')
button_1 = Button(my_window, width='20', height='3', bg='white', text='Button 1')
button_2 = Button(my_window, width='20', height='3', bg='black', text='Button 2', fg='white')
button_3 = Button(my_window, width='20', height='3', bg='grey', text='Button 3')

label_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
label_3.grid(row=0, column=2)
button_1.grid(row=1, column=0)
label_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

# bucle principal
my_window.mainloop()
