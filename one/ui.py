from tkinter import*
from time import sleep
from tkinter.messagebox import showinfo
import one.data
import one.transition
tk=Tk()
tk.title("KNOCK CODE")
tk.resizable(0,0)

img = PhotoImage(file='one/logos/img.png')
tk.tk.call('wm', 'iconphoto', tk._w, img)

one.transition.transition(tk)
rf=Frame(tk,width=500,height=600)
rf.pack()
canvas=Canvas(rf,width=500,height=600)
canvas.pack()
tk.update()
store=list()
store1=list()
global count
global count1
count=0
count1=0
class inputs:
	def draw(self):		
		print("========================== KNOCK CODE STARTED =========================")		
		print("") 
		self.a = StringVar()
		self.b = StringVar()
		self.lb1=Label(rf,text="ROWS")
		lb2=Label(rf,text="COLUMNS")
		ent1=Entry(rf,textvariable=self.a)
		ent2=Entry(rf,textvariable=self.b)
		bt1=Button(text="GENERATE PAD")

		self.lb1.pack()
		self.lb1.place(x=115,y=10)
		ent1.pack()
		ent1.place(x=50,y=30)
		lb2.pack()
		lb2.place(x=320,y=10)
		ent2.pack()
		ent2.place(x=270,y=30)


		bt1.bind("<Button-1>",self.generate)
		bt1.pack()
		bt1.place(x=190,y=70)
		
		

	def generate(self,event):
		global x1,y1,x2,y2
		x1,y1,x2,y2=(50,125,450,475)
		global row,col

		bt2=Button(rf,text="STORE")
		bt3=Button(rf,text="CONFIRM")
		bt2.bind("<Button-1>",self.storedatabase)
		bt2.pack()
		bt2.place(x=120,y=500)
		bt3.bind("<Button-1>",self.check)
		bt3.pack()
		bt3.place(x=300,y=500)		

		row=int(self.a.get())
		col=int(self.b.get())
		print("======================== GENERATE TRIGERRED ========================")
		print("row\tcol")
		print(row,"\t",col)
		print("")		
		if(row!=0 and col!=0): 
			canvas.create_rectangle(x1,y1,x2,y2, width=5)
			print("")
			print("===================== COORDINATES FOR GRIDS =====================")
			print("")
			a=float(400/col)
			b=float(350/row)
			p=float(x1)
			q=float(y1)
			r=float(p+a)
			s=float(q+b)
			m=float(p)
			n=float(r)
	
			for i in range(row):
				for j in range(col):
					print(p,q,r,s)
					canvas.create_rectangle(p,q,r,s)
					p+=a
					r+=a
				print("")
				p=m			
				q+=b
				r=n
				s+=b
			print("")
			canvas.bind("<Button-1>",self.get_knock)
			print("")
			print("==================== MOUSE CLICK COORDINATES ====================")
			print("GRAPH\t\t\t MATRIX \t\t VALUE")
		else:
			print("================================================================")
			print("ROWS AND COLUMNS CANT BE ZERO")
			print("================================================================")


	def storedatabase(self,event):
		print("")
		print("========================= STORE TRIGERRED ==========================")			
		one.data.stor(store)

	def checkdatabase(self,event):
		print("")			
		one.data.check(store1)
		


	def get_knock(self,eventorigin):
			global xg,yg
			xg=eventorigin.x
			yg=eventorigin.y
			if((xg>=x1 and yg>=y1)and(xg<=x2 and yg<=y2)):
				self.knock_code()

	def knock_code(self):
		global count
		a=float(400/col)
		b=float(350/row)
		p=float(x1)
		q=float(y1)
		r=float(p+a)
		s=float(q+b)
		m=float(p)
		n=float(r)
		for i in range(row):
			for j in range(col):
				if((xg>=p and yg>=q)and(xg<=r and yg<=s)):
					store.append(((i+1)*10)+(j+1))
					print(xg,",",yg,"\t\t",i+1,",",j+1,"\t\t\t",store[count])
					count+=1
					break
				p+=a
				r+=a
			if((xg>=p and yg>=q)and(xg<=r and yg<=s)):
				break
			p=m			
			q+=b
			r=n
			s+=b

	def getknock(self,eventorigin):
			global xg,yg
			x1,y1,x2,y2=(20,90,480,500)
			xg=eventorigin.x
			yg=eventorigin.y
			if((xg>=x1 and yg>=y1)and(xg<=x2 and yg<=y2)):
				self.knockcode()

	def knockcode(self):
		global row,col
		global count1
		a=float(460/col)
		b=float(410/row)
		p=float(20)
		q=float(90)
		r=float(p+a)
		s=float(q+b)
		m=float(p)
		n=float(r)
		for i in range(row):
			for j in range(col):
				if((xg>=p and yg>=q)and(xg<=r and yg<=s)):
					store1.append(((i+1)*10)+(j+1))
					print(xg,",",yg,"\t\t",i+1,",",j+1,"\t\t\t",store1[count1])
					count1+=1
					break
				p+=a
				r+=a
			if((xg>=p and yg>=q)and(xg<=r and yg<=s)):
				break
			p=m			
			q+=b
			r=n
			s+=b


	def check(self,event):
		global row,col
		rf.pack_forget()
		fr=Frame(tk,width=500,height=600)
		fr.pack()
		canvas=Canvas(fr,width=500,height=600,bg='black')
		canvas.pack()
		canvas.create_rectangle(20,90,480,500,width=5)
		print("")
		print("")
		print("======================== CHECK TRIGERRED ========================")
		print("")
		lb=Label(fr,text="ENTER THE KNOCK",bg='black',fg='white')
		lb.pack()
		lb.place(x=20,y=15)
		lb.config(font=("courier",30,"bold"))

		a=float(460/col)
		b=float(410/row)
		p=float(20)
		q=float(90)
		r=float(p+a)
		s=float(q+b)
		m=float(p)
		n=float(r)
		print("===================== COORDINATES FOR GRIDS =====================")
		print("")
		for i in range(row):
			for j in range(col):
				print(p,q,r,s)
				canvas.create_rectangle(p,q,r,s,width=2.5,outline='green')
				p+=a
				r+=a
			print("")
			p=m			
			q+=b
			r=n
			s+=b
		canvas.bind("<Button-1>",self.getknock)
		bt=Button(fr,text="CHECK",fg='white',bg='black')
		bt.bind("<Button-1>",self.checkdatabase)
		bt.pack()
		bt.config(height=2,width=10)	
		bt.place(x=192,y=530)
		b=Button(fr,text="EXIT",fg='white',bg='black')
		b.bind("<Button-1>",self.exit)
		b.pack()
		b.config(height=1,width=4)	
		b.place(x=375,y=530)	
		print("")
		print("==================== MOUSE CLICK COORDINATES ====================")
		print("GRAPH\t\t\t MATRIX \t\t VALUE")

	def alert(n):
		if(n==1):
			showinfo("ALERT","AUTHENTICATED")
		else:
			showinfo("ALERT","NOT AUTHENTICATED")

	def exit(self,event):
		print("")
		print("========================== KNOCK CODE EXITING =========================")
		sleep(0.5)
		tk.destroy()
