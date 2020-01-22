#moduals
import turtle
import os
import math
import random
import pygame
pygame.mixer.init()
#Setting up Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1280, height=720)
wn.title('Space Invaders')
wn.bgpic('Background.gif')
wn.addshape(r'player.gif')
wn.addshape(r'invader.gif')
wn.addshape(r'Bullet.gif')







music = pygame.mixer.music.load('mercury.wav')
pygame.mixer.music.play(-1)
playerexplosionsound = pygame.mixer.Sound('explosion.wav')
invaderexplosionsound = pygame.mixer.Sound('invaderkilled.wav')
shootingsound = pygame.mixer.Sound('shoot.wav')


#Draw Border
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

#making score and setting to 0
score = 0

#draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.ht()

#making high schore list
f = open('highscore.txt', 'r')
highscore = f.readline()
f.close()

highscore_pen = turtle.Turtle()
highscore_pen.speed(0)
highscore_pen.color('white')
highscore_pen.penup()
highscore_pen.setposition(350, 200)

#create player turtle
player = turtle.Turtle()
player.color('blue')
player.shape(r"player.gif")
player.penup()
player.speed(0)
player.setposition(0, -280)
player.setheading(90)
playerspeed = 15



#number of enemys
numberofenemies = 7
enemies = []

for i in range(numberofenemies):
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color('red')
	enemy.shape(r"invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)
	


enemyspeed = 5


#create the player bullet
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape(r'Bullet.gif')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.setposition(player.xcor(), player.ycor() + 10)
bullet.ht()
bulletspeed = 20

player_alive = True


bulletstate = "ready"
#functions and keybinds

def fire():
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
		x = player.xcor()
		y = player.ycor() + 10
		bullet.st()
		bullet.setposition(x, y)
		shootingsound.play()


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



def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 20:
		return True
	else:
		return False


	
		

	



#create keyword binding
wn.onkey(left, "a")
wn.onkey(right, "d")
wn.onkey(fire, "w")

wn.listen()

if str(score) <= str(open('highscore.txt','r')) :
		f = open('highscore.txt', 'w')
		f.write(str(score))
		f.close()
#main game loop

while player_alive == True:
	highscore_pen.st
	highscorestring = "Previous Score: %s" %highscore
	highscore_pen.write(highscorestring, False, align="left", font=("Arial", 20, "normal"))
	highscore_pen.ht()

	for enemy in enemies:
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		if enemy.xcor() >= 280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)

			enemyspeed *= -1

		if enemy.xcor() <= -280:
			for e in enemies:
				y = e.ycor()
				y -=40
				e.sety(y)
			enemyspeed *= -1

		if isCollision(bullet, enemy):
			bullet.ht()
			bulletstate == "ready"
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x, y)		
			invaderexplosionsound.play()

			#update score
			score += 10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

		if enemy.ycor() <= -280:
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x, y)



		if isCollision(player, enemy):
			enemy.ht()
			player.ht()
			print('Game Over')
			player_alive = False
			playerexplosionsound.play()



	
	y = bullet.ycor()
	y += bulletspeed
	bullet.sety(y)

	if bullet.ycor() > 275:
		bullet.ht()
		bulletstate = "ready"

	if str(score) <= str(open('highscore.txt','r')) :
		f = open('highscore.txt', 'w')
		f.write(str(score))
		f.close()

if str(score) < str(open('highscore.txt','r')) :
		f = open('highscore.txt', 'w')
		f.write(str(score))
		f.close()


score_pen.setposition(-75, 0)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 30, "normal"))

delay = input()
wn.mainloop()
