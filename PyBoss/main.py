import os
import csv
import datetime
# data sets
boss = ['1', '2']

state_abb = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


#loop thru different data sets
for employee in boss:
    
    # Grab the electiondata csv
    employeecsv = os.path.join('employee_data_' + employee + '.csv')

    #Create New csv
    newemployeeCSV = os.path.join('employee_data_output_' + employee + '.csv')

    # Set empty list variables
    Emp_id = []
    Name = []
    DOB = []
    SSN = []
    State = []
    First_Name = []
    Last_Name = []

    with open(employeecsv, 'r') as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')

        # Skipp headers
        next(csvReader, None)

        for row in csvReader:

            # Append data from the row
            Emp_id.append(row[0])

            First_Name.append(str(row[1]).split()[0])
            
            Last_Name.append(str(row[1]).split()[1])
            
            DOB.append(datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y'))
            
            SSN.append('***-**-'+(row[3].split('-')[2]))
           
            State.append(state_abb[row[4]])
            
            
        
        # #Zip lists together
        modifiedcsv = zip(Emp_id, First_Name, Last_Name, DOB, SSN, State)
    with open(newemployeeCSV, 'w') as csvFile:

        csvWriter = csv.writer(csvFile, delimiter= ',')

            # Write Headers into file
        csvWriter.writerow(["Emp_ID", "First_Name", "Last_Name","DOB", "SSN", "State"])
            # Write the zipped lists to a csv
        csvWriter.writerows(modifiedcsv)

