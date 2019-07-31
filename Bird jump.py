import turtle
import time
import random


wn=turtle.Screen()
wn.setup(600,600)
wn.bgcolor("light blue")
wn.title("BIRD JUMP(Inspired by flappy bird),developed by @S.Adak")
wn.tracer(0)
#player


turtle.register_shape("bird.gif")
turtle.register_shape("bird1.gif")
turtle.register_shape("bird2.gif")
player=turtle.Turtle()
player.speed(0)
player.penup()
player.shape("bird.gif")
player.goto(0,0)

#hurdles 1
h1=turtle.Turtle()
h1.speed(0)
h1.penup()
h1.color("green")
h1.shape("square")
h1.shapesize(30,4)
x_go=400
h1.goto(x_go,375)


h2=turtle.Turtle()
h2.speed(0)
h2.penup()
h2.color("green")
h2.shape("square")
h2.shapesize(30,4)
h2.goto(x_go,-375)

#hurdles 2
h11=turtle.Turtle()
h11.speed(0)
h11.penup()
h11.color("green")
h11.shape("square")
h11.shapesize(30,4)
h11.goto(800,375)

h22=turtle.Turtle()
h22.speed(0)
h22.penup()
h22.color("green")
h22.shape("square")
h22.shapesize(30,4)
h22.goto(800,-375)



score=0


s_b=turtle.Turtle()
s_b.speed(0)
s_b.penup()
s_b.color("red")
s_b.goto(0,150)
s_b.write("BIRD JUMP",align="center",font=("Comic Sans MS",40,"normal"))
s_b.hideturtle()

sab=turtle.Turtle()
sab.speed(0)
sab.penup()
sab.color("blue")
sab.goto(0,50)
sab.write("Use spacebar to play",align="center",font=("Comic Sans MS",20,"normal"))
sab.hideturtle()


game_over=turtle.Turtle()
game_over.speed(0)
game_over.penup()
game_over.color("black")
game_over.goto(0,0)
game_over.hideturtle()


	
global response
respond=True

game=True

global speed

gravity=5

sb=turtle.Turtle()
sb.speed(0)
sb.penup()
sb.color("black")
sb.goto(-275,265)
sb.write("Score: 0",font=("Comic Sans MS",20,"normal"))
sb.hideturtle()


def jump_up():
	s_b.clear()
	sab.clear()
	global score
	global game
	speed=1.1
	while game:
		wn.update()
		time.sleep(0.007)
		player.sety(player.ycor()+speed*gravity)
		speed=speed-0.03
		if speed>=-0.3:
			player.shape("bird1.gif")
		if speed<0.3:
			player.shape("bird2.gif")			

		h1.setx(h1.xcor()-2.5)
		h2.setx(h2.xcor()-2.5)
		h11.setx(h11.xcor()-2.5)
		h22.setx(h22.xcor()-2.5)	

		if speed==0:
			player.left(90)
		if h1.xcor()<-400:
			h1.setx(400)
			h2.setx(400)
			y_go=random.randint(150,600)
			h1.sety(y_go)
			h2.sety(-(750-y_go))


		if h11.xcor()<-400:
			h11.setx(400)
			h22.setx(400)
			y_go=random.randint(150,600)
			h11.sety(y_go)
			h22.sety(-(750-y_go))
		if ((player.xcor()+10)>(h1.xcor()-40)) and ((player.xcor()-10)<(h1.xcor()+40)):
			if((player.ycor()+12)>(h1.ycor()-300) or(player.ycor()-10)<(h2.ycor()+296)):
				game_over.write("Game Over",align="center",font=("Comic Sans MS",50,"normal"))
				game=False
				respond=False
				break
		if ((player.xcor()+10)>(h11.xcor()-40)) and ((player.xcor()-10)<(h11.xcor()+40)):
			if((player.ycor()+12)>(h11.ycor()-300) or(player.ycor()-10)<(h22.ycor()+296)):
				game_over.write("Game Over",align="center",font=("Comic Sans MS",50,"normal"))
				game=False
				respond=False
				break	

		if player.ycor()>285 or player.ycor()<-285:
				game_over.write("Game Over",align="center",font=("Comic Sans MS",50,"normal"))
				game=False
				respond=False
				break								

		if ((player.xcor()-10)==(h1.xcor()+40)) or ((player.xcor()-10)==(h11.xcor()+40)):
			score+=1
			sb.clear()
			sb.clear()
			sb.write("Score: {}".format(score),font=("Comic Sans MS",20,"normal"))	

if respond:
	wn.listen()
	wn.onkeypress(jump_up,"space")
		
wn.mainloop()		








	



