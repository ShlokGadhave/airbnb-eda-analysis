import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  #Importing Essentials 
import seaborn as sns 
df=pd.read_csv('datasets.csv') # Import Dataset 
print(df)
# Intial Exploration
print(df.head(10)) 
print(df.columns)
print(df.info()) 
print(df.describe()) #Statisical records 
print(df.shape)

#Data Cleaning 
print(df.dropna(inplace=True)) #dropping all missing values
print(df.isnull().sum())
print(df.shape)
#Dealing with the duplicates 
print(df.duplicated().sum())
print(df[df.duplicated()]) #Retriving all the duplicates values 
#Deleting all the duplicates 
print(df.drop_duplicates(inplace=True))

#type casting
df['id']=df['id'].astype(object)
df['host_id']=df['host_id'].astype(object)
print(df.dtypes)

#Univairate Analysis 
data=df[df['price']<1500]
print(data)

plt.figure(figsize=(6,5))
sns.boxplot(x='price',data=data,color="cyan")
plt.title('Outilers of Price Disturbtion below 1500')
plt.show()


plt.figure(figsize=(5,5))
sns.histplot(x='price',data=data,bins=30,color='lightgreen')
plt.title('Price Disturbtion below 1500')
plt.show()

sns.countplot(x='reviews_per_month',data=df,color='red')
plt.title('Reviews Per Month')
plt.ylabel('Frequency')
plt.show()

sns.histplot(x='availability_365',data=df)
plt.title('Availability Disturbution')
plt.ylabel('Frequency')
plt.show()

# group function
group=df.groupby(by='neighbourhood_group')['price'].mean()
print(group)
# Feature Engineering 
df['price per bed ']=df['price']/df['beds']
print(df.head())

# Average Price per bed 
groups=df.groupby(by='neighbourhood_group')['price per bed '].mean()
print(groups)

# Bivairable Analysis

sns.barplot(x='neighbourhood_group',y='price',data=df,hue='room_type',palette='muted')
plt.title('Price Dependency on Neighbourhood')
plt.show()


sns.scatterplot(x='number_of_reviews',y='price',data=df,hue='neighbourhood_group')
plt.title('Price Dependency on Number of Price')
plt.show()

sns.pairplot(
     vars=['latitude','longitude','minimum_nights','calculated_host_listings_count'],
     data=df.sample(1000),   # taking only 1000 rows
     hue='room_type',
     palette='colorblind'
 )

plt.show()

# Geographical Distuburtion of Airbnb 

sns.scatterplot(x='longitude',y='latitude',data=df,hue='room_type')
plt.title(' Geographical Distuburtion of Airbnb ')
plt.show()

#heatmap correlation of one vairable with others on numerical columns 

corr=df[['latitude','price','number_of_reviews','longitude','reviews_per_month','calculated_host_listings_count','availability_365','beds']].corr()
print(corr)

sns.heatmap(data=corr,annot=True)
plt.show()