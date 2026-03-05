import pandas as pd
from sklearn.impute import SimpleImputer
import os

#setting working directory to properly read the file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#reading the file
df=pd.read_csv("titanic_new.csv")


#searching for the columns with majority of null info 
print("Null values:\n", df.isnull().sum())
#decided to drop "Cabin" beacuse it had a lot of missing values
df.drop(columns=["Cabin"], inplace=True)
#regarding "Age" column I decided to fill null values by using imputation
df=SimpleImputer(strategy="mean")
df.fit()
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!DOK
print("---------------")

print("Unique values:\n", df.nunique())
drop_cols=["Passenger.Id", "Name", "Ticket"]
df.drop(columns=drop_cols, inplace=True)

print(df.head())