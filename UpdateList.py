from Laptop import *

import csv

def addLaptop(lists):

    print("See the instruction manual before proceeding to use this function. You can find the instruction manual in the root directory of this program.")

    ID = len(lists)
    brand = input("What is the brand of the Laptop? ")
    model = input("What is the model number? ")
    cpu = input("What is the CPU model? ")
    ram = input("What is the Memory Configuration? ")
    gpu = input("What is the GPU Configuration? ")
    ssd = input("What is the SSD Configuration? ")
    hdd = input("What is the HDD Configuration? ")
    price = input("What is the price? ")

    lists.append(Laptop(int(ID), brand, model, cpu, ram, gpu, ssd, hdd, float(price)))

    print("The Laptop has been added.")

def importLaptop():

    LPList = []

    with open('Laptops.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')

        for row in reader:

            LPList.append(Laptop(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], float(row[8])))

    return LPList

    print("The database has been imported.")
    
def removeLaptop(ID, lists):
    
    for record in lists:

        if record.ID == ID:
            lists.remove(record)

    print("The Laptop has been removed.")

def editLaptop(ID, lists):

    print("See the instruction manual before proceeding to use this function. You can find the instruction manual in the root directory of this program.")

    for record in lists:

        if record.ID == ID:
            
            type = int(input("What are you trying to input? (Input the index) \n1. CPU \n2. RAM \n3. GPU \n4. SSD \n5. HDD \n6. Price \nYour choice: "))

            if type == 1:
                change = input("What is the updated CPU model? ")
                record.changeCPU(int(change))

            elif type == 2:
                change = input("What is the updated Memory Configuration? ")
                record.changeRAM(change)

            elif type == 3:
                change = input("What is the updated GPU Configuration? ")
                record.changeGPU(change)

            elif type == 4:
                change = input("What is the updated SSD Configuration? ")
                record.changeSSD(change)

            elif type == 5:
                change = input("What is the updated HDD Configuration? ")
                record.changeHDD(change)

            elif type == 6:
                change = input("What is the updated price? ")
                record.chanegPrice(float(change))

            else:
                print("Wrong input.")

    print("The laptop has been edited.")

def updateCSV(lists):
    with open('Laptops.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for record in lists:
            out = [record.ID, record.brand, record.model, record.cpu, record.ram, record.gpu, record.ssd, record.hdd, record.price]
            writer.writerow(out)

    print("The database has been updated.")