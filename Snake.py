import turtle
import random
import time

delay=0.1
 

#score
score=0
highest_score=0 
#setup screen
wn=turtle.Screen()
wn.title("Snake game")
wn.bgcolor("green")
wn.setup(width=620,height=600)
wn.tracer(0)#turns off screen updates

#snakehead
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#snakefood1
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,150)

#snakefood2
food2=turtle.Turtle()
food2.speed(0)
food2.shape("circle")
food2.color("yellow")
food2.penup()
food2.goto(0,-150)

segments=[]

#pen
pen=turtle.Turtle()
pen.speed()
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 Highest score: 0",align="center",font=("Courier",24,"normal"))
 
#functions





def go_up():
	if head.direction!="down":
		head.direction="up"
def go_down():
	if head.direction!="up":
		head.direction="down"
def go_left():
	if head.direction!="right":
		head.direction="left"		
def go_right():
	if head.direction!="left":
		head.direction="right"
def move():
	if head.direction=="up":
		y=head.ycor()
		head.sety(y+20) 
	if head.direction=="down":
		y=head.ycor()
		head.sety(y-20) 
	if head.direction=="left":
		x=head.xcor()
		head.setx(x-20) 
	if head.direction=="right":
		x=head.xcor()
		head.setx(x+20) 	
#keyboard activating

 

wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

wn.listen()

#main loop
while True:
	wn.update()

	#check for border collisions
	if head.xcor()>300 or head.xcor()<-300 or head.ycor()>290 or head.ycor()<-290:
		time.sleep(1)
		head.goto(0,0)
		head.direction="stop"
		#hide segments after collision with the border
		for i in segments:
			i.goto(1000,1000)

		segments.clear()
		#reseting the score
		score=0
		pen.clear()	

		pen.write("Score: {}  Highest Score: {}".format(score,highest_score),align="center", font=("Courier",24,"normal"))
		#reset delay
		delay=0.1


	#checkfor collision with food
	if head.distance(food)< 20:
		x=random.randint(-289, 289)
		y=random.randint(-289, 289)
		food.goto(x,y)

		#add a segment
		new_segment =turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("grey")
		new_segment.penup()
		segments.append(new_segment)

		#shorten the delay
		delay-=0.001
		#increase the score
		score+=10
		if score>=highest_score:
			highest_score=score
		pen.clear()	

		pen.write("Score: {}  Highest Score: {}".format(score,highest_score),align="center",font=("Courier",24,"normal"))	
	#collosion with food 2
	if head.distance(food2)< 20:
		x=random.randint(-289, 289)
		y=random.randint(-289, 289)
		food2.goto(x,y)

		#add a segment
		new_segment =turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("grey")
		new_segment.penup()
		segments.append(new_segment)

		#shorten the delay
		delay-=0.001
		#increase the score
		score+=20
		if score>=highest_score:
			highest_score=score
		pen.clear()	

		pen.write("Score: {}  Highest Score: {}".format(score,highest_score),align="center",font=("Courier",24,"normal"))	

	


	#move the end segments firstin reverse order
	for i in range(len(segments)-1,0,-1):
		x=segments[i-1].xcor()
		y=segments[i-1].ycor()
		segments[i].goto(x,y)
	#move segment o to head pos
	if len(segments)>0:
		x=head.xcor()
		y=head.ycor()
		segments[0].goto(x,y)	
	move()	
	# check for body segment cllosions
	for segment in segments:
		if segment.distance(head)< 20:
			time.sleep(1)
			head.goto(0,0)
			head.direction="stop"
			#hide segments
			for i in segments:
				i.goto(1000,1000)
				segments=[]
			score=0	
			pen.clear()	

			pen.write("Score: {}  Highest Score: {}".format(score,highest_score),align="center", font=("Courier",24,"normal"))
			#reset delay
			delay=0.1
			

	time.sleep(delay)

wn.mainloop()



