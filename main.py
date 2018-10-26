from GUI import GUI
from multiprocessing import Process
from Device import Device
from AccessPoint import AccessPoint
from Server import Server
import time


def guiFunc():
    gui = GUI()

    i = 0
    for machine in machine_list:
        if isinstance(machine, Device):
            gui.create_machine(machine, 10 + 190 * i, 10)
            i += 1

        if isinstance(machine, AccessPoint):
            gui.create_CAP(machine, 200, 200)

        if isinstance(machine, Server):
            gui.create_server(machine, 200, 390)

    # gui.create_CAP(200, 200)

    gui.link_to(10000, 10003)
    gui.link_to(10001, 10003)
    gui.link_to(10002, 10003)
    gui.link_to(10003, 10004)

    gui.run()


def main():
    global machine_list
    machine_list = []
    device_1 = Device(5, 20, 10000)
    device_2 = Device(7, 30, 10001)
    device_3 = Device(2, 15, 10002)
    CAP_1 = AccessPoint(10, 10, 10003)
    server_1 = Server(50, 70, 10004)
    machine_list.append(device_1)
    machine_list.append(device_2)
    machine_list.append(device_3)

    machine_list.append(CAP_1)
    machine_list.append(server_1)

    gui_process = Process(target=guiFunc())
    gui_process.start()


if __name__ == '__main__':
    main()
