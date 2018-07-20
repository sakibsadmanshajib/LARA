from Laptop import *

import csv

def addLaptop(lists):

    print("See the instruction manual before proceeding to use this function. You can find the instruction manual in the root directory of this program.")

    id = len(lists)
    brand = input("What is the brand of the Laptop? ")
    model = input("What is the model number? ")
    cpu = input("What is the CPU model? ")
    ram = input("What is the Memory Configuration? ")
    gpu = input("What is the GPU Configuration? ")
    ssd = input("What is the SSD Configuration? ")
    hdd = input("What is the HDD Configuration? ")
    price = input("What is the price? ")

    lists.append(Laptop(id, brand, model, cpu, ram, gpu, ssd, hdd, int(price)))

def importLaptop(file):

    LPList = []

    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')

        for row in spamreader:

            comp = row[0].split(',')
            LPList.append(Laptop(comp[0], comp[1], comp[2], comp[3], comp[4], comp[5], comp[6], comp[7], int(comp[8])))

    return LPList
    
def removeLaptop(id, lists):
    
    for record in lists:

        if record.id == id:
            lists.remove(record)
            
        else:
            print("Sorry, the item you are trying to delete is not in the database.")

def editLaptop(id, lists):

    print("See the instruction manual before proceeding to use this function. You can find the instruction manual in the root directory of this program.")

    for record in lists:

        if record.id == id:
            
            type = input("What are you trying to input? (Input the index) \n1. CPU \n2. RAM \n3. GPU \n4. SSD \n5. HDD \n6. Price \nYour choice: ")

            if type == 1:
                change = input("What is the updated CPU model? ")
                record.changeCPU(change)

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
                record.chanegPrice(int(change))

            else:
                print("Wrong input.")

        else:
            print("Sorry, the item you are trying to edit is not in the database.")

def updateCSV(lists, file):
    with open(file, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for record in lists:
            out = record.id + "," + record.brand + "," + record.model + "," + record.cpu + "," + record.ram + "," + record.gpu + "," + record.ssd + "," + record.hdd + "," + str(record.price)
            spamwriter.writerow(out)