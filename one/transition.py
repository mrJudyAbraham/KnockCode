from tkinter import*
from time import sleep
#root=Tk()
#root.title("TRANSITON")
#root.resizable(0,0)
def transition(object):
	root=object
	fr=Frame(root,width=500,height=600)
	fr.pack()
	canvas=Canvas(fr,width=500,height=600,bg='black')
	canvas.pack()
	 
	img=PhotoImage(file="one/logos/handwhiteblack.png")
	canvas.create_image(250,300,image=img)
	
	x1,y1,x2,y2=(50,100,450,500)
	j=0
	t=0
	for i in range(3):
		x1,y1,x2,y2=(150,200,350,400)
		a,b,c,d=(150,200,350,400)
		k=3
		j=0
		t=0
		while ((j<5)==True)or((t<5)==True)!=False:
			if(j<5):
				canvas.create_oval(x1,y1,x2,y2,width=k,outline='white')
				x1-=25
				y1-=25
				x2+=25
				y2+=25
				k+=2
				root.update()
			if(j>1):
				canvas.create_oval(a,b,c,d,width=k,outline='black')
				a-=25
				b-=25
				c+=25
				d+=25
				k+=2
				t+=1
				root.update()
			sleep(0.25)
			j+=1
			root.update()
	fr.pack_forget()	
	root.update()
#mainloop()
