import turtle
import tkinter as tk
import random 

mesaje:list[str] = ['yes', 'no', 'maybe']



screen = turtle.Screen()
screen.setup(500,700)
screen.bgcolor('light blue')
screen.tracer(0)


bingo = turtle.Turtle()
bingo.speed(10)
bingo.goto(0,-160)
bingo.color('white')
bingo.fillcolor('black')
bingo.begin_fill()
bingo.circle(180)
bingo.end_fill()

bingo.penup()
bingo.goto(-2,-65)
bingo.pendown()

bingo.color('#D3D3D3')
bingo.fillcolor('#D3D3D3')
bingo.begin_fill()
bingo.circle(80)
bingo.end_fill()

bingo.penup()
bingo.goto(61,-24)
bingo.setheading(180)
bingo.pendown()

bingo.color('pink')
bingo.fillcolor('pink')
bingo.begin_fill()
for i in range (2):
  bingo.forward(125)
  bingo.right(120)
bingo.end_fill()

pico = turtle.Turtle()
def generate():
  global pico
  pico.clear()
  pico.color('white')
  pico.penup()
  pico.goto(-15,0)
  pico.pendown()
  text_bila = random.choice(mesaje)
  pico.write(text_bila, font = ('Arial', 13 , 'normal'))

canvas = screen.getcanvas()
buton = tk.Button(canvas.master, text ='generate', command = generate)
buton.pack()
buton.place(x= 220 ,y =120)

kuk = turtle.Turtle()
kuk.penup()
kuk.color('white')
intrebare = turtle.textinput("Magic 8 Ball", 'Intrebare: ')

kuk.goto(x= -60 ,y =270)
kuk.write(intrebare , font = ('Arial', 25 , 'normal') )

screen.mainloop()