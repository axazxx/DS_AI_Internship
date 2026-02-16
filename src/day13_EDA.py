import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#task 1

print("TASK 1")
df=pd.read_csv("house_prices.csv")
plt.subplot(1,2,1)
sns.histplot(df["Price"],kde=True)
plt.title('Histogram of Price')
plt.xlabel('Price')
plt.ylabel('Count')
plt.show()
print("Skewness of PRICE",df['Price'].skew())
print("Kurtosis of PRICE",df["Price"].kurt())
plt.subplot(1,2,2)
sns.countplot(x='Neighborhood',data=df)
plt.title('Count of Neighborhoods')
plt.xlabel('Count')
plt.ylabel('Neighborhood')
plt.tight_layout()
plt.show()

#task 2

sns.set(style="whitegrid")

print("TASK 2")
df= pd.read_csv("house_prices.csv")
plt.subplot(1, 2, 1)
sns.scatterplot(x='SqFt', y='Price', data=df)
plt.subplot(1, 2, 2)
sns.boxplot(x='Price', y='Brick', data=df)
plt.tight_layout()
plt.show()

print("\nAs X increases, Y seems to increase")

#task 3

print("TASK 3")
plt.subplot(1,2,1)
corr_matrix=df.corr(numeric_only=True)
print(corr_matrix)
print("There are no two variables with correlation score higher than 0.8")
sns.heatmap(corr_matrix,annot=True)
plt.show()
plt.subplot(1,2,2)
sns.boxplot(x=df['Price'])
plt.xlabel('Price')
plt.tight_layout()
plt.show()