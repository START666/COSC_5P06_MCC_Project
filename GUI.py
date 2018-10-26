import tkinter


class GUI:
    global root
    global canvas
    global machine_list

    def __init__(self):
        self.machine_list = []
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=500, height=500)
        self.canvas.pack()

    def create_machine(self, device, x, y):
        edge = 90
        self.canvas.create_rectangle(x, y, x + edge, y + edge, fill='black')
        self.machine_list.append([device, x, y])

    def create_CAP(self, CAP, x, y):
        edge = 90
        self.canvas.create_rectangle(x, y, x + edge, y + edge, fill='purple')
        self.machine_list.append([CAP, x, y])

    def create_server(self, server, x, y):
        size = 90
        self.canvas.create_oval(x, y, x + size, y + size, fill="yellow")
        self.machine_list.append([server, x, y])

    def link_to(self, address_1, address_2):
        machine_1 = [0, 0, 0]
        machine_2 = [0, 0, 0]
        for machine in self.machine_list:
            if address_1 == machine[0].address:
                machine_1 = machine
            if address_2 == machine[0].address:
                machine_2 = machine

        location_1 = self.get_center([machine_1[1], machine_1[2]], 90)
        location_2 = self.get_center([machine_2[1], machine_2[2]], 90)
        self.canvas.create_line(location_1[0], location_1[1], location_2[0], location_2[1], fill='red')

    def run(self):
        self.root.mainloop()

    def get_center(self, location, size):
        x = location[0] + size / 2
        y = location[1] + size / 2
        return [x, y]
