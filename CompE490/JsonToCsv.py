import json
import csv
import ijson
from traitlets.config.loader import JSONFileConfigLoader
import os
from os import path

cwd = os.getcwd()
print(cwd)

#path = '..\\test_data.json'
path = '..\\md_traffic.json'



#edit

with open(path,'r') as jsonfile:
    objects = ijson.items(jsonfile, 'meta.view.columns.item')
    #objects = ijson.items(jsonfile, 'node1.lists.item')
    print(objects)
    columns = list(objects)
    
print(columns)

CSVfile = open('/EmployData.csv', 'w')
csvwriter = csv.writer(CSVfile)
print(csvwriter)

count = 0
for emp in columns:
    if count == 0:
        header = emp.keys()
        csvwriter.writerow(header)
        count += 1
    csvwriter.writerow(emp.values())




"""for key in X.keys():
    firstProp = key #Gets the Key value inside employee data
    
for item in ijson.items(f, 'meta.view.columns.item'):
        print(item)
        break
    
emp_data = X[key] #Prints the data associated with the key
csvwriter = csv.writer(CSVfile)
print(csvwriter)

count = 0
for emp in emp_data:
    if count == 0:
        header = emp.keys()
        csvwriter.writerow(header)
        count += 1
    csvwriter.writerow(emp.values())

CSVfile.close()"""