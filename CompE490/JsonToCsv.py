import json
import csv


employee_data = '{"employee_details":[{"employee_name": "James", "email": "james@gmail.com", "job_profile": "Sr. Developer"},{"employee_name": "Smith", "email": "Smith@gmail.com", "job_profile": "Project Lead"}]}'


X = json.loads(employee_data) # This loads the json file into a variable X
CSVfile = open('./EmployData.csv', 'w') # This opens a new CSV file with write permissions




emp_data = X['employee_details']


csvwriter = csv.writer(CSVfile)

count = 0
for emp in emp_data:
    if count == 0:
        header = emp.keys()
        csvwriter.writerow(header)
        count += 1
    csvwriter.writerow(emp.values())

CSVfile.close()