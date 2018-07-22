from Laptop import *

class Ultrabook(Laptop):

    def __init__(self, super):
        if super.gpu[0] != "d":
            self.id = super.id
            self.brand = super.brand
            self.model = super.model
            self.cpu = super.cpu
            self.ram = super.ram
            self.gpu = super.gpu
            self.ssd = super.ssd
            self.hdd = super.hdd
            self.price = super.price
    
    def __repr__(self):
        str = "\n%s \nSpecification: \nModel: %s\nProcessor: %s\nMemory: %s\nGraphics: %s\nStorage: %s\nPrice: %.2f" % (modelDetail(self, importmodelDetails()), self.model, CPUDetails(self, importCPUDetails()), self.ram, self.gpu, self.ssd, self.price)
        return str