import csv

def addLaptop(brand, model, cpu, ram, gpu, ssd, hdd, price, lists):

    laptop = {}

    laptop['brand'] = brand
    laptop['model'] = model
    laptop['cpu'] = cpu
    laptop['ram'] = ram
    laptop['gpu'] = gpu
    laptop['ssd'] = ssd
    laptop['hdd'] = hdd
    laptop['price'] = price

    lists.append(laptop)

def importLaptop(file, lists):
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
        for row in spamreader:
            comp = row[0].split(',')
            addLaptop(comp[0], comp[1], comp[2], comp[3], comp[4], comp[5], comp[6], comp[7], lists)
    
Laptops = []

importLaptop('Laptops.csv', Laptops)

print(Laptops)
#def removeLaptop(brand, model, cpu, ram, gpu, lists):