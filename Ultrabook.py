from Laptop import *

class Ultrabook(Laptop):

    def __init__(self, super):
        if super.gpu[0] != "d":
            self.id = super.id
            self.brand = super.brand
            self.model = super.model
            self.cpu = super.cpu
            self.ram = super.ram
            self.ssd = super.ssd
            self.hdd = super.hdd
            self.price = super.price
    
    def __repr__(self):
        str = "%s %s"