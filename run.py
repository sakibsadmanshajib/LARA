from updateList import *

Laptops = []

importLaptop('Laptops.csv', Laptops)

print(Laptops)

removeLaptop('ASUS', 'N580VD', '7700HQ', '16G4', 'GTX1050', Laptops)

print(Laptops)