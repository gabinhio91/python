# from paddle import Paddle
import turtle
import time
import random
import os
import tkinter as tk

screen = turtle.Screen()
screen.bgcolor('light blue')
screen.setup(1200,500)
canvas = screen.getcanvas()

joc =0

def jocul():
     while joc :
     ###FARA IMPORT
          play.destroy()
          class Paddle(turtle.Turtle):
               def __init__(self, coordinates):
                    super().__init__()
                    self.shape('square')
                    self.color('#B2AC88')
                    self.shapesize(1,5.3)
                    self.penup()
                    self.setpos(coordinates[0], coordinates[1])

               def move_right(self):
                    new_x = self.xcor() + 35
                    self.goto(new_x, self.ycor())
          

               def move_left(self):
                    new_x = self.xcor() - 35
                    self.goto(new_x, self.ycor())


     ###CU IMPORT
     # class Paddle(Turtle):
     #      def __init__(self, coordinates):
     #         super().__init__()
     #         self.shape('square')
     #         self.color('#B2AC88')
     #         self.shapesize(1,5.3)
     #         self.penup()
     #         self.setpos(coordinates[0], coordinates[1])

     #      def move_right(self):
     #           new_x = self.xcor() + 35
     #           self.goto(new_x, self.ycor())
          

     #      def move_left(self):
     #          new_x = self.xcor() - 35
     #          self.goto(new_x, self.ycor())



          if os.path.exists('hiscore.txt'):
               pass
          else:
               f = open('hiscore.txt', 'w')
               f.write('0')


          hiscore = 0
          combo = 0
          scor = 0
          drift = [-5, -2, 0, 2, 5]
          # drift = [0]


          def exit_click():
               canvas.destroy()
               turtle.bye()
          
          exit = tk.Button(canvas.master, text = 'EXIT', height = 2, width = 4, command = exit_click, bg = 'red')
          exit.pack()
          exit.place(x = 1160, y = 5)
          
          scor_turtle = turtle.Turtle()
          scor_turtle.penup()
          scor_turtle.hideturtle()
          scor_turtle.color('black')
          scor_turtle.goto(-560,200)
          scor_turtle.write(f'Scor: {scor}\n Combo: x{combo}', font = ('Arial', 15, 'normal'))


          paleta = Paddle([0, -145])

          ball = turtle.Turtle()
          ball.shape('circle')
          ball.color('red')
          ball.penup()
          ball.goto(0, 200)
          ball.dy = 0
          ball.dx = 0

          game_is_on = True   

          screen.listen()
          screen.onkey(paleta.move_right, 'd')
          screen.onkey(paleta.move_left, 'a')


          while game_is_on and joc :
               ball.dy -=1
               ball.sety(ball.ycor() + ball.dy)
               ball.setx(ball.xcor() + ball.dx)

               if ball.ycor() <= -107 and ball.distance(paleta) <52:
                    scor_turtle.clear()
                    ball.dy = ball.dy * -1 + 1
                    ball.dx = random.choice(drift)
               #   print(f"y = {ball.ycor}, dist : {ball.distance(paleta)}")
                    combo +=1
                    if combo >=5 and combo < 10:
                         scor +=2
                    elif combo >=10 and combo <20:
                         scor+=4
                    elif combo >=20:
                         scor+=7
                    else:
                         scor+=1
                    scor_turtle.write(f'Scor: {scor}\n Combo: x{combo}', font = ('Arial', 15, 'normal'))
               #   print('combo',combo)
               #   print('scor',scor)
               #   print('\n')
                    

               if ball.ycor() < -300:
                    game_is_on = False
               #  exit.unpack()
               

               if ball.xcor() < -580 or ball.xcor() > 580:
                    ball.dx *=-1

          exit.destroy()
          screen.clear()
          screen.bgcolor('black')


          f= open('hiscore.txt','r')
          hiscore = int(f.read())

          if scor >= hiscore:
               f = open('hiscore.txt', 'w')
               f.write(str(scor))
               f.close()
               hiscore = scor
          
          time.sleep(1)

          scor_turtle.hideturtle()
          scor_turtle.color('white')
          scor_turtle.penup()
          scor_turtle.setpos(-90,0)
          scor_turtle.write(f'Scor: {scor}', font = ('Arial', 30, 'normal'))

          time.sleep(2)

          scor_turtle.clear()
          scor_turtle.setpos(-120,0)
          scor_turtle.write(f'HighScore: {hiscore}', font = ('Arial', 30, 'normal'))
          time.sleep(2)
          scor_turtle.clear()
          play.destroy()
          if joc == True:
               screen.bgcolor('light blue')
          else:
               screen.bgcolor('black')


def start_game():
     global joc
     joc=1
     jocul()
     play.destroy()

if joc == 0:
     play = tk.Button(canvas.master, text = 'PLAY',height = 3, width = 12,  command = start_game, background='#FAC898')
     play.pack()
     play.place(x= 557, y =230)

screen.mainloop()