import tkinter


class GUI:

    def __init__(self):
        global root
        global canvas
        root = tkinter.Tk()
        canvas = tkinter.Canvas(root, width=500, height=500)
        canvas.pack()

    def create_machine(self, x, y):
        edge = 90
        canvas.create_rectangle(x, y, x + edge, y + edge, fill='black')


    def run(self):
        root.mainloop()
