import pandas as pd

#read csv file
df = pd.read_cvs('example.csv')

df.to_csv('My_output',index=False)
pd.read_cvs('My_output')


#read excel
pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1')

#save excel file
df.to_excel('Excel_Sample2.xlsx',sheet_name='NewSheet')

#read html 
data = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')

#work with SQL
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
df.to_sql('my_table',engine)
sqldf = pd.read_sql('my_table',con=engine)

