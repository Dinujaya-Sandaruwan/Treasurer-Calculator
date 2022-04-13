#import packges
import tkinter
from tkinter import *


#window_settings
window = Tk()
window.title("Treasurer Calculator")
window.geometry("430x670")
window.resizable(False,False)
window.iconbitmap('gg.ico')
window.configure(bg='#1f1f1f')

# var = StringVar()
# var.set('hello')

#title
tit_label = Label(window, text = "Treasurer Calculator", bg = '#1f1f1f', fg = '#ffffff')
tit_label.config(font=('Roboto', 30 ,'bold'))
tit_label.grid(pady= 20, padx=20, row = 1, column = 1)

value = 0

#SUM Label
# global tot_label
tot_label = Label(window, text = value , bg = '#1f1f1f', fg = '#24ff48')
tot_label.config(font=('Roboto', 50 ,'bold'))

# Funcations
def add_500():
    global value
    value = 500 + value
    # print (value)
    print_value = ("Rs.", value)
    tot_label = Label(window, text =  print_value , bg = '#1f1f1f', fg = '#24ff48')
    tot_label.config(font=('Roboto', 50 ,'bold'))
    tot_label.grid(pady= 40, padx=20, row = 7, column = 1)

def add_1000():
    global value
    value = 1000 + value
    # print (value)
    print_value = ("Rs.", value)
    tot_label = Label(window, text =  print_value , bg = '#1f1f1f', fg = '#24ff48')
    tot_label.config(font=('Roboto', 50 ,'bold'))
    tot_label.grid(pady= 40, padx=20, row = 7, column = 1)
def add_1500():
    global value
    value = 1500 + value
    # print (value)
    print_value = ("Rs.", value)
    tot_label = Label(window, text =  print_value , bg = '#1f1f1f', fg = '#24ff48')
    tot_label.config(font=('Roboto', 50 ,'bold'))
    tot_label.grid(pady= 40, padx=20, row = 7, column = 1)

def add_2000():
    global value
    value = 2000 + value
    # print (value)
    print_value = ("Rs.", value)
    tot_label = Label(window, text =  print_value , bg = '#1f1f1f', fg = '#24ff48')
    tot_label.config(font=('Roboto', 50 ,'bold'))
    tot_label.grid(pady= 40, padx=20, row = 7, column = 1)

#Buttons
bt_500 = Button(window, text = "+ 500  ", padx = 120, pady = 5, bg='#0052cc', fg='#ffffff', activebackground='black',activeforeground = 'white', borderwidth = 10, command = add_500)
bt_500.config (font=('Courgette', 25 , 'bold'))
bt_500.grid(pady= 10, row = 3, column = 1)

bt_1000 = Button(window, text = "+ 1000", padx = 120, pady = 5, bg='#0052cc', fg='#ffffff', activebackground='black',activeforeground = 'white', borderwidth = 10, command = add_1000)
bt_1000.config (font=('Courgette', 25 , 'bold'))
bt_1000.grid(pady= 10, row = 4, column = 1)

bt_1500 = Button(window, text = "+ 1500", padx = 120, pady = 5, bg='#0052cc', fg='#ffffff', activebackground='black',activeforeground = 'white', borderwidth = 10, command = add_1500)
bt_1500.config (font=('Courgette', 25 , 'bold'))
bt_1500.grid(pady= 10, row = 5, column = 1)

bt_2000 = Button(window, text = "+ 2000", padx = 120, pady = 5, bg='#0052cc', fg='#ffffff', activebackground='black',activeforeground = 'white', borderwidth = 10, command = add_2000)
bt_2000.config (font=('Courgette', 25 , 'bold'))
bt_2000.grid(pady= 10, row = 6, column = 1)


tot_label.grid(pady= 40, row = 7, column = 1)








#mainloop
window.mainloop()