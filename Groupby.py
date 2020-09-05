import numpy as np
import pandas as pd

#Groupby allows you to group together rows based offf of a column and perform an aggregate functiom on them
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB', 'FB'], 'Person':['Sam','Charlie', 'Amy', 'Vanessa', 'Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
#get the common columns by groupby (groupby only return a DataFrameGroupBy Object)
byComp = df.groupby('Company')
#have to pass a aggregate function 
byComp.mean()
byComp.sum()
byComp.std()

#get the sum of specific index
byComp.sum().loc['FB']
df.groupby('Company').count()

#get information of each index
df.groupby('Company').describe()

#use horizontal format
df.groupby('Company').describe().transpose()['FB']
