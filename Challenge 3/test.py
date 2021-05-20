import os
from az.cli import az
import json
from python_terraform import *
import time
from tqdm import tqdm
import json
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.basicConfig(filename='example1.log',level=logging.INFO)
logging.basicConfig(filename='example2.log',level=logging.WARNING)
logging.basicConfig(filename='example3.log',level=logging.CRITICAL)

 


rg = az("group list")[1]
length = len(rg)
j=0
save_data = []
while j < length :
        rg1 = az("group list")[1][j]['name']
        j += 1
        save_data.append(str(j) + '] ' + rg1)
data = json.dumps(save_data, indent=4)
print(data)
choice = input("\n Enter the name of the resource group from the above list: ")
key = input("\n Enter the key of the resource: ")
value = input("\n Enter the value of the resource:")
save_data = []
conv = []
vm = az("resource list --resource-type Microsoft.Compute/virtualMachines")[1]
leng = len(vm)
k=0
while k < leng :
        vm1 = az("resource list --resource-type Microsoft.Compute/virtualMachines")[1][k]
        try:
            kv  = az("resource list --resource-type Microsoft.Compute/virtualMachines")[1][k]['tags'][key]
        except (TypeError,KeyError):
            k += 1
            continue
        fire = vm1['resourceGroup']
        sire = vm1['id']
        tire = kv
        save_data.append(fire)
        save_data.append(sire)
        save_data.append(tire)
        k += 1
m = 0
n = 1
data = ''
for m in range(len(save_data)):
    if choice == save_data[m] and value == save_data[m+2]:
            conv.append('%d] %s' %(n,save_data[m+1]))
            m += 3
            n += 1
print(conv)