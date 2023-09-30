import pandas as pd
import numpy as np

print(pd.__version__)

# Create a pandas series from each of the items below: a list, numpy and a dictionary
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

series_1 = pd.Series(mylist)
series_2 = pd.Series(myarr)
series_3 = pd.Series(mydict)

#print(series_1.head(3))
#print(series_2.head(3))
#print(series_3.head(3))

number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting iterator to list
result_list = list(result)
#print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting iterator to set
result_set = set(result)
#print(result_set)

# Convert the series ser into a dataframe with its index as another column on the dataframe.
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)

#print('mydict')
mydict = dict(zip(mylist, myarr))
#print(mydict)

#print('ser')
ser = pd.Series(mydict)
#print(ser.head(3))

#print('df')
df = ser.to_frame().reset_index()
#print(df.head(3))

#print('df1')
df1 = pd.DataFrame(ser)
#print(df1.head(3))

# Combine ser1 and ser2 to form a dataframe.
import numpy as np
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

# Solution 1
df = pd.concat([ser1, ser2], axis=1).reset_index()
#print(df.head())

# Solution 2
df = pd.DataFrame({'col1': ser1, 'col2': ser2}).reset_index()
#print(df.head())

# Give a name to the series ser calling it ‘alphabets’.
ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser.name = 'thisame'
#print(ser.head())

# From ser1 remove items present in ser2.
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

print('ser1')

# Solution
res = ser1[~ser1.isin(ser2)]

print(res)





