#task 1

import pandas as pd 
df= pd.read_csv("customer_order.csv")
print("Shape before cleaning", df.shape)
print("MIssing values", df.isna().sum())
df["CustID"] = df["CustID"].fillna("Unknown")
df["Name"] = df["Name"].fillna("Unknown")
df["Amount"] = df["Amount"].fillna(df["Amount"].median())
df["Payment"] = df["Payment"].fillna("Unknown")
df["City"] = df["City"].fillna("Unknown")
df["Date"] = df["Date"].fillna("Unknown")
print("Number of duplicate rows", df.duplicated().sum())
df = df.drop_duplicates()
print("\nShape after cleaning", df.shape)
print(df.head())

#task 2

af = pd.read_csv("customer_order2.csv")
print("\nData type before conversion:", af.dtypes)
af["Price"] = af["Price"].str.replace('$','')
af["Price"] = af["Price"].str.replace(',','')
af["Price"] = af["Price"].astype(float)
af["Date"] = pd.to_datetime(af["Date"])
print("\nData type after conversion:", af.dtypes)

#task 3

bf = pd.read_csv("customer_order3.csv")
print(bf.head())
bf["Location"] = bf["Location"].str.strip()
bf["Location"] = bf["Location"].str.lower()
print(bf["Location"].unique())
print(bf.head())
