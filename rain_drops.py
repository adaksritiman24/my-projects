import turtle
import random
import time

class Raining:
	def __init__(self,mk):
		mk.setup(700,500)
		mk.bgcolor((0.5,0.7,0.8))
		mk.title("Rain")
		mk.tracer(0)
		self.rain(mk)
	def rain(self,mk):	
		R=[]
		for _ in range(50):
			R.append(turtle.Turtle())
		for r1 in R:
			r1.color((0.3,0.2,0.9))
			r1.penup()
			r1.shape("square")
			r1.shapesize(0.5,0.14)
			r1.goto(random.randint(-350,350),random.randint(-250,250))
			r1.speed(0)
		R2=[]
		for _ in range(30):
			R2.append(turtle.Turtle())
		for r1 in R2:
			r1.color((0.3,0.4,0.9))
			r1.penup()
			r1.shape("square")
			r1.shapesize(0.4,0.13)
			r1.goto(random.randint(-350,350),random.randint(-250,250))
			r1.speed(0)	
		R3=[]
		for _ in range(50):
			R3.append(turtle.Turtle())
		for r1 in R3:
			r1.color((0.3,0.5,0.9))
			r1.penup()
			r1.shape("square")
			r1.shapesize(0.3,0.12)
			r1.goto(random.randint(-350,350),random.randint(-250,250))
			r1.speed(0)						
		self.move(R,R2,R3,mk)

	def move(self,R,R2,R3,screen):
		self.speed=5
		self.sp=3
		self.s=2
		while True:
			screen.update()
			for r1 in R:
				r1.sety(r1.ycor()-self.speed)
				
			for r1 in R:
				if r1.ycor()<-270:
					r1.sety(random.randint(260,280))
			for r1 in R2:
				r1.sety(r1.ycor()-self.sp)
				
			for r1 in R2:
				if r1.ycor()<-270:
					r1.sety(random.randint(260,280))
			for r1 in R3:
				r1.sety(r1.ycor()-self.s)
				
			for r1 in R3:
				if r1.ycor()<-270:
					r1.sety(random.randint(260,270))								



scr=turtle.Screen()
b=Raining(scr)
scr.mainloop()
