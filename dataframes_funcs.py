import numpy as np
import pandas as pd 

my_series = pd.Series( data = [2,3,5,4],             # Data
                       index= ['a', 'b', 'c', 'd'])  # Indexes

print(my_series)

my_dict = {"x": 2, "a": 5, "b": 4, "c": 8}

my_series2 = pd.Series(my_dict)

print(my_series2) 

# dataframes

# Create a dictionary with some different data types as values

my_dict = {"name" : ["Joe","Bob","Frans"],
           "age" : np.array([10,15,20]),
           "weight" : (75,123,239),
           "height" : pd.Series([4.5, 5, 6.1], 
                                index=["Joe","Bob","Frans"]),
           "siblings" : 1,
           "gender" : "M"}

df = pd.DataFrame(my_dict)   # Convert the dict to DataFrame

print(df)                           # Show the DataFrame


my_dict2 = {"name" : ["Joe","Bob","Frans"],
           "age" : np.array([10,15,20]),
           "weight" : (75,123,239),
           "height" :[4.5, 5, 6.1],
           "siblings" : 1,
           "gender" : "M"}

df2 = pd.DataFrame(my_dict2)   # Convert the dict to DataFrame

print(df2)                            # Show the DataFrame