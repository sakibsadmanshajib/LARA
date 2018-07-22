from Laptop import *

class Ultrabook(Laptop):

    def __init__(self, super):
            self.ID = super.ID
            self.brand = super.brand
            self.model = super.model
            self.cpu = super.cpu
            self.ram = super.ram
            self.gpu = super.gpu
            self.ssd = super.ssd
            self.hdd = super.hdd
            self.price = super.price
