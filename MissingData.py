import numpy as np
import pandas as pd
d = {'A': [1,2,np.nan], 'B': [5,np.nan,np.nan],'C': [1,2,3]}
df = pd.DataFrame(d)

#dropna method
df.dropna(axis=1) #drop columns with null values

#dropna with thresh 
#passing thresh value to determine which row to drop
#i.e: thresh = 2 will see if a row has at least 2 non-NA values
df.dropna(thresh=2)

#fill method (replace missing value)
df.fillna(value='FILL VALUE')
df['A'].fillna(value=df['A'].mean()) #fill na values in column A
