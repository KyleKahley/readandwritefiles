# import pandas to file
import pandas as pd
# reading sales csv
df = pd.read_csv("sales.csv")
# create variable for each element of sales file into dataframd
customerIDs = df["CustomerID"]
subtotal = df["SubTotal"]
tax = df["TaxAmt"]
freight = df['Freight']

# creating empty dictionary as data
data = {}
# for each customer in the range  add subtotal, tax and freight together
for i in range(0, len(customerIDs)):
    total = subtotal[i] + tax[i] + freight[i]
    # if the customer ID number already exists add the total to the exisiting total
    if customerIDs[i] in data:

        data[customerIDs[i]] += total
# if the customer ID does not exist, use total as the total for the customer
    else:
        data[customerIDs[i]] = total
# create new dataframe using dictionary, grabbing all keys and all the values into the dictionary
df_2 = pd.DataFrame({'Customer IDs': data.keys(),
                    'Customer Amounts': data.values()})
# round the data frame to 2 decimals
df_2 = df_2.round(2)
# move big dataframe into a new csv file and remove index numbers for formating
df_2.to_csv('salesreport.csv', index=False)
