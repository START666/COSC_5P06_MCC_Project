import random
from queue import Queue
from Task import Task
from DataLink import DataLink


class Device:
    global computation_power
    global memory_size
    global max_memory_size
    global task_queue
    global address
    global link_list

    def __init__(self, computation_power, max_memory_size, address):
        self.computation_power = computation_power
        self.max_memory_size = max_memory_size
        self.address = address
        self.memory_size = max_memory_size
        self.task_queue = Queue(0)
        self.link_list = []

    def link_to(self, access_point):
        latency = random.randint(1, 10)
        data_link = DataLink(latency, self.address, access_point.address)
        self.link_list.append(data_link)
        access_point.link_list.append(data_link)

    def generate_task(self):
        task_size = random.randint(1, 50)
        if self.memory_size > task_size:
            task = Task(task_size, self.address)
            self.task_queue.put(task)
            self.memory_size -= task_size

    def get_next_task(self):
        if not self.task_queue.empty():
            task = self.task_queue.get()

            self.memory_size += task.size

            return task
        else:
            return None
