from tkinter import*

newroot = Tk()
newroot.geometry("720x720+0+0")
newroot.title("Menu")


def enter1():
	newroot.destroy()
	import restaurant_management_system


def enter2():
	newroot.destroy()
	import price	


label11 = Label(newroot, text="Bill")
label11.grid(row=1, sticky=E)

press_btn = Button(newroot, text="Press Here", command= enter1)
press_btn.grid(row=1, column=1)

label21 = Label(newroot, text="Change Price")        
label21.grid(row=2,sticky=E)

press1_btn = Button(newroot, text="Press Here", command= enter2)
press1_btn.grid(row=2, column=1)

newroot.mainloop()
