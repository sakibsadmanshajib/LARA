class Laptop(object):

    def __init__(self, id, brand, model, cpu, ram, gpu, ssd, hdd, price):
        self.id = id
        self.brand = brand
        self.model = model
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.ssd = ssd
        self.hdd = hdd
        self.price = price
    
    def __repr__(self):
        str = self.brand + self.model
        return str

    def changeCPU(self, cpu):
        self.cpu = cpu
    
    def changeRAM(self, ram):
        self.ram = ram

    def changeGPU(self, gpu):
        self.gpu = gpu

    def changeSSD(self, ssd):
        self.ssd = ssd

    def changeHDD(self, hdd):
        self.hdd = hdd

    def changePrice(self, price):
        self.price = price
