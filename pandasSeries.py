import pandas as pd
import numpy as np

#create a list
labels = ['a', 'b', 'c']
my_data = [10,20,30]

#create a numpy array
arr =np.array(my_data)

#create a dict
d = {'a':10, 'b':20, 'c':30}

#create a Series (default index as number)
pd.Series(data = my_data)

#create a Series with desired index
pd.Series(data=my_data, index=labels)

#short-way
pd.Series(my_data, labels)

#we can pass numpy array
pd.Series(arr,labels)

#We can also pass dict in Series, it will automatedly use key as index
pd.Series(d)

#Can pass built-in function in Series
pd.Series(data=[sum,print,len])

#understanding index
ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])
ser2 = pd.Series([1,2,5,4], ['USA', 'Germany', 'Italy', 'Japan'])

ser1['USA'] ##passing the index

# plus two Series will find and sum the similar index
ser1 + ser2 




