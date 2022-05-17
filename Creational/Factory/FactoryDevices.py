from abc import ABCMeta , abstractstaticmethod

class IDevice(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_hardware():
        """ InterFace """

class DeviceMac(IDevice):
    def __init__(self):
        self.cpu = "m1"
        self.memory = "8" 
        self.color = "space gray"
        self.storage = "528"

    def get_hardware(self):
        return {
            "CPU" : self.cpu,
            "Memory" : self.memory,
            "color": self.color,
            "Storage" : self.storage
        }

class DeviceImac(IDevice):
    def __init__(self):
        self.cpu = "Intel core i9"
        self.memory = "32" 
        self.color = "space gray"
        self.storage = "1TB"

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
        self.memory = "4" 
        self.color = "White"
        self.storage = "64"
        self.case = "Silicon"
        
    def get_hardware(self):
        return {
            "CPU" : self.cpu,
            "Memory" : self.memory,
            "color": self.color,
            "Storage" : self.storage,
            "case" : self.case,
        }

class DeviceFactory():
    @staticmethod
    def get_device(device_type):
        try:
            if device_type == 0:
                return DeviceMac()
            
            elif device_type == 1:
                return DeviceImac()

            elif device_type == 2:
                return DeviceIphone()

            raise AssertionError("Your requested Device not found !")
            
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    DeviceType = int(input(
        """
        Please select your desire device below :

        -0 Mac
        -1 IMac
        -2 Iphone
        """+"\n        ==> "
    ))

    Device = DeviceFactory.get_device(DeviceType)

    print(Device.get_hardware())