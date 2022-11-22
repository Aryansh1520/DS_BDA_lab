#IMPORTING LIBRARY
import pandas as pd

#LINK TO THE DATASET
#https://www.kaggle.com/datasets/rajanand/rainfall-in-india

#LOADING THE SAID DATASET INTO A FRAME
df = pd.read_csv(r".\datasets\rainfall in india 1901-2015.csv")

data = {}

#ALL COLUMNS 
print(df.columns)
print("")

#HEAD()
print("HEAD: ")
print(df.head(10))

#CHECKING NULL VALUES IN THE DATASET
print(df["MAR"].isnull())
print("")

#DESCRIBE()
print(df["MAR"].describe())
print("")

#PRINTING SHAPE OF THE DATAFRAME
print("Shape : ",df.shape)

#SIZE OF THE DATAFRAME
print("SIZE : ",df.size)

df.dropna()
year = []
rainfall = []
newdf = df[["SUBDIVISION","YEAR","JUN"]]
print(newdf)


for x in newdf.itertuples():
    if (x[1] == "ANDAMAN & NICOBAR ISLANDS" and x[2]>=2000 and x[2]<=2010 ):
        print(x)
        #DATATYPE CONVERSION
        year.append(str(x[2]))
        rainfall.append(int(x[3]))
data = {k:v for (k,v) in zip(year,rainfall)}
print("\n\n\n\n")

#COONVERTING INTO QUATITATIVE VALUES
print(data)
