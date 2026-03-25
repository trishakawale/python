import pandas as pd

# Load file
df = pd.read_excel("employee.xlsx")

# a) Employees in Automotive domain
print("\nAutomotive Employees:")
print(df[df['Department'] == 'Automotive'])

# b) Employee details by ID
emp_id = int(input("Enter Employee ID: "))
print(df[df['Employee ID'] == emp_id])

# c) List of Developers
print("\nDevelopers List:")
print(df[df['Designation'] == 'Developer'])
