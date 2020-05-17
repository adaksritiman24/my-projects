import turtle as tl
import random

scr =tl.Screen()
scr.title("Moving Stars")
scr.tracer(0)
scr.setup(800,800)
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
			self.p=0.5	
		#print(self.a/self.b)
	def move(self):
		if self.x<0:
			self.x -=self.z
		else:
			self.x +=self.z	
		self.y =self.p*self.x 

		self.star.setx(self.x)
		self.star.sety(self.y)
		self.star.shapesize(self.size)
		self.size+=0.007
		self.z+=0.5
		
stars =[]
for i in range(40):
	star = Star(random.randint(-400,400), random.randint(-400,400))
	stars.append(star)

run =True
while run:
	scr.update()
	for star in stars:
		star.move()
		if star.star.xcor()>500 or star.star.ycor()>500 or star.star.ycor()<-500 or star.star.xcor()<-500:
			star.star.shapesize(0.05)
			star.initialize(random.randint(-100,100),random.randint(-100,100))
			
scr.mainloop()		