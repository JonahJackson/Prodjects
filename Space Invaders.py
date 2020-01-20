import turtle
import os

wn = turtle.Screen()
wn.bgcolor("black")
wn.title('Space Invasders')

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed = 15

enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2

bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.setposition(player.xcor(), player.ycor() + 10)
bullet.ht()
bulletspeed = 20

player_alive = True

if enemy.xcor() == player.xcor() and enemy.ycor() == player.ycor():
	player_alive = False


def fire():

		x = player.xcor()
		y = player.ycor() + 10
		bullet.st()
		bullet.setposition(x, y)

def right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)
	

def left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = - 280
	player.setx(x)
	

wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(fire, "space")
wn.listen()
wn.mainloop()

while player_alive == True:
	x = enemy.xcor()
	x += enemyspeed
	enemy.setx(x)
