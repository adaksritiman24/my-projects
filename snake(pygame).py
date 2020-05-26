import pygame
import random
import time
'''
This ia a self created version of the original snake game.
'''
'''
 creating a class Food for the snake in the game.
 the food will be located at some random positions in the game screen.

''' 
class Food:
	def __init__(self):
		self.x = 20*random.randint(0, 29)
		self.y = 20*random.randint(0, 29)
		#thi is the rgb value of yellow indicating the food color.
		self.color =(250,250,0)
	def show_up(self, win):
		# the food will be a square of size 20X20.
		pygame.draw.rect(win,self.color,(self.x,self.y, 20, 20))	
'''
defining the snake object in our game.
initially our snake will belocated at the middle of the screen.
'''
class Snake:
	def __init__(self):
		self.x = 280
		self.y = 280
		#i have chosen the colour of the snake to be Red.
		self.headcolor = (255,0,0)
		#speed by which the snake will move on the screen.
		self.speed =20
		self.all_false()
		# this list will contain the positon of the squares(which will form the snake's body) which will determine the location of the body of the snake in the game screen.
		#intially the snake has only head and no body.
		self.bodies= []
	def create_body(self,x,y, b1,b2):
		#adding the location of a new body in the list of self.bodies of the snake once this function is called.
		if len(self.bodies)==0:
			self.bodies.append((x,y))
		else:
			self.bodies.append((b1,b2))	
	
	def mov_bodies(self,x,y):
		# the position of the each and every body part of the snake is moved to the positon of their preeceding body part, and the 
		#first body part(that is closest to the snake head) is moved to the previous positon of the snake head.
		if len(self.bodies)>=1:
			for i in range(len(self.bodies)-1,0,-1):
				self.bodies[i]=self.bodies[i-1]
			self.bodies[0]=(x,y)	
	
	def all_false(self):	
		#this function is to stop the snake movement in the screen.
		# it is called at the beginning of the game and also called when there is a gameover.
		self.up =False
		self.down =False
		self.left =False
		self.right =False

	def draw(self, win):
		#this function draws the snake head on the screen.
		pygame.draw.rect(win,self.headcolor,(self.x,self.y,20,20))	
	def body_draw(self,win):	
		#this function draws the snake bodies on the screen.
		for body in self.bodies:
			pygame.draw.rect(win,(255,255,255),(body[0],body[1],20,20))	

	def move(self):
		'''
		this function is used to move the coordinate of the snake head.
		for eg. when self.up =True means, the player has presses the down arrow key and now I have increased
		the y cordinate of the snake by 20(self.speed) ,indicating the new position of the snake head.
		'''
		if self.up==True:
			self.y-=self.speed
		elif self.down==True:
			self.y+=self.speed
		elif self.left==True:
			self.x-=self.speed
		elif self.right==True:	
			self.x+=self.speed
	#these are the four function that will be called from Game ,which will help to decide which move to do.	
	# for example if a snake is moving up, then self.up will be True.  In that case the player will not be allowedto move the snake down.
	# same goes for the remaining moves.		
	def mov_up(self):
		if self.down==False:
			self.all_false()
			self.up = True
	def mov_down(self):
		if self.up==False:
			self.all_false()
			self.down = True

	def mov_left(self):
		if self.right==False:
			self.all_false()
			self.left = True

	def mov_right(self):
		if self.left==False:
			self.all_false()
			self.right = True
'''
this is the main game body that must be called to play the game.
this will containg every elements in the game.
'''
class Game:
	def __init__(self):
		#screen height and width.
		self.height = 600
		self.width = 600
		self.run =False
		#score of the player. Initially 0.
		self.score = 0
		self.highscore=0
		#initialisation of pyagme font.
		pygame.font.init()
		self.f1 = pygame.font.SysFont("lucida", 30)
		self.f2 = pygame.font.SysFont("comicsans", 60)
		self.main()

	def main(self):
		#the allowdraw helps in determining the snake's frame rate in our game
		self.allowdraw=0
		'''
		when self.mov is true ,any key press is calling a function else it is not.  
		'''
		self.mov=True
		self.super =False
		self.pos_x=None
		self.pos_y=None
		self.bd1=None
		self.bd2=None
		clock = pygame.time.Clock()
		#creating the instances of the snake and food.
		self.snake =Snake()
		self.food = Food()
		pygame.init()
		self.run =True
		#setting up the pygame window and its title.
		self.win = pygame.display.set_mode((self.width,self.height))
		pygame.display.set_caption("Snake Game by Sritiman Adak")
		while(self.run):
			#this is use to set the fps of the game to 60.
			clock.tick(60)
			#This is just a mandatory check for quit event in pygame.
			#i helps to exit from the while loop as well as quit pygame when the player is trying to quit the game.
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					self.run=False		
			#key bindings
			keys = pygame.key.get_pressed()
			#when player presses up arrow.
			if keys[pygame.K_UP]:
				if self.mov:
					self.snake.mov_up()
					self.super=True
					self.mov=False
			#when player presses down arrow		
			if keys[pygame.K_DOWN]:
				if self.mov:
					self.snake.mov_down()	
					self.super =True
					self.mov=False
			#when player presses left arrow		
			if keys[pygame.K_LEFT]:
				if self.mov:
					self.snake.mov_left()	
					self.super =True
			#when player presses right arrow		
			if keys[pygame.K_RIGHT]:
				if self.mov:
					self.snake.mov_right()
					self.super=True
					self.mov =False
			#this draws all objects on the screen that we created.
			self.draw_window()
			self.allowdraw+=1
		
		pygame.quit()
	#printing the score of the player and the highest score at the top left corner of the game screen.	
	def scoring(self):
		t1 =self.f1.render(f"Score: {self.score}",False,(200,200,0))	
		t2 =self.f1.render(f"Highest Score: {self.highscore}",False,(200,200,0))
		self.win.blit(t1,(5,5))	
		self.win.blit(t2,(120,5))	
	#printing SNAKE GAME on the middle of screen at the beginning of the game.	
	def snake_game(self):
		t1 =self.f2.render(f"SNAKE GAME",False,(230,230,230))
		self.win.blit(t1,(150,200))		

	def draw_window(self):
		#declaring the screen colour as dark blue.
		self.win.fill((0,0,80))
		self.snake.body_draw(self.win)
		self.snake.draw(self.win)
		self.food.show_up(self.win)
		if self.super==False:
			self.snake_game()
		if self.allowdraw>5:
			'''
			self.pos_x and self.pos_y helps to keep track the previous position of the snake in the screen
			once the snake has moved away from that position.
			''' 	
			self.pos_x = self.snake.x
			self.pos_y = self.snake.y

			if len(self.snake.bodies)>0:
				#Keeping track of the position of the last square of the snake body.
				self.bd1 = self.snake.bodies[len(self.snake.bodies)-1][0]
				self.bd2 = self.snake.bodies[len(self.snake.bodies)-1][1]
			#moving the sanke on the screen.	
			self.snake.move()
			self.snake.mov_bodies(self.pos_x,self.pos_y)
			# function for checking the collision of the snake head and food.
			self.check_collisions()	
			# function for checking the collision of snake head with its own body.
			self.body_collision()
			# function for checking the collision of the snake head with the screen boundary.
			self.check_wall()
			self.allowdraw=0
			self.mov=True	
		#prints the score on the screen.	
		self.scoring()		
		pygame.time.delay(10)
		#updating the pygame screen.
		pygame.display.flip()

	def check_collisions(self):
		if self.snake.x==self.food.x and self.snake.y==self.food.y:
			#if there is a collision with the food, the score is increased by 1 and the the food is set to a new position by creating a new instance of the food.
			#a new square is also added to the snake body.
			self.food=Food()	
			self.snake.create_body(self.pos_x,self.pos_y, self.bd1, self.bd2)
			self.score+=1
			'''
			if the score is one more than the highscore then the highscore is also increased by 1
			else if the score less than or equal to highscore, then the highscore is left unchanged.
			'''
			if self.highscore+1==self.score:
				self.highscore+=1
	def check_wall(self):
		'''
		Once there is a collision of the snake head with the wall(screen boundary),
		game is over, program stops for 2 sec,a new instance of the food is created on the screen,
		all the snake body parts are deleted,movement of the snake is stopped, and position of the 
		snake is again set to the middle of the screen.
		Score is set to 0.
		Same things are done in the body_collision function.
		'''
		if self.snake.x>580 or self.snake.x<0 or self.snake.y>580 or self.snake.y<0:
			time.sleep(2)
			self.food=Food()	
			self.snake.bodies=[]
			self.snake.all_false()
			self.snake.x,self.snake.y =280,280	
			self.score=0
	def body_collision(self):
		for body in self.snake.bodies:
			if self.snake.x == body[0] and self.snake.y == body[1]:
				time.sleep(2)	
				self.food=Food()
				self.snake.bodies=[]
				self.snake.all_false()
				self.snake.x,self.snake.y =280,280	
				self.score=0


if __name__=="__main__":
	Game()