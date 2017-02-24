import json
import csv
import ijson.backends.yajl2 as ijson
import os
from os import path
import time
import gc
from ctypes import util, cdll

cwd = os.getcwd()

path = '../md_traffic.json'
#path = '../generated.json'



start_time = time.time() #Testing time
with open(path,'r') as jsonfile:
    gc.disable()
    objects = ijson.items(jsonfile, 'meta.view.columns.item')
    columns = list(objects) 
    gc.enable()
print('md_traffic = ', columns)
end_time = time.time() #Testing time
print('Time Taken in Minutes', (end_time-start_time)/60)


CSVfile = open('../Traffic.csv', 'w')
csvwriter = csv.writer(CSVfile)

count = 0
for emp in columns:
    if count == 0:
        #emp.encode('utf-8', 'replace')
        header = emp.keys()
        csvwriter.writerow(header)
        count += 1
    csvwriter.writerow(emp.values())
CSVfile.close()


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

CSVfile.close()



##Test Pruposes##
employee_data = '{"employee_details":[{"employee_name": "James", "email": "james@gmail.com", "job_profile": "Sr. Developer"},{"employee_name": "Smith", "email": "Smith@gmail.com", "job_profile": "Project Lead"}]}'
employee_parsed = json.loads(employee_data)
emp_data = employee_parsed['employee_details']
print('Emp_data = ', emp_data)
##Test Pruposes##"""