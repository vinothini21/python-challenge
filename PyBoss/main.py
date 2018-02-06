import os
import csv

# data sets
boss= ['1', '2']


#loop thru different data sets
for employee in boss:
    
    # Grab the electiondata csv
    paragraphtxt = os.path.join('employee_' + 'data_' + boss + '.csv')