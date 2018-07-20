class Laptop(object):

    def __init__(self, brand, model, cpu, ram, gpu, ssd, hdd, price):
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
    
        
    def removeLaptop(self, brand, model, cpu, ram, gpu):

        if self.brand == brand and self.model == model and self.cpu == cpu and self.ram == ram and self.gpu == gpu:
            del self
                
        else:
            print("Sorry, the item you are trying to delete is not in the database.")

    def editLaptop(self, brand, model, cpu, ram, gpu, type, change):

        if self.brand == brand and self.model == model and self.cpu == cpu and self.ram == ram and self.gpu == gpu:
            self.type = change
                
        else:
            print("Sorry, the item you are trying to edit is not in the database.")
