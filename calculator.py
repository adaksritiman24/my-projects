from tkinter import *

def delete():
	if calc["text"]!="0":
		t=calc["text"]
		l=len(t)
		calc["text"]=t[:len(t)-1:1]
		if calc["text"]=="":
			calc["text"]="0"

def all_clear():
	calc["text"]="0"

def plus():
	if(calc["text"]=="0"):
		calc["text"]=""	
	calc["text"]=calc["text"]+"+"
def minus():
	if(calc["text"]=="0"):
		calc["text"]=""	
	calc["text"]=calc["text"]+"-"
def multiply():
	if(calc["text"]=="0"):
		calc["text"]=""	
	calc["text"]=calc["text"]+"X"
def divide():
	if(calc["text"]=="0"):
		calc["text"]=""	
	calc["text"]=calc["text"]+"/"
def rem():
	if(calc["text"]=="0"):
		calc["text"]=""	
	calc["text"]=calc["text"]+"%"			
def pow():
	if(calc["text"]=="0"):
		calc["text"]=""	
	calc["text"]=calc["text"]+"^"	

def write1():
	if(calc["text"]=="0"):
		calc["text"]=""
	calc["text"]=calc["text"]+"1"
def write2():
	if(calc["text"]=="0"):
		calc["text"]=""
	calc["text"]=calc["text"]+"2"
def write3():
	if(calc["text"]=="0"):
		calc["text"]=""
	calc["text"]=calc["text"]+"3"

def write4():
	if(calc["text"]=="0"):
		calc["text"]=""
	calc["text"]=calc["text"]+"4"
def write5():
	if(calc["text"]=="0"):
		calc["text"]=""
	calc["text"]=calc["text"]+"5"

def write6():
	if(calc["text"]=="0"):
		calc["text"]=""
	calc["text"]=calc["text"]+"6"

def write7():
	if(calc["text"]=="0"):
		calc["text"]=""
	calc["text"]=calc["text"]+"7"

def write8():
	if(calc["text"]=="0"):
		calc["text"]=""
	calc["text"]=calc["text"]+"8"

def write9():
	if(calc["text"]=="0"):
		calc["text"]=""
	calc["text"]=calc["text"]+"9"
def write0():
	if(calc["text"]=="0"):
		calc["text"]=""
	calc["text"]=calc["text"]+"0"	

def decimal():
	if(calc["text"]=="0"):
		calc["text"]=""
	calc["text"]=calc["text"]+"."			

def equate():
	try:
		l=list(map(float,calc["text"].split("+")))
		a=0
		for i in range(len(l)):
			a=a+l[i]
		calc["text"]=str(a)	
	except:
		try:
			l=list(map(float,calc["text"].split("-")))
			a=l[0]
			for i in range(1,len(l)):
				a=a-l[i]
			calc["text"]=str(a)
		except:
			try:
				l=list(map(float,calc["text"].split("X")))
				a=1
				for i in range(0,len(l)):
					a=a*l[i]
				calc["text"]=str(a)	
			except:
				try:
					l=list(map(float,calc["text"].split("/")))
					a=l[0]
					for i in range(1,len(l)):
						a=a/l[i]
					calc["text"]=str(a)	
				except:
					try:
						l=list(map(float,calc["text"].split("%")))
						a=l[0]
						for i in range(1,len(l)):
							a=a%l[i]
						calc["text"]=str(a)	
					except:
						try:
							l=list(map(float,calc["text"].split("^")))
							a=l[0]
							for i in range(1,len(l)):
								a=a**l[i]
							calc["text"]=str(a)	
						except:
							calc["text"]="Error"		
				
root=Tk()
root.geometry("300x400")
root.title("CACULATOR by @S.Adak")
#root.config(bg='cadet blue')
b=Frame(root,bg="black")
b.place(relheight=1,relwidth=1)
f=Frame(b,bg="grey")
f.place(relx=0.005,rely=0.005,relheight=0.99,relwidth=0.99)
frame=Frame(f,bg="grey")
frame.place(relx=0.01,rely=0.01,relheight=0.98,relwidth=0.98)
global calc
calc=Label(frame,text="0",bg="black",fg="white",font=30,anchor="e",justify="right")
calc.place(relx=0.005,rely=0.01,relheight=0.17,relwidth=0.99)


b1=Button(frame,text="AC",bg="grey",bd=10,font=20,command=lambda: all_clear())
b1.place(relx=0,rely=0.2,relheight=0.16,relwidth=0.25)
b2=Button(frame,text="1",bg="grey",bd=10,font=20,command= lambda: write1())
b2.place(relx=0,rely=0.36,relheight=0.16,relwidth=0.25)
b3=Button(frame,text="4",bg="grey",bd=10,font=20,command= lambda: write4())
b3.place(relx=0,rely=0.52,relheight=0.16,relwidth=0.25)
b4=Button(frame,text="7",bg="grey",bd=10,font=20,command= lambda: write7())
b4.place(relx=0,rely=0.68,relheight=0.16,relwidth=0.25)
b5=Button(frame,text="=",bg="grey",bd=10,font=20,command= lambda: equate())
b5.place(relx=0,rely=0.84,relheight=0.16,relwidth=0.25)


b6=Button(frame,text=".",bg="grey",bd=10,font=20,command= lambda: decimal())
b6.place(relx=0.25,rely=0.2,relheight=0.16,relwidth=0.25)
b7=Button(frame,text="2",bg="grey",bd=10,font=20,command= lambda: write2())
b7.place(relx=0.25,rely=0.36,relheight=0.16,relwidth=0.25)
b8=Button(frame,text="5",bg="grey",bd=10,font=20,command= lambda: write5())
b8.place(relx=0.25,rely=0.52,relheight=0.16,relwidth=0.25)
b9=Button(frame,text="8",bg="grey",bd=10,font=20,command= lambda: write8())
b9.place(relx=0.25,rely=0.68,relheight=0.16,relwidth=0.25)
b10=Button(frame,text="0",bg="grey",bd=10,font=20,command= lambda: write0())
b10.place(relx=0.25,rely=0.84,relheight=0.16,relwidth=0.25)


b11=Button(frame,text="DEL",bg="grey",bd=10,font=20,command=lambda: delete())
b11.place(relx=0.50,rely=0.2,relheight=0.16,relwidth=0.25)
b12=Button(frame,text="3",bg="grey",bd=10,font=20,command= lambda: write3())
b12.place(relx=0.50,rely=0.36,relheight=0.16,relwidth=0.25)
b13=Button(frame,text="6",bg="grey",bd=10,font=20,command= lambda: write6())
b13.place(relx=0.50,rely=0.52,relheight=0.16,relwidth=0.25)
b14=Button(frame,text="9",bg="grey",bd=10,font=20,command= lambda: write9())
b14.place(relx=0.50,rely=0.68,relheight=0.16,relwidth=0.25)
b15=Button(frame,text="^",bg="grey",bd=10,font=20,command= lambda: pow())
b15.place(relx=0.50,rely=0.84,relheight=0.16,relwidth=0.25)

b16=Button(frame,text="+",bg="grey",bd=10,font=20,command= lambda: plus())
b16.place(relx=0.75,rely=0.2,relheight=0.16,relwidth=0.25)
b17=Button(frame,text="-",bg="grey",bd=10,font=20,command= lambda: minus())
b17.place(relx=0.75,rely=0.36,relheight=0.16,relwidth=0.25)
b18=Button(frame,text="X",bg="grey",bd=10,font=20,command= lambda: multiply())
b18.place(relx=0.75,rely=0.52,relheight=0.16,relwidth=0.25)
b19=Button(frame,text="/",bg="grey",bd=10,font=20,command= lambda: divide())
b19.place(relx=0.75,rely=0.68,relheight=0.16,relwidth=0.25)
b20=Button(frame,text="%",bg="grey",bd=10,font=20,command= lambda: rem())
b20.place(relx=0.75,rely=0.84,relheight=0.16,relwidth=0.25)



root.mainloop()

