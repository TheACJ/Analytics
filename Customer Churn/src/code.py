import numpy as np
import pandas as pd
import plotly.express as px 
df=pd.read_csv('telecom_customer_churn.csv')
#print(df.head(5))
df.columns
df1=df.copy()
# Unwanted colunms will be dropped with the drop() function
df1.drop(['Customer ID','Total Refunds','Zip Code','Latitude','Longitude','Churn Category','Churn Reason'],axis='columns',inplace=True)
#print(df1.shape)
df1.dtypes
# Check for unique values in each column
features = df1.columns
""" for feature in features:
     print(f'{feature}--->{df[feature].nunique()}') """
# Get percentage of NULL data in each column
df1.isnull().sum() / df1.shape[0]
#Cleaning Function for the Dataset
def clean_dataset(df):
    assert isinstance(df, pd.DataFrame)
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)
# --------------------
df1=df1.interpolate()
df1=df1.dropna()
df.head()
df['Unlimited Data']
# all the number columns in a variable
number_columns=['Age','Number of Dependents','Number of Referrals','Tenure in Months','Avg Monthly Long Distance Charges','Avg Monthly GB Download','Monthly Charge','Total Charges','Total Extra Data Charges','Total Long Distance Charges','Total Revenue']
# Function to check unique values of column having datatype:"object"
""" def unique_values_names(df):
    for column in df:
        if df[column].dtype=='object':
            print(f'{column}:{df[column].unique()}')
#Calling the above function with a dataframe
unique_values_names(df1)
 """
#Visusalizing Column "Age" in the dataset
""" fig = px.histogram(df1, x = 'Age')
fig.show() """
#-----
print(df1.hist(figsize=(15,15), xrot=30))
