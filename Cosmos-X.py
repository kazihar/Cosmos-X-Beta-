#space invaders tuts pt-9 finished
#setting up the screen

import pygame
import turtle
import os
import math
import random
import winsound
pygame.init()

music = pygame.mixer.music.load('musci.mp3')
pygame.mixer.music.play(-1)

#set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Cosmos-X(Beta)")
wn.bgpic("space_invaders_background.gif")

#registering the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player3.gif")
turtle.register_shape("player1.gif")

#Drawing border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Setting the score to 0
score = 0

#drawing the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,275)
scorestring = "Score: %s" %score
score_pen.write(scorestring,False,align="Left",font=("Arial", 14,"normal"))
score_pen.hideturtle()



#creating a player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player3.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 30

#creating the enemy
#enemy.color("Red")
#enemy.shape("circle")
#enemy.penup()
#enemy.speed(0)
#enemy.setposition(-200,250)

#enemyspeed = 2

#choosing the number of enemies
number_of_enemies = 5
#void enemy list
enemies = []
#Addings enemies
for i in range(number_of_enemies):
    #creating enemies
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("Red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)
enemyspeed = 5

#creating the player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("player1.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed  = 30

#Defining bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#move the player left
def move_left():
    x = player.xcor()
    x -=playerspeed
    if x < -280:
        x = -280
    player.setx(x)

#move the player right
def move_right():
    x = player.xcor()
    x+=playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#firing a bullet
def fire_bullet():
    #Declaring bullet state as a global if it needs to be changed
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("laser",winsound.SND_ASYNC)
        bulletstate = "fire"
        #move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x ,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#creating keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet ,"space")

#Main game loop
while True:
    for enemy in enemies:
        #move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Move the enemy back and down
        if enemy.xcor() > 280:
            #moves all enemies down
            for e in enemies:
                y = e.ycor()
                y -=40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            #move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1
            
        #checking for a collision between the bullet and enemy
        if isCollision(bullet,enemy):
            winsound.PlaySound("explosion",winsound.SND_ASYNC)
            #reseting the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            #reseting the enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x,y)

            
            #Updating the score
            score+=10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring,False,align="Left",font=("Arial",14,"normal"))

        #checking for a collison between enemy and player
        if isCollision(player,enemy):
            winsound.PlaySound("explosion",winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #moving the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #bullet border check
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

delay = raw_input("press enter to finish")








