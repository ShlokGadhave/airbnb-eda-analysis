🏠 Airbnb Data Analysis Project
📌 Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on an Airbnb dataset using Python libraries like:

Pandas
NumPy
Matplotlib
Seaborn

The main objective of this project is to analyze Airbnb listings, understand pricing patterns, detect outliers, visualize geographical distributions, and explore relationships between multiple variables.

📂 Dataset Information

The dataset contains Airbnb listing information such as:

Column Name	Description
id	Unique ID of listing
host_id	Unique ID of host
neighbourhood_group	Area/Region of listing
latitude	Latitude location
longitude	Longitude location
room_type	Type of room
price	Price of listing
minimum_nights	Minimum nights required
number_of_reviews	Total reviews
reviews_per_month	Monthly reviews
availability_365	Availability in year
beds	Number of beds
calculated_host_listings_count	Total listings by host
⚙️ Technologies Used
Technology	Purpose
Python	Programming Language
Pandas	Data Cleaning & Analysis
NumPy	Numerical Operations
Matplotlib	Data Visualization
Seaborn	Advanced Statistical Graphs
🧹 Data Cleaning Process
✅ Handling Missing Values
df.dropna(inplace=True)
Removed all rows containing null values.
Helps in improving data quality.
✅ Duplicate Handling
df.drop_duplicates(inplace=True)
Removed duplicate records from dataset.
Prevents repeated data affecting analysis.
✅ Type Casting
df['id']=df['id'].astype(object)
df['host_id']=df['host_id'].astype(object)
Converted IDs into object datatype.
IDs are categorical identifiers, not numerical values.
📊 Exploratory Data Analysis (EDA)
1️⃣ Boxplot Analysis
sns.boxplot(x='price',data=data,color="cyan")
📌 Purpose
Detects outliers in Airbnb prices.
Shows spread of pricing data.
📈 Graph Explanation

The boxplot displays:

Median price
Quartiles
Outliers
🔍 Observation
Many listings have extremely high prices.
Most listings are concentrated below ₹1500.
2️⃣ Price Distribution Histogram
sns.histplot(x='price',data=data,bins=30,color='lightgreen')
📌 Purpose
Understands distribution of Airbnb prices.
📈 Graph Explanation
X-axis → Price
Y-axis → Frequency
🔍 Observation
Majority listings are low to medium priced.
Very few expensive listings.
3️⃣ Reviews Per Month Countplot
sns.countplot(x='reviews_per_month',data=df,color='red')
📌 Purpose
Shows frequency of monthly reviews.
📈 Observation
Most properties receive fewer reviews monthly.
Highly reviewed properties are less common.
4️⃣ Availability Distribution
sns.histplot(x='availability_365',data=df)
📌 Purpose
Understands yearly availability of Airbnb listings.
📈 Observation
Some listings are available throughout the year.
Others are booked frequently.
5️⃣ GroupBy Analysis
group=df.groupby(by='neighbourhood_group')['price'].mean()
📌 Purpose
Calculates average price by neighbourhood.
📈 Observation
Certain neighbourhoods have significantly higher average prices.
6️⃣ Feature Engineering
df['price per bed ']=df['price']/df['beds']
📌 Purpose

Created a new feature:

➜ Price Per Bed

This helps compare property pricing more fairly.

7️⃣ Barplot Analysis
sns.barplot(x='neighbourhood_group',y='price',data=df,hue='room_type')
📌 Purpose
Compares room prices across neighbourhoods.
📈 Observation
Entire homes are generally more expensive.
Shared rooms are cheaper.
8️⃣ Scatterplot Analysis
sns.scatterplot(x='number_of_reviews',y='price',data=df,hue='neighbourhood_group')
📌 Purpose
Studies relationship between reviews and price.
📈 Observation
Highly priced listings do not always receive more reviews.
9️⃣ Pairplot Analysis
sns.pairplot(
     vars=['latitude','longitude','minimum_nights','calculated_host_listings_count'],
     data=df.sample(1000),
     hue='room_type',
     palette='colorblind'
 )
📌 Purpose
Visualizes relationships between multiple numerical variables.
📈 Observation
Helps identify patterns and correlations.
Useful for multivariable analysis.
🌍 Geographical Distribution Analysis
sns.scatterplot(x='longitude',y='latitude',data=df,hue='room_type')
📌 Purpose
Displays geographical locations of Airbnb properties.
📈 Observation
Airbnb listings are densely concentrated in certain regions.
Different room types appear across various locations.
🔥 Correlation Heatmap
corr=df[['latitude','price','number_of_reviews','longitude','reviews_per_month','calculated_host_listings_count','availability_365','beds']].corr()

sns.heatmap(data=corr,annot=True)
📌 Purpose
Measures correlation between numerical features.
📈 Heatmap Interpretation
Positive correlation → Variables increase together.
Negative correlation → One increases while other decreases.
🔍 Observation
Some variables show weak correlation with price.
Useful for feature selection in machine learning.
🚀 Key Learnings From Project

✔ Data Cleaning Techniques
✔ Handling Missing Values
✔ Duplicate Removal
✔ Feature Engineering
✔ Data Visualization
✔ Correlation Analysis
✔ Exploratory Data Analysis (EDA)
✔ Geographical Data Visualization


▶️ How To Run Project
1️⃣ Install Required Libraries
pip install pandas numpy matplotlib seaborn
2️⃣ Run Python File
python main.py
📸 Output Graphs Included
Boxplot
Histogram
Countplot
Scatterplot
Pairplot
Heatmap
Barplot
Geographical Visualization

📌 Conclusion

This project provides complete exploratory analysis of Airbnb listings using Python. It demonstrates practical implementation of data cleaning, visualization, feature engineering, and statistical analysis techniques which are essential in Data Analytics and Machine Learning projects.
