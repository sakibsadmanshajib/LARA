import csv

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
        str = "%s \nSpecification: \nModel: %s\nProcessor: %s\nMemory: %s\nGraphics: %s\nStorage: %s\nPrice: %.2f" % (modelDetail(self, importmodelDetails()), self.model, CPUDetails(self, importCPUDetails()), RAMDetails(self, importRAMDetails()), GPUDetails(self, importGPUDetails()), StorageDetails(self, importStorageDetails()), self.price)
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

def CPUDetails(self, lists):
    for items in lists:
        if items['cpu'] == self.cpu:
            return items['det']

def importCPUDetails():
    CPUDetailList = []

    with open('CPUDetails.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')

        for row in reader:
            CPUDetail = {}
            CPUDetail['cpu'] = row[0]
            CPUDetail['archi'] = row[1]
            CPUDetail['det'] = row[2]
            CPUDetail['cores'] = int(row[3])
            CPUDetail['threads'] = int(row[4])
            CPUDetail['base'] = float(row[5])
            CPUDetail['boost'] = float(row[6])
            CPUDetail['cache'] = float(row[7])
            CPUDetail['tdp'] = float(row[8])
            CPUDetail['igpu'] = row[9]
            CPUDetailList.append(CPUDetail)
        
    return CPUDetailList

    print("The CPU database has been successfully imported.")

def modelDetail(self, lists):
    for items in lists:
        if self.brand == items['brand'] and self.model == items['model']:
            return items['det']

def importmodelDetails():
    modelDetailList = []

    with open('ModelDetails.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')

        for row in reader:
            modelDetail = {}
            modelDetail['brand'] = row[0]
            modelDetail['model'] = row[1]
            modelDetail['det'] = row[2]
            modelDetailList.append(modelDetail)

    return modelDetailList
    
    print("The model database has been successfully imported.")

def addModelDetails(lists, self, det):
    modelDetail = {
        'brand' : self.brand,
        'model' : self.model,
        'det' : det
    }

    lists.append(modelDetail)

    print("The new model details has been added.")

def removeModelDetails(lists, self):
    
    for items in lists:
        if self.brand == items['brand'] and self.model == items['model']:
            lists.remove(items)

    print("The model details has been deleted.")

def editModelDetails(lists, self, det):

    for items in lists:
        if self.brand == items['brand'] and self.model == items['model']:
            items['det'] = det

    print("The model details has been edited")

def updateModelCSV(lists):

    with open('ModelDetails.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for record in lists:
            out = [record['brand'], record['model'], record['det']]
            writer.writerow(out)

    print("The model details database has been updated.")

def RAMDetails(self, lists):
    
    for item in lists:
        if item['ram'] == self.ram:
            return item['det']

def importRAMDetails():
    RAMDetailList = []

    with open('RAMDetails.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')

        for row in reader:
            RAMDetail = {}
            RAMDetail['ram'] = row[0]
            RAMDetail['size'] = row[1]
            RAMDetail['type'] = row[2]
            RAMDetail['bus'] = row[3]
            RAMDetail['det'] = row[4]
            RAMDetailList.append(RAMDetail)
        
    return RAMDetailList

    print("The RAM database has been successfully imported.")

def GPUDetails(self, lists):

    for item in lists:
        if item['gpu'] == self.gpu:
            return item['det']

def importGPUDetails():
    GPUDetailList = []

    with open('GPUDetails.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')

        for row in reader:
            GPUDetail = {}
            GPUDetail['gpu'] = row[0]
            GPUDetail['type'] = row[1]
            GPUDetail['chip'] = row[2]
            GPUDetail['bus'] = row[3]
            GPUDetail['boost'] = row[4]
            GPUDetail['vram'] = row[5]
            GPUDetail['vramtype'] = row[6]
            GPUDetail['det'] = row[7]
            GPUDetailList.append(GPUDetail)
        
    return GPUDetailList

    print("The GPU database has been successfully imported.")

def StorageDetails(self, lists):

    storage = ""

    if self.ssd != '0':
        for item in lists:
            if item['ssd'] == self.ssd:
                storage = storage + item['det']

        if self.hdd != '0':
            storage = storage + " and "
            for item in lists:
                if item['hdd'] == self.hdd:
                    storage = storage + item['det']
    
    else:
        for item in lists:
            if item['hdd'] == self.hdd:
                storage = storage + item['det']

    return storage

def importStorageDetails():
    StorageDetailList = []

    with open('StorageDetails.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')

        for row in reader:
            StorageDetail = {}
            StorageDetail['ssd'] = row[0]
            StorageDetail['hdd'] = row[1]
            StorageDetail['det'] = row[2]
            StorageDetailList.append(StorageDetail)
        
    return StorageDetailList

    print("The Storage database has been successfully imported.")