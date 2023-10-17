import pandas as pd
from datetime import datetime

salaries = pd.read_csv('Salaries.csv')
#print(salaries.info())
#Task 1: Finding the number of unique jobs.
"""unique_jobs = pd.unique(salaries["JobTitle"])
unique_job_count = len(unique_jobs)

#Prints 93 unique jobs.
print(unique_job_count)"""

#Task 2: Number of Johns
"""john_count = 0
for value in salaries["EmployeeName"]:
    if "John".upper() in value:
        john_count += 1

print(john_count)"""

#Task 3: Entries with a surname > 6
"""surname_greater_than_six = 0
name = salaries["EmployeeName"]
for item in salaries["EmployeeName"]:
    if len(item.split()[-1]) > 6:
        surname_greater_than_six += 1 

print(surname_greater_than_six)"""

#Task 4: Adding last updated column

"""timestamp = datetime.now()

salaries['last_updated'] = timestamp.isoformat()"""

#Task 5: Adding time_ratio column (OverTime:BasePay)


salaries['time_ratio'] = salaries['BasePay'] / salaries['OvertimePay']

#Task 6: A new dataframe that contains employees who earn over $100k