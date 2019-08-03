import turtle
import math
import time
import random
wn=turtle.Screen()
wn.setup(1600,800)
wn.title("Solar System Model")
wn.bgcolor("black")
wn.tracer(0)


class Planet(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.speed(0)
		self.penup()
		self.goto(0,0)
		self.shape("circle")
	def colour(self,color,size):
		self.color(color)
		self.shapesize(size)
		
stars=[]
for _ in range(200):
	stars.append(turtle.Turtle())
for s in stars:
	s.penup()
	s.speed(0)
	s.shapesize(random.choice([0.1,0.2,0.05,0.07,0.03]))
	s.shape("circle")
	s.goto(random.randint(-800,800),random.randint(-400,400))
	s.color(random.choice(["white","gold"]))	





planet1=Planet()
planet1.colour("green",1)
planet1.goto(-240,0)
planet1.pendown()

planet2=Planet()
planet2.colour("light blue",1.7)
planet2.goto(-400,0)
planet2.pendown()

planet3=Planet()
planet3.colour("red",2.5)
planet3.goto(-549,0)
planet3.pendown()

planet4=Planet()
planet4.colour("blue",2)
planet4.goto(-750,0)
planet4.pendown()


star=Planet()
star.colour("gold",3.5)
star.goto(-90,0)
hp=2
e=1
lp=2
d=-1
pp=2
sp=4
b=1
c=1
while True:

			wn.update()
			
			x=planet1.xcor()+sp
			y=b*((90/240)*math.sqrt(abs((240**2)-(x**2))))
			planet1.shapesize(1)
			planet1.goto(x,y)
			if x==240:
				sp=-sp
				b=-1
			if x==-240:
				sp=-sp
				b=1	
			m=planet2.xcor()+pp
			n=c*((150/400)*math.sqrt(abs((400**2)-(m**2))))
			planet2.goto(m,n)

			if m==400:
				pp=-pp
				c=-1
			if m==-400:
				pp=-pp
				c=1	
			o=planet3.xcor()+lp
			p=d*((210/549)*math.sqrt(abs((549**2)-(o**2))))
			planet3.goto(o,p)
			if o==549:
				lp=-lp
				d=1
			if o==-549:
				lp=-lp
				d=-1
			q=planet4.xcor()+hp
			r=e*((270/750)*math.sqrt(abs((750**2)-(q**2))))
			planet4.goto(q,r)
			if q==750:
				hp=-hp
				e=-1
			if q==-750:
				hp=-hp
				e=1					


			star.forward(1)
			star.right(120)			







wn.mainloop()









