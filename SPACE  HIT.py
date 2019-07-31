import turtle
import random
import time
import math

#setup screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("DEL")
wn.bgpic("spc.gif")
wn.tracer(0)


s_r=0
danger=turtle.Turtle()
danger.penup()
danger.speed(0)
danger.shape("circle")
danger.color("red")
danger.goto(random.randint(-290,290),random.randint(-290,290))
danger.setheading(random.randint(0,360))
def danger_move():
		danger.forward(2+sp)
		#border checking
		if danger.xcor()>=290 or danger.xcor()<=-290:
			danger.right(50)
			
		if danger.ycor()>=290 or danger.ycor()<=-290:

			danger.right(50)
		if danger.xcor()>300 or danger.xcor()<-300 or danger.ycor()>300 or danger.ycor()<-300:
			danger.goto(random.randint(-290,290),random.randint(-290,290))
			danger.setheading(random.randint(0,180))



index=turtle.Turtle()
index.penup()
index.hideturtle()
index.color("white")
index.speed(0)
index.goto(0,300)
index.write("Yellow ball: +10       Blue ball: -10       Red ball: Game Over",align="center",font=("arial",11,"bold"))
sp=0
class Game(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.speed(0)
		self.color("white")
		self.goto(-290,300)
		self.score=0
		self.write("Score: {} ".format(self.score),False,align="center",font=("arial",11,"bold"))
	def update_score(self):
		self.clear()
		self.write("Score: {} ".format(self.score),False,align="center",font=("arial",11,"bold"))	#writing on sprite
	def change_score(self,points):
		self.score+=points
		
		speed=0
		if self.score>100:
			speed=0.2
		if self.score>200:
			speed=0.4



			
		self.update_score()	
		return speed

#creating a class for player
class Player(turtle.Turtle):#player(object)
	
	#proper way to initialize an object
	def __init__(self):#two underscores on each side of init
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.shape("triangle")
		self.color("white")
		self.left(90)
		self.speed=0
	#methods in class
	def move(self):
		self.forward(self.speed)
		
		#border checking
		if self.xcor()>290 or self.xcor()<-290:
			self.left(60)
			
		if self.ycor()>290 or self.ycor()<-290:
			self.left(60)
			
		


	def turnleft(self):
		self.left(30)
		
	def turnright(self):
		self.right(30)
		
	def fast(self):
		if self.speed<=5:
			self.speed+=0.3
		

	def slow(self):
		if self.speed>0:
			self.speed-=0.3
	def dontmove(self):
		self.speed=0
		player.goto(0,0)

			

#creating a class for border
class Border(turtle.Turtle):

	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.speed(0)
		self.color("white")
		self.pensize(5)
	def draw_border(self):
		self.penup()
		self.goto(-300,-300)
		self.pendown()
		self.goto(-300,300)
		self.goto(300,300)
		self.goto(300,-300)
		self.goto(-300,-300)
#creating a goal
class Goal(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.color("yellow")
		self.shape("circle")
		self.speed=0.5
		self.goto(random.randint(-280,280),random.randint(-280,280))
		self.setheading(random.randint(0,360))	
	def move(self):
		self.forward(self.speed+sp)
		#border checking
		if self.xcor()>290 or self.xcor()<-290:
			self.left(60)
		if self.ycor()>290 or self.ycor()<-290:
			self.left(60)
		if self.xcor()>300 or self.xcor()<-300 or self.ycor()>300 or self.ycor()<-300:
			self.goto(random.randint(-290,290),random.randint(-290,290))
			self.setheading(random.randint(0,360))	
	def jump(self):
		self.goto(random.randint(-290,290),random.randint(-290,290))

#creating enemies
class Enemy(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.color("blue")
		self.shape("circle")
		self.speed=0.5
		self.goto(random.randint(-280,280),random.randint(-280,280))
		self.setheading(random.randint(0,360))	
	def move(self):
		self.forward(self.speed+sp)
		#border checking
		if self.xcor()>290 or self.xcor()<-290:
			self.left(60)
		if self.ycor()>290 or self.ycor()<-290:
			self.left(60)
		if self.xcor()>300 or self.xcor()<-300 or self.ycor()>300 or self.ycor()<-300:
			self.goto(random.randint(-290,290),random.randint(-290,290))
			self.setheading(random.randint(0,360))				
	def jump(self):
		self.goto(random.randint(-290,290),random.randint(-290,290))

		
#check collisions
def isCollisions(t1,t2):
	a=t1.xcor()-t2.xcor()
	b=t1.ycor()-t2.ycor()
	distance=math.sqrt((a**2)+(b**2))

	if distance<20:
		return True
	else:
		return False	



border=Border()
border.draw_border()
#create multiple goals
game=Game()
enemies=[]
for i in range(3):
	enemies.append(Enemy())
goals=[]
for count in range(6):
	goals.append(Goal())
#player is an instance in class Player as self
player=Player()
#set keyboard bindings
wn.listen()
wn.onkeypress(player.turnleft,"Left")
wn.onkeypress(player.turnright,"Right")
wn.onkeypress(player.fast,"Up")
wn.onkeypress(player.slow,"Down")
#collision check








	
#main loop
while True:
	wn.update()
	player.move()#move already defined in Player class
	danger_move()
	if player.xcor()>300 or player.ycor()>300 or player.xcor()<-300 or player.ycor()<-300:
		player.goto(random.randint(-250,-250),random.randint(-250,250))
	for goal in goals:

		goal.move()

		if isCollisions(player,goal):
			
			goal.jump()
			sp=game.change_score(10)
			s_r+=10

	for enemy in enemies:
		enemy.move()
		#check collision with enemies
		if isCollisions(player,enemy):
			enemy.jump()
			sp=game.change_score(-10)
			s_r-=10
	if isCollisions(player,danger):
		time.sleep(3)
		player.dontmove()
		danger.goto(random.randint(-290,290),random.randint(-290,290))
		game.change_score(-s_r)
		s_r=0
				






wn.mainloop()