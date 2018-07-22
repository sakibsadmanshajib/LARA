from UpdateList import *
from Laptop import *
from Ultrabook import Ultrabook
from GamingLaptop import GamingLaptop

laptop = importLaptop()
ultrabook = []
for record in laptop:
    if record.gpu[0] == 'i':
        ultrabook.append(Ultrabook(record))

query_list = ultrabook

print(query_list)

gaming = []
for record in laptop:
    if record.gpu[0] == 'd':
        gaming.append(GamingLaptop(record))

query_list = gaming

print(query_list)