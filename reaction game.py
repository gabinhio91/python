import time
import tkinter as tk
import random 
import os


if os.path.exists('hiscore.txt'):
     pass
else:
     f = open('hiscore.txt', 'w')
     f.write('100')


def start_joc():
     canvas.itemconfig(red_dot, fill ='red')
     screen.after(random.randint(1000,5000), turn_green)
     screen.after(random.randint(500,5500), turn_blue)

def turn_blue():
     canvas.itemconfig(red_dot, fill ='blue')

def turn_green():
     global start_time
     canvas.itemconfig(red_dot, fill = 'green')
     start_time = time.time()

def on_click(event):
     if canvas.itemcget(red_dot, 'fill') == 'green':
          reaction_time = time.time() - start_time
          show_reaction_time(reaction_time)
     elif canvas.itemcget(red_dot, 'fill') == 'blue':
          canvas.delete(red_dot)
          canvas.create_text(200,200, text = f"ai pierdut", fill = 'black', font = ('Helvetica', 20))
     else:
        canvas.delete(red_dot)
        canvas.create_text(200,200, text = f"ai furat startul ", fill = 'black', font = ('Helvetica', 20))
          

def show_reaction_time(reaction_time):
     # global scor
     # scor = reaction_time
     canvas.delete(red_dot)
     # f= open('hiscore.txt','r')
     # hiscore = float(f.read())
     # if scor <= hiscore:
     #      f = open('hiscore.txt', 'w')
     #      f.write(str(scor))
     #      f.close()
     #      hiscore = scor
     canvas.create_text(200,200, text = f"Timp de reactie: {reaction_time:.3f} secunde", fill = 'black', font = ('Helvetica', 20))
     # time.sleep(2)
     # canvas.delete()
     # canvas.create_text(200,200 , text = f'HighScore: {hiscore}', font = ('Helvetica', 20, 'normal'))
     

     
     
# def end():

     


screen = tk.Tk()
screen.title = 'test de reactie'
screen.geometry('400x400')

canvas = tk.Canvas(screen, width = 400, height = 400, bg = 'white')
canvas.pack()


red_dot = canvas.create_oval(150,150,250,250, fill = 'red')
canvas.bind('<Button-1>', on_click)
start_joc()


screen.mainloop()