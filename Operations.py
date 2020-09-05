import numpy as np
import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],
                    'col2':[444,555,666,444],
                    'col3':['abc','def','ghi','xyz']})

#return the unique value
df['col2'].unique()                    

#return the number of unique value
df['col2'].nunique()

#count the value
df['col2'].value_counts()

#apply method
#use for applying our own method
def times2(x):
    return x*2
df['col1'].apply(times2)

#apply with lambda
df['col2'].apply(lambda x: x*2)

#remove columns
#df.drop('col1',axis=1,inplace=True)

#get list of columns in DF
df.columns

#information of index
df.index

#sort values by column
df.sort_values('col2')

#check null value
df.isnull()

data = {'A':['foo','foo','foo','bar','bar','bar'],
        'B': ['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)


#rewrite the df into multi-level index
df.pivot_table(values='D',index=['A','B'], columns='C')