from Laptop import *

import csv

def addLaptop(brand, model, cpu, ram, gpu, ssd, hdd, price):

    return Laptop(brand, model, cpu, ram, gpu, ssd, hdd, price)

def importLaptop(file):

    LPList = []

    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')

        for row in spamreader:

            comp = row[0].split(',')
            LPList.append(Laptop(comp[0], comp[1], comp[2], comp[3], comp[4], comp[5], comp[6], float(comp[7])))

    return LPList
    
def removeLaptop(brand, model, cpu, ram, gpu, lists):
    
    for i in range(0, len(lists)):

        if lists[i].brand == brand and lists[i].model == model and lists[i].cpu == cpu and lists[i].ram == ram and lists[i].gpu == gpu:
            lists.pop(i)
            
        else:
            print("Sorry, the item you are trying to delete is not in the database.")

#def editLaptop(brand, model, cpu, ram, gpu, type, change, lists):
#    for record in lists:
#        if record['brand'] == brand and record['model'] == model and record['cpu'] == cpu and record['ram'] == ram and record['gpu'] == gpu:
#            record[type] = change
#        else:
#            print("Sorry, the item you are trying to edit is not in the database.")
