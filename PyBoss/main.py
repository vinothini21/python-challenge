import os
import csv

# data sets
boss= ['1', '2']


#loop thru different data sets
for employee in boss:
    
    # Grab the electiondata csv
    employeecsv = os.path.join('employee_' + 'data_' + boss + '.csv')

    with open(employeecsv,'r') as e:

        for emp in e: