class Device:
    def __init__(self):
        cpu = self.cpu 
        memory = self.memory 
        color = self.color
        storage = self.storage

    def get_hardware(self):
        return {
            "CPU" : self.cpu,
            "Memory" : self.memory,
            "color": self.color,
            "Storage" : self.storage
        }

mac = Device(cpu="M1" , memory="8" , color="spacegray" , storage="528")
imac = Device(cpu="Intel core i9" , memory="32" , color="gray" , storage="1TB")


"""
Now we wanna create iphone object from same class but iphone needs an extra case , 
so we need to edit the constructors of class in __init__ function
"""