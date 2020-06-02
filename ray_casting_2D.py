import numpy as np
import pygame
'''
This is a simple ray casting simulation in 2D.
Move the ligth source using mouse curser to see the shadow effects created by the ray.
'''
#Defining of the Ray which holds all the rays produced by the source
class Rays:
	def __init__(self):
		#length of each ray if not hit by any obstacle
		self.length = 1300
		#total number of rays,(this can be changed as per the computing power of the computer, more rays-->better effects--> more computing power required)
		self.lines = 100
		self.g = np.linspace(0, 44/7 ,self.lines)
		self.g[-1] = self.g[-2]
		#colour of each ray(kept to white)
		self.color =(255,255,255)
		
	def show(self):
		#position of the source of all ray == position of the mouse on the screen.
		self.x,self.y = pygame.mouse.get_pos()
		#self.x1 and self.y1 contains end positions(x, y respectively) of all the rays 
		self.x1, self.y1 = self.x+ self.length*np.cos(self.g) ,self.y + self.length*np.sin(self.g)
	def draw(self, scr):	
		#Showing all the rays in the screen as line segments
		for i, j in zip(self.x1,self.y1):
			pygame.draw.line(scr,self.color,(self.x,self.y),(i,j),2)

#Defining some hurdles in the screen (as line segments)
class Hurdles:
	def __init__(self):
		#declaring the 6 hurdles(line segments as =[(x_start, y_start),(x_end,y_end)])
		self.h1 = [(280,390),(490,200)]
		self.h2 = [(560,600),(320,400)]
		self.h3= [(400,200),(200,100)]
		self.h4 = [(60,283),(120,600)]
		self.h5 = [(409,540),(390,267)]
		self.h6 = [(746,265),(560,389)]
		#making a list of line segments
		self.h = [self.h1,self.h2,self.h3,self.h4,self.h5, self.h6]
		#coloring hurdles as dull white
		self.color = (130,130,130)

	def show(self, scr):
		#showing the hurdles on the screen
		for h in self.h:
			pygame.draw.line(scr,self.color,(h[0]),(h[1]),1)

#Main class which will run our simulation in pygame window.
class Game:
	def __init__(self):
		self.run =True
		self.black = (0,0,0)
		self.dimension =(800,800)
		self.main()
	def main(self):
		#this function will run the mainloop of the program.
		clock =pygame.time.Clock()
		#declaring rays
		#declaring hurdles
		self.rays = Rays()
		self.hurdles = Hurdles()
		#setup environment for pygame
		pygame.init()
		self.scr = pygame.display.set_mode(self.dimension)
		pygame.display.set_caption("Ray Casting 2D by @sritiman_adak")
		while self.run:
			#predefined frame rate for the simulation(not much of use ,mostly depends on the computer's capability)
			clock.tick(60)
			#event type checking in pygame
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					self.run =False
				self.display()
		#quitting the pygame window once self.run is false			
		pygame.quit()			
	def display(self):
		#refresh the background of the screen with black colour after every iteration.
		self.scr.fill(self.black)
		self.rays.show()
		#before drawing the rays we must check whether the ray is intersecting with any of the hurdle(line segments) present on the screen.
		self.check_collision()
		self.rays.draw(self.scr)
		self.hurdles.show(self.scr)
		pygame.display.flip()

	def check_collision(self):
		# !!IMPORTANT function which checks whether ray is hitting any line segment or not
		# a,b are the two end points of the line segment(hurdles) in the screen for each h in self.hurdles.h
		#c,d are the two end points of the ray line segments in the array of rays.c is obviously the mouse curser position on the screen.
		# d point is calculated from the arrays holding the x position  and y positions of all the rays respectively.  
		c = np.array([self.rays.x,self.rays.y])
		for h in self.hurdles.h:
			a = np.array(h[0])
			b = np.array(h[1])
			ca = c-a
			ba = b-a
			neu = np.cross(ca, ba)
			for i in range(self.rays.lines):
				d =np.array([self.rays.x1[i], self.rays.y1[i]])
				dc=d-c
				deno = np.cross(ba, dc)
				#t and u denote the fraction of the linesegment 'hurdle' , 'ray' respectively covered from points "a" and "c" respectively after which there is a intersection found.
				u = neu/deno
				t = np.cross(ca,dc)/deno
				#only if t and u lies between 0 and 1 implies that there is an intersection between the two line segments found. 
				if t<=1 and t>=0 and u<=1 and u>=0:
					#once the intersection point is found ,we will extend the considered ray only uptill the point of intersection
					#so the final x and y positions of the considered ray is updated in the respective arrays before displaying them on the screen.
					point = a + t*(b-a)
					self.rays.x1[i] = point[0]
					self.rays.y1[i] = point[1]




if __name__ =="__main__":
	Game()
