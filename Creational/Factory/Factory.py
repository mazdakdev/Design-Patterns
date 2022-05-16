from abc import ABCMeta , abstractstaticmethod

class IDevice(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_hardware():
        """ InterFace """

class DeviceMac(IDevice):
    def __init__(self):
        self.cpu = "M1"
        self.memory = 16
        self.color = "Space-Gray"
        self.storage = 512

    def get_hardware(self):
        return {
            "CPU" : self.cpu,
            "Memory" : self.memory,
            "color": self.color,
            "Storage" : self.storage
        }

class DeviceIphone(IDevice):
    def __init__(self):
        self.cpu = "A13"
        self.memory = 4
        self.color = "White"
        self.storage = 128

    def get_hardware(self):
        return {
            "CPU" : self.cpu,
            "Memory" : self.memory,
            "color": self.color,
            "Storage" : self.storage
        }

class DeviceFactory():
    @staticmethod
    def get_device(device_type):
        try:
            if device_type == 0:
                return DeviceMac()
            
            elif device_type == 1:
                return DeviceIphone()
            raise AssertionError("Your requested Device not found !")
            
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    DeviceType = int(input(
        """
        Please select your desire device below :

        -0 Mac
        -1 Iphone
        """+"\n        ==> "
    ))

    Device = DeviceFactory.get_device(DeviceType)

    print(Device.get_hardware())