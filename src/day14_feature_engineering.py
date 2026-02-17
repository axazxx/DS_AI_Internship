#task 1

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

data = {
        "Car_ID": ["C001","C002","C003","C004","C005","C006"],
        "Transmission": ['Automatic','Manual','Automatic','Manual','Automatic','Manual'],
        "Color": ['Red','Blue','Green','Red','Blue','Green']
       }

df=pd.DataFrame(data)

le = LabelEncoder()
df['Transmission'] = le.fit_transform(df['Transmission'])
df = pd.get_dummies(df, columns=['Color'], drop_first=True)

#task 2

data1 = {
         'Age': [10,20,30,40,50,60],
         'Salary': [20000,30000,40000,50000,65000,42000]
         }
bf=pd.DataFrame(data1)

scalar = StandardScaler()
scaled_features = scalar.fit_transform(bf[['Age', 'Salary']])

scalar=MinMaxScaler()
bf[['Age','Salary']]=scalar.fit_transform(bf[['Age','Salary']])
print("AGE AND SALARY\n",bf)

plt.subplot(1,2,1)
sns.histplot(bf["Salary"],kde=True)
plt.title("Before scaling")

plt.subplot(1,2,2)
sns.histplot(scaled_features[:,1],kde=True)
plt.title("After scaling")
plt.show()

#task 3

cf=pd.read_csv("gdp.csv")
X_train,X_test,y_train,y_test=train_test_split(cf[['Year']],cf[['Value']],train_size=0.8,random_state=42)
model1=LinearRegression()
model1.fit(X_train,y_train)
baseline_preds=model1.predict(X_test)
baseline_score=r2_score(y_test,baseline_preds)
print("Score when model is trained with original features\n",baseline_score)
poly=PolynomialFeatures(degree=2,include_bias=False)
X_train_poly=poly.fit_transform(X_train)
X_test_poly=poly.transform(X_test)
poly_model=LinearRegression()
poly_model.fit(X_train_poly,y_train)
poly_preds=poly_model.predict(X_test_poly)
poly_score=r2_score(y_test,poly_preds)
print("Score when model is trained with Polynomial Features\n",poly_score)