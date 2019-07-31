from tkinter import *
import sqlite3
import datetime

class mainpage:
	def __init__(self,rt):
		rt.geometry("500x400")
		rt.title("Birthday Reminder")
		global frame
		frame=Frame(rt,bg="grey")
		frame.place(relheight=1,relwidth=1)
		Label(frame,bg="grey",fg="Black",text="WELCOME TO BIRTHDAY REMINDER",font=("Times New Roman",15,"underline bold"),justify="center").place(relx=0.02,rely=0.05,relwidth=0.96)
		global l1
		du=Frame(frame,bg="red")
		du.place(relx=0.12,rely=0.27,relheight=0.5,relwidth=0.76)
		l1=Label(du,bg="black",fg="white",font=("Arial",13,"normal"),justify="left",anchor="nw")
		l1.place(relx=0.02,rely=0.15,relheight=0.83,relwidth=0.96)
		Label(du,bg="red",text="Recent/Upcomming Birthdays :",fg="yellow",font=("Arial",14,"normal"),justify="left",anchor="nw").place(relx=0.01,rely=0,relheight=0.15,relwidth=0.98)
		button=Button(frame,bg="violet",fg="red",bd=5,text="Add new birthday",font=18,command=lambda: self.add_page(rt))
		button.place(relx=0.1,rely=0.8)
		button1=Button(frame,bg="red",fg="white",bd=5,text="Delete",font=18,command=lambda: self.deletepage(rt))
		button1.place(relx=0.5,rely=0.8)
		button2=Button(frame,bd=5,bg="black",fg="yellow",text="Quit",font=18,command=frame.quit)
		button2.place(relx=0.8,rely=0.8)	
		button3=Button(frame,bd=5,bg="green",fg="black",text="View Birthday",font=13,command=lambda: self.view_birth(rt))
		button3.place(relx=0.35,rely=0.15,relheight=0.09)
		self.upcomming_bdays()
	def deletepage(self,r):
		global e1
		global d_n
		global fr3
		d_n=StringVar()
		r.title("Delete Profile")	
		fr3=Frame(frame,bg="blue")
		fr3.place(relheight=1,relwidth=1)
		Label(fr3,bg="blue",fg="gold",text="Enter name of the person \nwhose profile is to be deleted:",justify="left",font=("Arial",15,"bold")).place(relx=0.1,rely=0.05)		
		e1=Entry(fr3,textvariable=d_n,bd=10,bg="green",fg="white",font=15)
		e1.place(relx=0.1,rely=0.2,relwidth=0.7,relheight=0.15)
		back=Button(fr3,bd=7,bg="yellow",fg="blue",text="Return",font=("Arial",14,"normal"),command=lambda: self.return_page())
		back.place(relx=0.8,rely=0.8)
		delete=Button(fr3,bd=7,bg="yellow",fg="red",text="Delete",font=("Arial",14,"normal"),command=lambda: self.delete_data())
		delete.place(relx=0.1,rely=0.8)		
	def return_page(self):
		mainpage(root)
	def add_page(self,r):
		r.title("Add New")	
		global name
		global day
		global month
		global year
		name= StringVar()
		day= StringVar()
		month=StringVar()
		year=StringVar()
		global e2
		global e3
		global e4
		global e5
		global fr1
		fr1=Frame(frame,bg="yellow")
		fr1.place(relheight=1,relwidth=1)
		back=Button(fr1,bd=7,bg="red",fg="silver",text="Return",font=("Arial",14,"normal"),command=lambda: self.return_page())
		back.place(relx=0.8,rely=0.8)
		Label(fr1,bg="yellow",fg="black",text="Enter name of the person: ",justify="left",font=("Arial",16,"normal")).place(relx=0.1,rely=0.05)				
		e2=Entry(fr1,textvariable=name,bd=10,bg="green",fg="white",font=15)
		e2.place(relx=0.1,rely=0.16,relwidth=0.7,relheight=0.12)
		add=Button(fr1,bd=7,bg="green",fg="black",text="Add",font=("Arial",14,"normal"),command=lambda: self.insert())
		add.place(relx=0.1,rely=0.8)
		Label(fr1,bg="yellow",fg="black",text="Enter birthday:\n\nDay(DD)     Month(MM)     Year(YYYY)",justify="left",font=("Arial",16,"normal")).place(relx=0.1,rely=0.35)	
		e3=Entry(fr1,textvariable=day,bd=5,bg="grey",fg="black",font=15)
		e3.place(relx=0.1,rely=0.57,relwidth=0.16,relheight=0.1)
		e4=Entry(fr1,textvariable=month,bd=5,bg="grey",fg="black",font=15)
		e4.place(relx=0.33,rely=0.57,relwidth=0.16,relheight=0.1)
		e5=Entry(fr1,textvariable=year,bd=5,bg="grey",fg="black",font=15)
		e5.place(relx=0.6,rely=0.57,relwidth=0.23,relheight=0.1)
	def insert(self):
		n=name.get()
		d=day.get()
		m=month.get()
		y=year.get()
		ct=sqlite3.connect("birthdays.db")
		with ct:
			curser=ct.cursor()
			curser.execute("CREATE TABLE IF NOT EXISTS Members(Name text, Day number,Month number, Year number)")
			try:
				curser.execute("INSERT INTO Members(Name,Day,Month,Year) VALUES(?,?,?,?)",(n,int(d),int(m),int(y)))
				self.clear()
				Label(fr1,bg="yellow",text="Birthday successfully added !",fg="red",font=8).place(relx=0.2,rely=0.7)
			except:
				Label(fr1,bg="yellow",text="Failed to add birthday !",fg="red",font=8).place(relx=0.2,rely=0.7)	
			ct.commit()
	def view(self):
		lb["text"]=''
		mon=("January","February","March","April","May","June","July","August","September","October","November","December")
		v_n=v_b.get()
		e6.delete(0,END)
		conn=sqlite3.connect("birthdays.db")
		txt=''
		with conn:
			c=conn.cursor()
			c.execute("SELECT * FROM Members WHERE Name=?",(v_n,))
			for r in c.fetchall():
				n=r[0]
				dd=r[1]
				mm=r[2]
				yyyy=r[3]
				txt=n+"'s"+" birthday is on \n"+str(dd)+" "+mon[mm-1]+" "+str(yyyy)

		conn.commit()
		if txt=="":
			txt="Data Not Available!"
		lb['text']=txt	
	def upcomming_bdays(self):
		mon=("January","February","March","April","May","June","July","August","September","October","November","December")
		tday=datetime.date.today()
		today_day=int(tday.day)
		temp=32
		today_month=int(tday.month)
		top_show=''
		conn=sqlite3.connect("birthdays.db")
		with conn:
			c=conn.cursor()
			for j in range(today_month,13):
				for i in range(today_day,32):
					c.execute("SELECT * FROM Members WHERE Day=? and Month=?",(i,j,))
					for r in c.fetchall():
						top_show=top_show+"-> "+r[0]+" has birthday on "+str(r[1])+" "+mon[r[2]-1]+"."+"\n"	
				today_day=1	

			for j in range(1,today_month+1):
				for i in range(1,temp):
					c.execute("SELECT * FROM Members WHERE Day=? and Month=?",(i,j,))
					for r in c.fetchall():
						top_show=top_show+"-> "+r[0]+" has birthday on "+str(r[1])+" "+mon[r[2]-1]+"."+"\n"											
					if j==today_month-1:
						temp=datetime.date.today().day			
			conn.commit()	
			l1["text"]=top_show	
	def delete_data(self):
		deleted_name=d_n.get()
		conn=sqlite3.connect("birthdays.db")
		with conn:
			c=conn.cursor()
			c.execute("DELETE FROM Members WHERE Name=?",(deleted_name,))
			conn.commit()
		e1.delete(0,END)
		Label(fr3,bg="blue",fg="pink",font=("Arial",20,"normal"),text="Profile Deleted !").place(relx=0.2,rely=0.5)



	def clear(self):
		e2.delete(0,END)
		e3.delete(0,END)
		e4.delete(0,END)
		e5.delete(0,END)			
	def view_birth(self,r):
		global v_b
		v_b=StringVar()
		global e6
		global fr2
		global lb
		r.title("View Birthday")	
		fr2=Frame(frame,bg="red")
		fr2.place(relheight=1,relwidth=1)
		Label(fr2,bg="red",fg="gold",text="Enter name of the person \nwhose birthday you want to view:",justify="left",font=("Comic Sans MS",15,"bold")).place(relx=0.1,rely=0.05)		
		e6=Entry(fr2,textvariable=v_b,bd=10,bg="green",fg="white",font=15)
		e6.place(relx=0.1,rely=0.22,relwidth=0.7,relheight=0.15)
		back=Button(fr2,bd=7,bg="yellow",fg="blue",text="Return",font=("Arial",14,"normal"),command=lambda: self.return_page())
		back.place(relx=0.8,rely=0.8)
		view=Button(fr2,bd=7,bg="blue",fg="yellow",text="View",font=("Arial",14,"normal"),command=lambda: self.view())
		view.place(relx=0.1,rely=0.8)	
		lb=Label(fr2,bg="red",fg="white",font=("Comic Sans MS",20,"bold"),justify="left")
		lb.place(relx=0.1,rely=0.5)					
root=Tk()
b=mainpage(root)
root.mainloop()