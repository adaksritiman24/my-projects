from tkinter import*
import sqlite3

def re_tress(wr):
	rec["text"]=wr



def write_recent():
	anbe=""
	cont=sqlite3.connect("iron_man_club(list).db")
	with cont:
		curs=cont.cursor()
		curs.execute("SELECT Username FROM Members")
		for r in curs.fetchall():
			anbe=r[0]+"\n"+anbe
		cont.commit()
	re_tress(anbe)


def recent():
	global rec	
	rec=Label(main_screen,fg="silver",bg="black",anchor="nw",justify="left",font=4)
	rec.place(relx=0.05,rely=0.3,relwidth=0.2,relheight=0.5)
	write_recent()


def rewrite(hh):
	lab3["text"]=hh


def show():
	total_chat=''
	c_n=sqlite3.connect("chats.db")
	with c_n:
		curser=c_n.cursor()
		curser.execute("SELECT * FROM Chats ")
		for row in curser.fetchall():
			total_chat=total_chat+"\n"+row[0]
		rewrite(total_chat)	
		c_n.commit()
	en.delete(0,END)		

def initial():
	t_c=''
	c_n=sqlite3.connect("chats.db")
	with c_n:
		curser=c_n.cursor()
		curser.execute("SELECT * FROM Chats ")
		for row in curser.fetchall():
			t_c=t_c+"\n"+row[0]
		c_n.commit()
	return t_c	


def write():
	talks=user+": "+entry.get()
	if entry.get()!="":
		connect=sqlite3.connect("chats.db")
		with connect:
			co=connect.cursor()
			co.execute("CREATE TABLE IF NOT EXISTS Chats(chat text)")
			co.execute("INSERT INTO Chats(chat) VALUES (?)",(talks,))
			connect.commit()
		show()	


 
def main_page():
	global entry
	global lab3
	global FR
	global en
	global main_screen
	entry=StringVar()

	main_screen=Toplevel(screen)
	main_screen.title("HOME PAGE")
	main_screen.geometry("849x549")
	img=PhotoImage(file="iron_man3.png")
	bg=Label(main_screen,image=img)
	bg.place(relwidth=1,relheight=1)
	greet="Welcome  "+user+" !"
	Label(bg,bg="black",fg="gold",text=greet,anchor="w",font=25,justify="left").place(relx=0.02,rely=0,relwidth=0.6,relheight=0.1)
	Label(bg,text="Recent members:",bg="black",fg="yellow",font=("Comic Sans MS",15,"normal"),anchor="n").place(relx=0.02,rely=0.25,relwidth=0.2,relheight=0.06)
	i=Label(bg,text="Hello all!,welcome to the fan club of iron man,\nthe most famous Avenger.You can write\npublicly overhere.(Please don't use abusive words)",bg="black",fg="white",anchor="w",justify="left")
	i.place(relx=0.01,rely=0.1,relwidth=0.35,relheight=0.1)
	recent()
	Label(bg,text="Recent Chats",font=15,bg="black",fg="violet",anchor="s").place(relx=0.36,rely=0.1,relwidth=0.15,relheight=0.1)
	FR=Frame(bg,bd=5,bg="red")
	FR.place(relx=0.25,rely=0.2,relwidth=0.5,relheight=0.5)
	lab3=Label(FR,text=initial(),bg="black",fg="orange",anchor="sw",justify="left")
	lab3.place(relwidth=1,relheight=1)
	en=Entry(bg,textvariable=entry,bd=10,font=15)
	en.place(relx=0.3,rely=0.75,relwidth=0.3,relheight=0.2)
	Label(bg,bg="black",fg="green",text="Write Here",anchor="w",font=20).place(relx=0.15,rely=0.75,relwidth=0.12,relheight=0.2)
	Button(bg,text="Post",bd=10,bg="green",fg="white",font=20,command=lambda: write()).place(relx=0.65,rely=0.8,relwidth=0.1,relheight=0.1)

	main_screen.mainloop()


def register():
	
	username_c=username.get()
	email_c=email.get()
	country_c=country.get()
	occ_c=occ.get()
	hobby_c=hobby.get()
	gender_c=gender.get()
	age_c=age.get()
	dob_c=dob.get()
	phone_c=phone.get()
	password_c=password.get()
	#important
	con=sqlite3.connect("iron_man_club(list).db")
	with con:
		cursor=con.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS Members(Username text,Email text,Country text,Occupation text,Hobby text,Gender text,Age text,DOB text,phone_no text,Password text)")
		cursor.execute("INSERT INTO Members (Username,Email,Country,Occupation,Hobby,Gender,Age,DOB,phone_no,Password) VALUES(?,?,?,?,?,?,?,?,?,?)",(username_c,email_c,country_c,occ_c,hobby_c,gender_c,age_c,dob_c,phone_c,password_c))
		con.commit()
	Label(rt,text="Membership successfull!",bg="black",fg="green",anchor="n").place(relx=0.05,rely=0.94,relwidth=0.9,relheight=0.20)
	clear()

def recognition():
	global user
	user=un.get()
	pas=pw.get()
	con=sqlite3.connect("iron_man_club(list).db")
	with con:
		c=con.cursor()
		c.execute('SELECT * FROM Members WHERE Password=? AND Username=?',(pas,user,))
		if len(c.fetchall())==1:
			main_page()
		elif len(c.fetchall())==0:
			Label(screen,text="Wrong username or password!",bg="black",fg="red",font=15).place(relx=0.1,rely=0.6,relheight=0.10,relwidth=0.3)
		

		con.commit()
	
				
		





def login():
	global screen
	global un
	global pw
	un=StringVar()
	pw=StringVar()
	screen=Toplevel(root)
	screen.title("LOGIN")
	screen.geometry("1024x516")
	img=PhotoImage(file="iron_man2.png")
	lab=Label(screen,image=img)
	lab.place(relheight=1,relwidth=1)
	lab1=Label(lab,text="Username",font=("Comic Sans MS",24,"normal"),fg="pink",bg="black",justify="left").place(relx=0.1,rely=0,relheight=0.3,relwidth=0.3)
	lab2=Label(lab,text="Password",font=("Comic Sans MS",24,"normal"),fg="pink",bg="black",justify="left").place(relx=0.1,rely=0.25,relheight=0.3,relwidth=0.3)
	n=Entry(lab,textvariable=un,bd=10,bg="blue",fg="white",font=16)
	n.place(relx=0.1,rely=0.2,relheight=0.10,relwidth=0.3)
	m=Entry(lab,textvariable=pw,bd=10,bg="red",fg="white",font=16)
	m.place(relx=0.1,rely=0.45,relheight=0.10,relwidth=0.3)
	Button(lab,text="LOGIN",bd=12,bg="gold",fg="brown",font=("arial",20,"bold"),command=lambda: recognition()).place(relx=0.15,rely=0.8,relheight=0.10,relwidth=0.2)

	screen.mainloop()

def clear():
	a.delete(0,END)
	b.delete(0,END)
	c.delete(0,END)
	d.delete(0,END)
	e.delete(0,END)
	f.delete(0,END)
	g.delete(0,END)
	h.delete(0,END)
	i.delete(0,END)
	j.delete(0,END)


	

def sign_in():
	global rt
	rt=Toplevel(root)
	rt.title("LOGIN")
	rt.geometry("700x500")
	global username
	global email
	global country
	global occ
	global hobby
	global gender
	global age
	global dob
	global phone
	global password
	username=StringVar()
	email=StringVar()
	country=StringVar()
	occ=StringVar()
	hobby=StringVar()
	gender=StringVar()
	age=StringVar()
	dob=StringVar()
	phone=StringVar()
	password=StringVar()
	global a
	global b
	global c
	global d
	global e
	global f
	global g
	global h
	global i
	global j


	fr=Frame(rt,bg="black",bd=10)
	fr.place(relwidth=1,relheight=1)
	Label(fr,text="New Membership Login",bg="black",fg="silver",font=("Comic Sans MS",15,"underline")).place(relwidth=1,rely=0.02,relheight=0.1)
	Label(fr,bg="black",fg="gold",text="Username:\nEmail:\nCountry:\nOccupation:\nHobby:\nGender:\nAge:\nDOB(ddmmyyyy):\nPhone number:\nPassword:",justify="left",font=("SimSun",25,"bold")).place(relx=0.1,rely=0.11,relwidth=0.4,relheight=0.765)
	a=Entry(fr,bd=4,textvariable=username,font=("Arial",12,"normal"))
	a.place(relx=0.5,rely=0.15,relwidth=0.36,relheight=0.06)
	b=Entry(fr,bd=4,textvariable=email,font=("Arial",12,"normal"))
	b.place(relx=0.5,rely=0.22,relwidth=0.45,relheight=0.06)
	c=Entry(fr,bd=4,textvariable=country,font=("Arial",12,"normal"))
	c.place(relx=0.5,rely=0.29,relwidth=0.35,relheight=0.06)
	d=Entry(fr,bd=4,textvariable=occ,font=("Arial",12,"normal"))
	d.place(relx=0.5,rely=0.36,relwidth=0.35,relheight=0.06)
	e=Entry(fr,bd=4,textvariable=hobby,font=("Arial",12,"normal"))
	e.place(relx=0.5,rely=0.43,relwidth=0.35,relheight=0.06)
	f=Entry(fr,bd=4,textvariable=gender,font=("Arial",12,"normal"))
	f.place(relx=0.5,rely=0.50,relwidth=0.12,relheight=0.06)
	g=Entry(fr,bd=4,textvariable=age,font=("Arial",12,"normal"))
	g.place(relx=0.5,rely=0.57,relwidth=0.12,relheight=0.06)
	h=Entry(fr,bd=4,textvariable=dob,font=("Arial",12,"normal"))
	h.place(relx=0.5,rely=0.64,relwidth=0.24,relheight=0.06)
	i=Entry(fr,bd=4,textvariable=phone,font=("Arial",12,"normal"))
	i.place(relx=0.5,rely=0.71,relwidth=0.24,relheight=0.06)
	j=Entry(fr,bd=4,textvariable=password,font=("Arial",12,"normal"))
	j.place(relx=0.5,rely=0.78,relwidth=0.12,relheight=0.06)
	Button(fr,text="Reset",bd=10,bg="blue",fg="white",command=lambda: clear()).place(relx=0.1,rely=0.87,relwidth=0.3,relheight=0.07)
	Button(fr,text="Submit",bd=10,bg="green",fg="white",command=lambda: register()).place(relx=0.5,rely=0.87,relwidth=0.3,relheight=0.07)
		

	rt.mainloop()


def club():
	global root
	root=Tk()
	root.title("Club")
	root.geometry("500x400")
	bg=PhotoImage(file="Iron_man.png")
	img=Label(root,image=bg)
	img.place(relwidth=1,relheight=1)
	Label(img,text="Iron Man Fan Club",bd=10,bg="black",fg="yellow",font=("Comic Sans MS",20,"bold")).place(relx=0,rely=0.1,relwidth=1,relheight=0.2)
	Label(img,text="**World's Largest fanclub**\n--- Over 1B menbers---",bg="black",fg="white").place(relx=0,rely=0.25,relwidth=1,relheight=0.1)
	Button(root,text="Sign In",bd=10,bg="red",fg="white",command=lambda: sign_in()).place(relx=0.35,rely=0.4,relwidth=0.3,relheight=0.1)
	Button(root,text="Log In",bd=10,bg="green",fg="white",command=lambda:login()).place(relx=0.35,rely=0.6,relwidth=0.3,relheight=0.1)

	root.mainloop()



club()