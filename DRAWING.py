from tkinter import *

class Machine1:
    def __init__(self, master, can):
        machine1 = can.create_rectangle(10, 10, 100, 100, fill="black")

class Machine2:
    def __init__(self, master, canvas):
        machine2 = canvas.create_rectangle(200, 10, 290, 100, fill="black")

class Machine3:
    def __init__(self, master, can):
        machine3 = canvas.create_rectangle(390, 10, 480, 100, fill="black")


root = Tk()

canvas = Canvas(root, width=500, height=500)
canvas.pack()


Cap = canvas.create_rectangle(200, 200, 290, 290, fill="purple")

Cloud = canvas.create_oval(200, 390, 290, 480, fill="yellow")

link1 = canvas.create_line(100, 100, 200, 200, fill="red")
link2 = canvas.create_line(245, 100, 245, 200, fill="red")
link3 = canvas.create_line(390, 100, 290, 200, fill="red")

link4 = canvas.create_line(245, 290, 245, 390, fill="red")


m1 = Machine1(root, canvas)
m2 = Machine2(root, canvas)
m3 = Machine3(root, canvas)

status = Label(root, text="Preparing to connect....", bd=1, relief=SUNKEN, anchor=W)   #West anchoring
status.pack(side=BOTTOM, fill=X)


root.mainloop()