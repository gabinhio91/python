from paddle import Paddle
import turtle
import time
import random

screen = turtle.Screen()
screen.bgcolor('light gray')
screen.setup(1200,500)

scor = 0
# drift = [-5, -2, 0, 2, 5]
drift = [0]

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

while game_is_on:
    ball.dy -=1
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    if ball.ycor() <= -107 and ball.distance(paleta) <48:
          ball.dy = ball.dy * -1 + 1
          ball.dx = random.choice(drift)
          scor +=1 
          print(f"y = {ball.ycor}, dist : {ball.distance(paleta)}")
          

    if ball.ycor() < -300:
         game_is_on = False
     

    if ball.xcor() < -580 or ball.xcor() > 580:
          ball.dx *=-1

screen.clear()
screen.bgcolor('black')

time.sleep(1)

scor_turtle = turtle.Turtle()
scor_turtle.hideturtle()
scor_turtle.color('white')
scor_turtle.penup()
scor_turtle.setpos(-90,0)
scor_turtle.write(f'Scor: {scor}', font = ('Arial', 30, 'normal'))


time.sleep(2)
# screen.mainloop()