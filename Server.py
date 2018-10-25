class Server:
    global computation_power
    global memory_size
    global address

    def __init__(self, computation_power, memory_size, address):
        self.computation_power = computation_power
        self.memory_size = memory_size
        self.address = address
