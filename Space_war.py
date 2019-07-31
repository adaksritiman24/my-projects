import turtle
import random
import time
win=turtle.Screen()
win.setup(600,600)
win.title("Space War")
win.bgpic("space_invaders_background.gif")
win.tracer(0)
turtle.register_shape("invader[1].gif")
turtle.register_shape("player[1].gif")

bullet_state="ready"


#multiple_enemies:


number_of_enemies=7
enemies=[]
#add enemies
#important!!
for i in range(number_of_enemies):
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.speed(0)
	enemy.penup()
	enemy.goto(random.randint(-200,200),random.randint(150,270))
	enemy.shape("invader[1].gif")
enemy_speed=0.7


danger=turtle.Turtle()
danger.hideturtle()
danger.penup()
danger.color("red")
danger.pensize(5)
danger.goto(-300,-250)
danger.pendown()
danger.forward(600)


#player
player=turtle.Turtle()
player.speed(0)
player.penup()
player.goto(0,-270)
player.shape("player[1].gif")
player.setheading(90)
player_speed=20

#fire

def fire_it():
	global bullet_state
	if bullet_state=="ready":
		bullet_state="fired"
		x=player.xcor()
		y=player.ycor()+10
		fire.setposition(x,y)
		fire.showturtle()


def collisions():
	a=fire.xcor()-enemy.xcor()
	b=fire.ycor()-enemy.ycor()		
	distance= (((a**2)+(b**2))**(0.5))
	if distance<14:
		return True
	else:
		return False
def ga():
	game_over=turtle.Turtle()
	game_over.speed(0)
	game_over.color("white")
	game_over.hideturtle()
	game_over.penup()
	game_over.goto(0,0)
	game_over.write("GAME OVER",align="center",font=("arial",50,"normal"))

fire=turtle.Turtle()
fire.speed(0)
fire.penup()
fire.shapesize(0.5,0.2)
fire.goto(0,0)
fire.shape("square")
fire.color("gold")

fire.speed=5
fire.hideturtle()


#functions
def go_left():
	if player.xcor()>-270:
	    player.setx(player.xcor()-player_speed)
def go_right():
	if player.xcor()<270:
	    player.setx(player.xcor()+player_speed)	

#set the score 0
score=0

#score
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(-290,270)
pen.write("Score: {}".format(score),align="left",font=("arial",20,"normal"))


win.listen()
win.onkeypress(go_left,"Left")
win.onkeypress(go_right,"Right")
win.onkeypress(fire_it,"space")
gameover=False

while not gameover:
	win.update()
	time.sleep(0.01)
	fire.sety(fire.ycor()+fire.speed)
	if fire.ycor()>300:
		bullet_state="ready"
	
	for enemy in enemies:	
		enemy.setx(enemy.xcor()+enemy_speed)
		if enemy.xcor()>270:
			for e in enemies:
				e.sety(e.ycor()-40)
			enemy_speed=-enemy_speed
		if enemy.xcor()<-270:
			for e in enemies:
				e.sety(e.ycor()-40)
				enemy_speed=-enemy_speed
		if collisions():
			enemy.goto(random.randint(-200,200),270)
			fire.goto(0,310)
			score+=1

			pen.clear()
			pen.write("Score: {}".format(score),align="left",font=("arial",20,"normal"))
	for enemy in enemies:		
		if enemy.distance(player)<20:
			ga()
			gameover=True	
		if enemy.ycor()<-240: 
			for e in enemies:
				e.sety(e.ycor()-40)	
			ga()
			gameover=True	




win.mainloop()