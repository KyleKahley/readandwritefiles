# import pandas to the file
import pandas as pd
# open customers file using pandas as a dataframe so it sees each element as a column
df = pd.read_csv("customers.csv")

# separate elements into variables
firstNames = df["FirstName"]
lastNames = df["LastName"]
countries = df["Country"]
# create dictionaries with names and country
data = {'Name': [], 'Country': []}
# for each person append names and country to dictionary
for i in range(0, len(firstNames)):
    data['Name'].append(firstNames[i] + ' ' + lastNames[i])
    data['Country'].append(countries[i])
# move data to new file from the dictionary
new_df = df.from_dict(data)
new_df.to_csv('customer_country.csv', index=False)
