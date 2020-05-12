from tkinter import *
from tkinter import colorchooser
from tkinter.filedialog import asksaveasfilename
from PIL import Image


class App:
	def __init__(self ,rt):
		self.rt = rt
		self.rt.geometry("700x600")
		self.x = None
		self.y = None
		self.penwidth = 2
		self.pencolor = "black"
		self.pt_line = True
		self.taken =False
		self.start_x =None
		self.start_y =None
		self.canvas = Canvas(self.rt ,bd= 5 ,relief =SUNKEN)
		self.canvas.place(relx =0.1,rely = 0, relwidth =1, relheight = 1)
		self.canvas.config(bg = "white")
		self.canvas.bind("<B1-Motion>", self.paint)
		self.canvas.bind("<ButtonRelease-1>", self.reset)
		f1 = Frame(self.rt, bg = "gray",bd =6, relief =SUNKEN)
		f1.place(relx =0, rely =0, relwidth =0.1, relheight=1)
		Button(f1,text = "Rect",bg = "gray", command = self.rect).place(relx =0.1,rely =0.51, relwidth= 0.8 ,relheight =0.05)
		Button(f1,text = "Line",bg = "gray", command = self.line).place(relx =0.1,rely =0.57, relwidth= 0.8 ,relheight =0.05)
		Button(f1,text = "Eraser",bg = "gray", command = self.eraser).place(relx =0.1,rely =0.63, relwidth= 0.8 ,relheight =0.05)
		Label(f1,text = "Brush\nWidth", bg = "gray").place(relx= 0, rely =0.05,relheight= 0.04, relwidth = 1)
		colorselect = Scale(f1,bg = "gray",from_ = 50 ,to= 2, orient = VERTICAL, command = self.set_width)
		colorselect.place(relx =0, rely =0.1, relheight = 0.4, relwidth=1)
		self.menubar()	
	def eraser(self):
		self.pt_line = True
		self.pencolor = "white"	
	def rect(self):
		self.pt_line =False
	def line(self):
		self.pencolor ="black"
		self.pt_line =True	
	def paint(self, event):
		if self.pt_line:
			if self.x and self.y:
				self.canvas.create_line(self.x,self.y ,event.x,event.y, width = self.penwidth ,fill = self.pencolor, capstyle=ROUND, smooth = True )
			self.x = event.x
			self.y = event.y
		else:	
			if not self.taken:
				self.start_x = event.x
				self.start_y = event.y
				self.taken =True
			
				

	def reset(self, event):
		if not self.pt_line and self.start_y and self.start_x:
			self.canvas.create_rectangle(self.start_x,self.start_y ,event.x,event.y, width = self.penwidth ,fill = self.pencolor)
			self.start_y = None
			self.start_x = None
			self.taken =False
		self.x = None
		self.y = None
	def menubar(self):
		main = Menu(self.rt, bg= "#20232A")
		file_menu = Menu(main ,tearoff = False, bg = "gray")
		file_menu.add_command(label = "Save", command = self.save)
		main.add_cascade(label="File",menu =file_menu)
		edit_menu = Menu(main ,tearoff = False, bg = "gray")
		edit_menu.add_command(label = "Edit Color", command = self.edit_color)
		edit_menu.add_command(label = "Background fill", command= self.background_fill)
		edit_menu.add_command(label = "Clear", command= self.c_clear)
		main.add_cascade(label="Edit",menu =edit_menu)
		self.rt.config(menu = main)	
	def set_width(self,val):
		self.penwidth = val
	def edit_color(self):
		color = colorchooser.askcolor()
		self.pencolor = color[1]
	def background_fill(self):
		color = colorchooser.askcolor()
		self.canvas.config(bg=color[1])
	def c_clear(self):
		self.canvas.config(bg = "white")
		self.canvas.delete(ALL)	
	def save(self):
		pass


if __name__ =="__main__":
	root = Tk()
	app =App(root)
	root.mainloop()
