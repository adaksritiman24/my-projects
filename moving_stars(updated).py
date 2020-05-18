import turtle as tl
import random

scr =tl.Screen()
scr.title("Moving Stars")
scr.tracer(0)
scr.setup(1200,800)
scr.bgcolor("black")

class Star:
	def __init__(self, m,n):
		self.size =0.05
		self.z = 0.4
		self.star = tl.Turtle()
		self.star.shape("circle")
		self.star.shapesize(self.size)
		self.star.color("white")
		self.star.penup()
		self.movforce= random.choice([0.6,0.8,0.3,0.5,1.0,2,5])
		self.initialize(m, n)
	def initialize(self,m,n):	
		self.size = 0.1
		self.z = 0.4
		self.star.goto(m,n)

		self.x, self.a= self.star.xcor(), self.star.xcor()
		self.y , self.b= self.star.ycor(), self.star.ycor()
		if self.a>2 or self.a<-2:
			self.p = self.b/self.a
		else:
			self.p=0.7
		#print(self.a/self.b)
	def move(self):
		if self.x<0:
			self.x -=self.z
		else:
			self.x +=self.z	
		self.y =self.p*self.x 

		self.star.setx(self.x)
		self.star.sety(self.y)
		self.star.shapesize(self.size*self.movforce)
		self.size+=0.03
		self.z+= self.movforce
		
stars =[]
for i in range(100):
	star = Star(random.randint(-700,700), random.randint(-700,700))
	stars.append(star)

run =True
while run:
	scr.update()
	for star in stars:
		star.move()
		if star.star.xcor()>1000 or star.star.ycor()>500 or star.star.ycor()<-500 or star.star.xcor()<-1000:
			star.star.shapesize(random.choice([0.1,0.2,0.05,0.03]))
			star.initialize(random.randint(-200,200),random.randint(-200,200))
			
scr.mainloop()		
