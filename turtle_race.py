# the color of the turtle winning in each round is saved in a file named :turtle_winner
import turtle as tl
import time
import random

#creating the screen object of turtle
scr = tl.Screen()
scr.title("Turte Race")
scr.tracer(0)# to hide animations
scr.bgcolor("green")
#object turtle of the race
class Turtle():
	def __init__(self, pos, color, speed):
		self.speed = 8/speed
		self.turtle =tl.Turtle()
		self.turtle.shape("turtle")
		self.color = color
		self.turtle.color(self.color)
		self.turtle.penup()
		self.turtle.setheading(90)
		self.turtle.goto(pos)
		self.turtle.pendown()
		self.finished =False
	def run(self):
		if not self.finished:
			self.turtle.forward(self.speed)	
	def check_completed(self):
		if self.turtle.ycor()>190:
			self.finished=True
#a square turtle object which is used to create finishline 
class FinishLine:
	def __init__(self, pos, color):
		self.ln =tl.Turtle()
		self.ln.shape("square")
		self.ln.shapesize((0.5))
		self.ln.color(color)
		self.ln.penup()
		self.ln.goto(pos)
		self.ln.pendown()
#object startline of the race		
class StartLine:
	def __init__(self, pos):
		self.ln =tl.Turtle()
		self.ln.color("white")
		self.ln.penup()
		self.ln.goto(pos)
		self.ln.pendown()
		self.ln.forward(240)
		self.ln.hideturtle()
def draw_start():
	st = StartLine((-120,-180))
# creating the finishline in our screen using the FinishLine class
def draw_finish():		
	color ="black"		
	for i in range(9):
		FinishLine((-100+25*i,200), color)
	color = "white"			
	for i in range(9):
		FinishLine((-88+25*i,200), color)
	color ="white"		
	for i in range(9):
		FinishLine((-100+25*i,190), color)
	color = "black"			
	for i in range(9):
		FinishLine((-88+25*i,190), color)	
draw_start()			
draw_finish()			
# defining the 5 turtle objects that would race against each other
# store all turtles in a list named ,turtles
turtle_1 = Turtle((0,-200),"white",random.randint(10,20))
turtle_2 = Turtle((50,-200),"blue",random.randint(10,20))
turtle_3 = Turtle((-50,-200),"red",random.randint(10,20))
turtle_4 = Turtle((100,-200),"black",random.randint(10,20))
turtle_5 = Turtle((-100,-200),"yellow",random.randint(10,20))
turtles = [turtle_1,turtle_5,turtle_4,turtle_3,turtle_2]

run =True
new =True
winners=[]
#main game loop
while run:
	scr.update()
	#  moving each and every turtle on the screen
	#  if the particular turtle has finished the race, it wii stop moving	 
	for turtle in turtles:	
		turtle.run()
		turtle.check_completed()
	done = 0
	winners.clear()
	#checking if a turtle has finished race
	# the color of the winnig turtle will be appended to the list of winners
	for turtle in turtles:
		if turtle.finished:
			winners.append(turtle.color)
			done+=1
	#file operation for saving the winning turtle of each race		
	if new:		
		if done >=1:
			f= open("turtle_winner.txt","a")
			f.write("WINNERS(s):\n")
			win = ""
			for winner in winners:
				win = win+winner+" "
			f.write(win)
			f.write("\n\n")
			f.close()	
			winners.clear()
			#once the winner is saved--ensure that further no more turtles are saved in the turtle_winner file
			new = False		
	# when all the turtles have completed the race it is time to go for a new race immediately.
	# screen is cleared
	# backgroung is restored
	# start an finishline are recreated
	# 5 turtles are initialized at the starting point		
	if done==5:
		new =True
		time.sleep(1)
		scr.clear()
		scr.tracer(0)
		scr.bgcolor("green")
		draw_start()
		draw_finish()
		turtle_1 = Turtle((0,-200),"white",random.randint(5,15))
		turtle_2 = Turtle((50,-200),"blue",random.randint(5,15))
		turtle_3 = Turtle((-50,-200),"red",random.randint(5,15))
		turtle_4 = Turtle((100,-200),"black",random.randint(5,15))
		turtle_5 = Turtle((-100,-200),"yellow",random.randint(5,15))
		turtles = [turtle_1,turtle_5,turtle_4,turtle_3,turtle_2]
		#turtles are ready for a new race
				
	
scr.mainloop()