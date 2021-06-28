import json
import os, sys

class Entity:
    def __init__(self, location, customer):
        self.location = location
        self.customer = customer

f = open(os.path.join(sys.path[0], './test.json'), "r")
data = json.load(f)

i_cust = 0
i_truck = 0
customers = []
trucks = []
for i in data['entities']:
    if i['customer']:
        i_cust += 1
        customers.append(Entity(i['location'],i['customer']))
    else:
        i_truck += 1
        trucks.append(Entity(i['location'],i['customer']))
print(customers[0].location)