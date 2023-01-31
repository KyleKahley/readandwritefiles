# import pandas to the file
import pandas as pd
# open employee pay file with pandas to read it as a dataframe to make it like a spreadsheet
df = pd.read_csv("EmployeePay.csv")
# separate each element like a column of the useful data in the file
firstnames = df["EmpFName"]
lastnames = df["EmpLName"]
salary = df["Salary"]
bonus = df["Bonus"]

# for each person in file, print first, last, salary and bonus
for i in range(0, len(firstnames)):
    print(
        f'{firstnames[i]} {lastnames[i]} has a salary of {salary[i]} and a bonus of {bonus[i]} with a total of {(salary[i]*bonus[i])+salary[i]}')
