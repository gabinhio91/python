import turtle
bingo = turtle.Turtle()
#bingo.
 # forward(x)/backward(x)
 # right(g°)/left(g°)
 # goto(x,y)
 # setheading(g°)
 # speed(1-10)
 # penup()/pendown()
 # fillcolor('culoare')
 # begin_fill()/end_fill()




# bingo.fillcolor('beige')
# bingo.begin_fill()

# bingo.goto(0,0)
# bingo.setheading(90)
# bingo.forward(100)
# bingo.right(90)
# bingo.forward(30)
# bingo.right(90)
# bingo.forward(70)
# bingo.left(90)
# bingo.forward(30)
# bingo.right(90)
# bingo.forward(30)
# bingo.right(90)
# bingo.forward(60)
### NU ###
# bingo.forward(30)
# bingo.right(90)
# bingo.forward(30)
# bingo.right(90)
# bingo.forward(30)

# bingo.end_fill()
# x=180
# bingo.fillcolor('red')
# bingo.begin_fill()
# bingo.goto(0,0)
# bingo.setheading(90)
# bingo.forward(120)
# bingo.setheading(0)
# while x!=0:
#                               bingo.forward(1)
#                               bingo.right(1)
#                               x-=1
# bingo.end_fill()
# x=260
# bingo.color('light blue')
# bingo.pensize(10)
# bingo.speed(10)
# bingo.setheading(180)
# bingo.forward(30)
# while x != 0:
#     bingo.forward(1)
#     bingo.left(1)
#     x-=1
# bingo.setheading(90)
# bingo.forward(10)
# bingo.left(90)
# bingo.forward(40)

screen= turtle.Screen()
screen.setup(500,500)
bingo.begin_fill()
def b():
    bingo.begin_fill()
def e():
    bingo.end_fill()
def up():
    bingo.forward(10)
def right():
    bingo.right(10)
def left():
    bingo.left(10)
ok=0
def space():
    global ok
    if ok%2 ==0:
          bingo.penup()
    elif ok%2 != 0:
        bingo.pendown()
    ok+=1

                            

turtle.onkey(up,'Up')
turtle.onkey(right,'Right')
turtle.onkey(left,'Left')
turtle.onkey(space,'space')
turtle.onkey(b,'b')
turtle.onkey(e,'e')
turtle.listen()






turtle.mainloop()