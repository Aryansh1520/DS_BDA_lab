import numpy as np
import pandas as pd
import math
df=pd.read_csv('raw_data.csv')
s_values=df['math score'].sum()
c_values=df['math score'].count()
mean=s_values/c_values
print(mean)
np.sort(df['math score'])
middle_index=math.floor(c_values/2)
median=np.sort(df['math score'])[middle_index]
print(median)
max_value=np.sort(df['math score'])[-1]
print(max_value)
min_value=np.sort(df['math score'])[0]
print(min_value)
def max_value(variable):
    return np.sort(df[variable])[-1]
max_value('math score')
def median_value(variable):
    middle_index=math.floor(c_values/2)
    return np.sort(df[variable])[middle_index]
median_value('math score')
df['math score'].std()
def std_dev(variable):
    lst=[]
    for i in range(c_values):
        sigma=(df[variable][i]-mean)**2
        lst.append(sigma)
    return np.sqrt(sum(lst)/c_values)
std_dev('math score')
std_dev('reading score')
df.describe()
def variance(data,ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)

def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev
variance(df['math score'])
stdev(df['math score'])
stdev(df['reading score'])
stdev(df['placement offer count'])
