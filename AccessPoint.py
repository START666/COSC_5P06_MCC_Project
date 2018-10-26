class AccessPoint:
    global computation_power
    global memory_size
    global address
    global link_list

    def __init__(self, computation_power, memory_size, address):
        self.computation_power = computation_power
        self.memory_size = memory_size
        self.address = address
        self.link_list = []


