def addLaptop(brand, model, cpu, ram, gpu, ssd, hdd, price, lists):

    laptop = {}

    laptop['Brand'] = brand
    laptop['Model'] = model
    laptop['Processor'] = cpu
    laptop['Memory'] = ram
    laptop['Graphics'] = gpu
    laptop['SSD'] = ssd
    laptop['HDD'] = hdd
    laptop['Price'] = price

    lists.append(laptop)

Laptoplist = []

addLaptop("ASUS", "S510UQ", "Core i5 8250U", "8GB DDR4", "NVIDIA GeForce MX150", "128GB NVMe", "1TB 5200", 64000, Laptoplist)

print(Laptoplist)