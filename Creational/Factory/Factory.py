from abc import ABCMeta , abstractstaticmethod

class IDevice(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_hardware():
        """ InterFace """


class DeviceMac(Ichair):
    def __init__(self):
        self.cpu = "M1"
        self.memory = 16
        self.color = "Black"
        self.storage = 512

    def get_hardware(self):
        return {
            "CPU" : self.cpu,
            "Memory" : self.memory,
            "color": self.color,
            "Storage" : self.storage
        }



