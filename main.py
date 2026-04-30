import pandas as pd
data=pd.read_csv("Airbnb_Open_Data.csv")
print(data.head(10))
print(data.columns) #Column Identification
print(data.shape) # Identification of rows and columns in the dataset 
#Findings and Analysis
print(data.info())
print(data.describe())
#Data Cleaning 
df=data.drop(columns=['last review', 'reviews per month',
       'review rate number', 'calculated host listings count',
       'availability 365', 'house_rules', 'license'],inplace=True)

print(df)

#Renaming The columns 
df1=data.rename(columns={'NAME':'name'})
print(df1)