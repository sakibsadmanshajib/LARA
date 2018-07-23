from UpdateList import *
from Password import *
from Ultrabook import Ultrabook
from GamingLaptop import GamingLaptop
from Laptop import *
import getpass

laptop = importLaptop()

ultrabook = []
for record in laptop:
    if record.gpu[0] == 'i':
        ultrabook.append(Ultrabook(record))

gaming = []
for record in laptop:
    if record.gpu[0] == 'd':
        gaming.append(GamingLaptop(record))


hashed_pass = "dec0cd2d7d4eed7e27afc99b61e2d148f5aa8d578d8eba637f65612272cbd1d16992d852b8b7ceb0d7f500df75f4e670ffb58a65a6200021d51bc1fd4bcd4ec2:5161ae90a3354f9ba86f615c461b8b0d"

choice = int(input("Hey there! Thank you for Alpha testing my program. I have already imported the Laptops from the CSV database. Report any bugs to mail@sakibsadmanshajib.com.\nWhat are you planning to do in this program? (Input the index only) \n1. Make changes to the database. \n2. Get recommendation. \nYour choice: "))

if choice == 1:

    password = getpass.getpass("Say the magic word: ")

    if check_password(hashed_pass, password):
        sub_choice = int(input("What do you want to do? (Input the Index only) \n1. Add Laptop \n2. Import Laptop from CSV (again) \n3. Remove Laptop \n4. Edit Laptop \n5. Update Laptop CSV File \nYour Choice: "))
        if sub_choice == 1:
            addLaptop(laptop)
        elif sub_choice == 2:
            laptop = importLaptop()
        elif sub_choice == 3:
            id = int(input("Look into the CSV database and find the ID of the laptop you want to delete. \nNow, input the ID here: "))
            removeLaptop(id, laptop)
        elif sub_choice == 4:
            id = int(input("Look into the CSV database and find the ID of the laptop you want to edit. \nNow, input the ID here: "))
            editLaptop(id, laptop)
        elif sub_choice == 5:
            confirmation = input("You're trying to rewrite the database. Are you sure what you're doing? (Y/N) ")
            if confirmation == 'Y':
                password = input("Say the magic word: ")
                if check_password(hashed_pass, password):
                    updateCSV(laptop)
                else:
                    print("Unauthorized request. Denied!")
            else:
                print("Thank you.")

    else:
        print("Wrong Password.")

elif choice == 2:

    budget = input("What is your budget? ")
    lower_budget = int(budget) - 4999
    upper_budget = int(budget) + 5001

    preference = int(input("What are planning to buy? (Input the index only)\n1. Ultrabook/Netbook (Great for office/normal use, such as Word processing, web-browsing, photoshop, light-workload, optional thin&light etc.)\n2. Gaming/Workstation (Great for Gaming, heavy-workload, video-editing, 3D rendering, CPU/GPU intensive task.\n3. Anyone would work just fine.\nYour choice: "))

    if preference == 1:
        query_list = ultrabook
    elif preference == 2:
        query_list = gaming
    elif preference == 3:
        query_list = laptop

    print("Your querry results are:")

    for record in query_list:
        if record.price in range(lower_budget, upper_budget):
            print(record)