#PHASE 1:
    
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("customer_analytics.csv")

#PHASE 2: Data Cleaning

#Before cleaning
df.head()
df.shape
df.info()
df.describe()

#Missing values
print("\nBefore Cleaning\n")
print("\nIdentifying Missing Values:-\n","\n", df.isnull().sum())

#Duplicate Rows
print("\nIdentifying Duplicate Row=", df.duplicated().sum())

#filling missing values and dropping duplicate rows
df["Education"] = df["Education"].fillna("Unknown")
df["AnnualIncome"] = df["AnnualIncome"].fillna(df["AnnualIncome"].mean())
df = df.drop_duplicates()
print("\nFilled missing values in AnnualIncome with its mean, also filled missing values in Education with Unkown, and dropped the duplicate rows")

#After cleaning
print("\nMissing Values:-\n","\n", df.isnull().sum())
print("\nDuplicate Row=", df.duplicated().sum())

#PHASE 3: Univariate and bivariate analysis

plt.figure()
plt.subplot(1,3,1)
plt.hist(df['Age'], bins=20)
plt.title("Age Frequency")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.subplot(1,3,2)
plt.hist(df['PurchaseFrequency'], bins=20)
plt.title("Distribution of PurchaseFrequency")
plt.xlabel("Purchase")
plt.ylabel("Frequency")

plt.subplot(1,3,3)
df['MaritalStatus'].value_counts().plot(kind='bar')
plt.title("MaritalStatus")
plt.tight_layout()
plt.show()


plt.figure()
plt.subplot(1, 2, 1)
sns.scatterplot(x=df['Age'], y=df['YearsEmployed'])
plt.title("Age vs YearsEmployed")

plt.subplot(1, 2, 2)
sns.boxplot(x=df['MaritalStatus'], y=df['Age'])
plt.title("MaritalStatus vs Age")
plt.tight_layout()
plt.show()

print("\nINSIGHTS FROM GRAPHS:-\n")
print("\n-The 1st Histogram is indicating that the dataset primarily represents middle-aged adults.")
print("\n-The 2nd Histogram shows moderate purchasing behavior, with fewer customers making very high numbers of purchases.")
print("\n-The BarChart shows the data set is not heavily skewed towards either groups i.e. Single or Married.")
print("\n-The scatterplot shows older individuals have been employed for more years.")
print("\n-In the Boxplot it indicates married individuals tend to be middle aged 30-50 whereas single individuals are from younger age.\n")

#PHASE 4: Correlation Matrix
   
plt.figure() 
corr_matrix=df.corr(numeric_only=True)
print(corr_matrix)
sns.heatmap(corr_matrix,annot=True)
plt.show()

print("\nThe strongest correlation is between age and employment (0.98)\n")
print("\n")
print("\nExecutive Summary:-\n")
print("\n-Age is Strongly Associated with Employment Status\n -Married Customers Tend to Be Older\n -Increase in Employed experience with increase in Age\n")





