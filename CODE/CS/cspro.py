from tkinter import *

root = Tk()

#function for the button
def data():
    net = e.get
    f = "your netwroth is :" + e.get()
    lable4 = Label(root, text=f)
    lable4.pack()
# create a label
label1 = Label(root, text="L COMPUTER SCIENCE PROJECT")
label2 = Label(root, text="CASH FLOW MASTER")
label3 = Label(root, text="give me your networth!!")
    
#position that label
label1.pack()
label2.pack()
label3.pack()
#for input
e = Entry(root, width=30)
e.pack()
button1 = Button(root, text="click here", command=data, padx=10, pady=10, fg="yellow" ,bg="blue")    
button1.pack()
# put it on the screen 
#label1.pack()



root.mainloop() 