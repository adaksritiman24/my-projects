import turtle as tl
import time
import random


tl.register_shape("goo_dino/dino1.gif")
tl.register_shape("goo_dino/dino2.gif")
tl.register_shape("goo_dino/dino3.gif")
tl.register_shape("goo_dino/h1.gif")
tl.register_shape("goo_dino/h2.gif")
tl.register_shape("goo_dino/h3.gif")
tl.register_shape("goo_dino/b1.gif")
tl.register_shape("goo_dino/b2.gif")

class Game():
	def __init__(self,wn):
		wn.setup(500,300)
		wn.title("Google Dino")
		self.Player()
		self.ground()
		self.jump(player)

		wn.tracer(0)
	def ground(self):
		gr=tl.Turtle()
		gr.penup()
		gr.speed(0)
		gr.goto(-450,-10)
		gr.pendown()
		gr.forward(900)
		gr.penup()
	def Player(self):
		global player
		player = tl.Turtle()
		player.shape("goo_dino/dino1.gif")
		player.penup()
		player.speed(0)
		player.goto(-170,0)
		player.shapesize(2)


	def jump(self,player):
		sb=tl.Turtle()
		sb.speed(0)
		sb.penup()
		sb.color("black")
		sb.goto(150,110)
		sb.write("Score: 0",font=("Comic Sans MS",10,"normal"))
		sb.hideturtle()	
		def game_over(s):	
			go=tl.Turtle()
			go.speed(0)
			go.penup()
			go.color("black")
			go.goto(0,20)
			go.write("GAME OVER\n  Score: {}".format(s),font=("Comic Sans MS",20,"normal"),align="center")
			go.hideturtle()				

		hurdle = tl.Turtle()
		hurdle.penup()
		hurdle.speed(0)
		hurdle.shapesize(1,2)

		
		hurdle.goto(300,0)	
		hu_choices=["goo_dino/h1.gif","goo_dino/h2.gif","goo_dino/h3.gif"]

		bird = tl.Turtle()
		bird.penup()
		bird.speed(0)
		bird.shape("square")
		bird.shapesize()
		bird.goto(500,0)
		bird.setheading(180)
		speed =0.8
		sp=6
		gravity =20
		c=0
		score =0
		global counter
		global var
		def var_criteria():
			global var
			var+=1
			return
		wn.listen()
		wn.onkeypress(var_criteria,"space")			

		while(True): 
			wn.update()	
			if var ==0:					
				if counter <50:
					player.shape("goo_dino/dino3.gif")
				if counter>50:
					player.shape("goo_dino/dino2.gif")	
				if counter>100:
					counter =0

			counter=counter+10


			
			if hurdle.xcor()<-300:
				hurdle.goto(300,0)
			if hurdle.xcor()==300:
				hurdle.shape(random.choice(hu_choices))	
			hurdle.setx(hurdle.xcor()-sp)	
			if player.distance(hurdle)<41 or player.distance(bird)<40:
				game_over(score)
				break 
			if score<130:
				sp+=0.01	
			c+=1
			if c==10:
				score+=1	
				
				sb.clear()
				sb.write("Score: {}".format(score),font=("Comic Sans MS",10,"normal"),align="center")	
				c=0

			if score> 200:
				sp=20
				if counter <50:
					bird.shape("goo_dino/b1.gif")
				if counter>50:
					bird.shape("goo_dino/b2.gif")					
				if bird.xcor()<-500:
					bird.goto(500,0)		
				bird.forward(sp)	

	
			if(var):
				player.shape("goo_dino/dino1.gif")			
				player.sety(player.ycor()+speed*gravity)
				speed =speed -0.1
				if speed<=-0.8:
					speed= 0.8
					var=0	
counter=0

var=0
wn=tl.Screen()
b=Game(wn)

wn.mainloop()
