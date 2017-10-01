from tkinter import*
import tkinter.messagebox


left1 = Tk()
left1.geometry("1600x800+0+0")
left1.title("Change Price")

label4 = Label(left1, font = ('arial',50,'bold'), text ="Change Price", fg = "steel blue", bd = 10, anchor = 'w')
label4.grid(row = 0)


fries_inp_p = StringVar()
samosa_inp_p = StringVar()
burger_inp_p = StringVar()
drinks_inp_p = StringVar()
paneer_tikka_inp_p = StringVar()
chicken_tikka_inp_p = StringVar()

def update():
	f = open('value.txt','r')
	line = f.readlines()
	fries_p = float(line[0])
	samosa_p = float(line[1])
	burger_p = float(line[2])
	drinks_p = float(line[3])
	paneer_tikka_p = float(line[4])
	chicken_tikka_p = float(line[5])
	f.close()
	
	f2 = open('value.txt','w')
	try:
		CoF1 = float(fries_inp_p.get())
	except Exception as e:
		if fries_inp_p.get() != "":
			tkinter.messagebox.showinfo('Error','Incorrect Input')
		fries_inp_p.set("")
		f2.write(str(fries_p)+"\n")
	else:
		f2.write(str(CoF1)+"\n")	
			
	try:
		CoS1 = float(samosa_inp_p.get())
	except Exception as e:
		if samosa_inp_p.get() != "":
			tkinter.messagebox.showinfo('Error','Incorrect Input')
		samosa_inp_p.set("")
		f2.write(str(samosa_p)+"\n")
	else:
		f2.write(str(CoS1)+"\n")

	try:
		CoB1 = float(burger_inp_p.get())
	except Exception as e:
		if burger_inp_p.get() != "":
			tkinter.messagebox.showinfo('Error','Incorrect Input')
		burger_inp_p.set("")
		f2.write(str(burger_p)+"\n")
	else:
		f2.write(str(CoB1)+"\n")

	try:
		CoD1 = float(drinks_inp_p.get())
	except Exception as e:
		if drinks_inp_p.get() != "":
			tkinter.messagebox.showinfo('Error','Incorrect Input')
		drinks_inp_p.set("")
		f2.write(str(drinks_p)+"\n")
	else:
		f2.write(str(CoD1)+"\n")

	try:
		CoP1 = float(paneer_tikka_inp_p.get())
	except Exception as e:
		if paneer_tikka_inp_p.get() != "":
			tkinter.messagebox.showinfo('Error','Incorrect Input')
		paneer_tikka_inp_p.set("")
		f2.write(str(paneer_tikka_p)+"\n")
	else:
		f2.write(str(CoP1)+"\n")

	try:
		CoC1 = float(chicken_tikka_inp_p.get())
	except Exception as e:
		if chicken_tikka_inp_p.get() != "":	
			tkinter.messagebox.showinfo('Error','Incorrect Input')
		chicken_tikka_inp_p.set("")
		f2.write(str(chicken_tikka_p))
	else:
		f2.write(str(CoC1))
	
	#f.write(str(samosa_p) +"\n"+ str(paneer_tikka_p) +"\n"+ str(chicken_tikka_p) +"\n"+ str(fries_p) +"\n"+ str(burger_p) +"\n"+ str(drinks_p))
	
	tkinter.messagebox.showinfo('Update Box','Successfully Updated')
	f2.close()	

def reset1():
	fries_inp_p.set("")
	samosa_inp_p.set("")
	burger_inp_p.set("")
	drinks_inp_p.set("")
	paneer_tikka_inp_p.set("")
	chicken_tikka_inp_p.set("")

def qexit1():
	left1.destroy()

def printfn():
	f3 = open('value.txt','r')
	liness = f3.readlines()
	fries_p = float(liness[0])
	samosa_p = float(liness[1])
	burger_p = float(liness[2])
	drinks_p = float(liness[3])
	paneer_tikka_p = float(liness[4])
	chicken_tikka_p = float(liness[5])
	print("fry "+str(fries_p))
	print("samosa "+str(samosa_p))
	print("chi tikka "+str(chicken_tikka_p))
	print("paneer tikka "+str(paneer_tikka_p))
	print("burger "+str(burger_p))
	print("drinks "+str(drinks_p))
	f3.close()

def backfn():
	left1.destroy()
	import question


fries = Label(left1, font=('arial',16,'bold'),text = "Fries", bd = 16, anchor = 'w' )
fries.grid(row=1,column=0,sticky = E)
txt_fries = Entry(left1,font=('arial',16,'bold'), textvariable=fries_inp_p, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_fries.grid(row=1,column=1)

samosa = Label(left1, font=('arial',16,'bold'),text = "Samosa", bd = 16, anchor = 'w' )
samosa.grid(row=2,column=0,sticky = E)
txt_samosa = Entry(left1,font=('arial',16,'bold'), textvariable=samosa_inp_p, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_samosa.grid(row=2,column=1)


burger = Label(left1, font=('arial',16,'bold'),text = "Burger", bd = 16, anchor = 'w' )
burger.grid(row=3,column=0,sticky = E)
txt_burger = Entry(left1,font=('arial',16,'bold'), textvariable=burger_inp_p, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_burger.grid(row=3,column=1)

drinks = Label(left1, font=('arial',16,'bold'),text = "Drinks", bd = 16, anchor = 'w' )
drinks.grid(row=4,column=0,sticky = E)
txt_drinks = Entry(left1,font=('arial',16,'bold'), textvariable=drinks_inp_p, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_drinks.grid(row=4,column=1)

paneer_tikka = Label(left1, font=('arial',16,'bold'),text = "Paneer Tikka", bd = 16, anchor = 'w' )
paneer_tikka.grid(row=5,column=0,sticky = E)
txt_paneer_tikka = Entry(left1,font=('arial',16,'bold'), textvariable=paneer_tikka_inp_p, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_paneer_tikka.grid(row=5,column=1)

chicken_tikka = Label(left1, font=('arial',16,'bold'),text = "Chicken Tikka", bd = 16, anchor = 'w' )
chicken_tikka.grid(row=6,column=0,sticky = E)
txt_chicken_tikka = Entry(left1,font=('arial',16,'bold'), textvariable=chicken_tikka_inp_p, bd=10, insertwidth =4,bg = "powder blue", justify ='right')
txt_chicken_tikka.grid(row=6,column=1)


btn_update = Button(left1, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Update", bg= "powder blue",command = update)
btn_update.grid(row=7, column= 1)

btn_reset1 = Button(left1, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Reset", bg= "powder blue",command = reset1)
btn_reset1.grid(row=7, column= 2)

btn_exit1 = Button(left1, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Exit", bg= "powder blue",command = qexit1)
btn_exit1.grid(row=7, column= 3)

btn_print = Button(left1, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "print", bg= "powder blue",command = printfn)
btn_print.grid(row=7, column= 4)

btn_back = Button(left1, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Back", bg= "powder blue",command = backfn)
btn_back.grid(row=8, column= 3)



left1.mainloop()





