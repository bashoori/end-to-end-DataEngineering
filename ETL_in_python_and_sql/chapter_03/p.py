import pandas as pd
f = pd.read_excel("ETL_in_python_and_sql/chapter_02/H+ Sport Employees.xlsx", sheet_name = "Employees-Table")
#employees = pd.read_excel("../Chapter_2/H+ Sport Employees.xlsx", sheet_name="Employees-Table")
f.head()
print(f)
