import os
import csv

us_state_abbrev = {
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

new_order = [1, 2, 0]
hidden_social = "***-**-"
new_social = ""

csvpath = os.path.join('resource', 'employee_data1.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvreader = list(csvreader)

    for row in range(1, len(csvreader)):
        # Separated into First name & Last name
        name = csvreader[row][1].split()
        csvreader[row][1] = name[0]
        csvreader[row].insert(2, name[1])

        # DOB re-written into DD/MM/YYYY
        date = csvreader[row][3].split("-")
        new_date = [date[i] for i in new_order]
        new_date = "/".join(new_date)
        csvreader[row][3] = new_date

        # Hidden SSN
        old_social = csvreader[row][4].split("-")
        new_social = hidden_social + old_social[2]
        csvreader[row][4] = new_social

        # State abbreviations
        csvreader[row][5] = us_state_abbrev[csvreader[row][5]] 
    
        print(csvreader[row])
      
