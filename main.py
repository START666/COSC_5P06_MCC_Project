from GUI import GUI
from multiprocessing import Process


def guiFunc():
    gui = GUI()
    gui.create_machine(10, 10)
    gui.create_machine(200, 10)
    gui.create_machine(390, 10)
    gui.run()


def main():
    gui_process = Process(target=guiFunc())
    gui_process.start()


if __name__ == '__main__':
    main()
