import json
import os, sys

class Entity:
    def __init__(self, location, customer):
        self.location = location
        self.customer = customer

f = open(os.path.join(sys.path[0], './test.json'), "r")
data = json.load(f)

customers = []
trucks = []

for i in data['entities']:
    if i['customer']:
        customers.append(Entity(i['location'],i['customer']))
    else:
        trucks.append(Entity(i['location'],i['customer']))

# debugging
for c in customers:
    print(f"{customers.index(c)}: {c.location}, {c.customer} {c}")

for t in trucks:
    print(f"{trucks.index(t)}: {t.location}, {t.customer} {t}")