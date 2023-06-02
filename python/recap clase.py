# class Persoana:
#     varsta = 0
#     nume = ""
#     def constructor(self,varsta, nume):
#         self.varsta = varsta
#         self.nume = nume
#     def descriere(self):
#         print(f'persoana se numeste {self.nume} si are {self.varsta} ani')
#     def __str__(self):
#         return(f'persoana se numeste {self.nume} si are {self.varsta} ani')


# gabi = Persoana()
# # gabi.varsta = 17
# # gabi.nume = 'gabriel'
# # print (gabi.varsta)
# # gabi.descriere()

# gabi.constructor(nume = 'marius', varsta = 18)
# gabi.descriere()

# print(gabi)





# class Car:
#     def __init__(self, an, marca, owner):
#         self.an = an
#         self.marca = marca 
#         self.owner = owner
#     def __str__(self):
#         return(f'masina este din anul {self.an}, de marca {self.marca} si detinuta de {self.owner}')
# masina = Car ( an = 2006, marca = 'BMW', owner = 'Andrei') 
# print(masina)


### PAGINA - ITLU LABEL

# import tkinter as tk
# window =tk.Tk()
# window.title('Label Example')
# label = tk.Label(window, text ='salut')
# label.pack()
# window.mainloop()



### BUTON

# import time 
# import tkinter as tk
# def button_click():
#     label.config(text = 'Button Clicked')
#     window.after(3000, lambda: label.config(text = 'text initial'))
 
# window = tk.Tk()
# window.geometry('400x220')
# label = tk.Label(window, text = 'text initial')
# button = tk.Button(window, text = 'click me', height = 5, width = 5, command = button_click)
# label.pack(side = 'left')
# button.pack()
# window.mainloop








###Caseta reprod text


# from tkinter import *
# def insert_text():
#     input_text = entry.get()
#     text_widget.delete('0', END)
#     text_widget.insert(END, input_text + '\n')
# window = Tk()
# window.geometry('400x220')
# window.title('insert text into text widget')
# entry = Entry(window)
# entry.pack()

# button = Button(window, text = 'insert', command = insert_text)
# button.pack()

# text_widget = Entry(window)
# text_widget.pack()

# window.mainloop()


import tkinter as tk
import random
window= tk.Tk()
window.geometry('1080x720')
def on_enter(e):
    e.widget['background'] = 'green'
    def pozitie(self):
        return self.random.randrange(0,1000), self.random.randrange(0,700)
    button.place(pozitie())
    button.unpack()
    button.pack()
def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'
button = tk.Button(window, text = 'click me', height = 5, width = 5)
button.grid()
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
button.pack()
window.mainloop()




