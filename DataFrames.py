import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101) #make sure we get the same random numbers

#DataFrame(data, index, columns)
df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'], ['W','X','Y','Z'])

#get Series out of DataFrame by grabbing a columns 
df['W']

#create a new columns
df['new'] = df['W'] + df['Y']

#erase the columns
#drop(label, axis=1, inplace=True)
#axis = 1 means columns, 0 means rows
df.drop('new', axis = 1, inplace=True)

#get many columns 
df[['Z','X']]

#selecting ROWS by label name
df.loc['A']

#selecting ROWS by numerical index
df.iloc[3]

#selecting ROWS and COLUMNS
df.loc['B','Y']

#selecting multiple ROWS and multiple COLUMNS
df.loc[['A', 'B'], ['W', 'Y']]


#---------Part 2--------------#
#conditional selection
booldf = df > 0
df[booldf]
df[df>0]
df[df['W']>0] #only display the true condition
df[df['Z']<0] 
df[df['W']>0][['Y','X']]

#nultiple condition
df[(df['W']>0) & (df['Y']>1)] #have to use & instead of and
df[(df['W']>0) | (df['Y']>1)]

#reset the index using reset_index (reset into numerical index)
df.reset_index()

#new index
newind = 'CA NY WY OR CO'.split()
df['States'] = newind

#set index
df.set_index('States')


#----------------Part 3------------------#
# Index Levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index) 

#create a DF
df = pd.DataFrame(randn(6,2), hier_index,['A','B'])

#accessing multi index
df.loc['G1'].loc[1]

#create a names for multi index
df.index.names = ['Groups', 'Num'] #outside index is Groups
                                   #inside index is Num
#get the G2 at outside index, 2 at inside index, and column B
df.loc['G2'].loc[2]['B']

#cross section (use for multi level index only)
#grab data from inner index "1". Remember pass the name of the index
df.xs(1, level='Num')
