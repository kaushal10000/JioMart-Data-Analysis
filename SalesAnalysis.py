import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df=pd.read_csv(r"C:\Users\kaush\Data Analysis\SuperMarket Sales\JioMart Sales Data.csv",encoding='unicode-escape')

print(df.shape)
print(df.head(11))
print()
print(df.info())

df.drop(['Status','unnamed1'], axis=1, inplace=True)
print(pd.isnull(df))
print("Null Values in Dataset:\n",pd.isnull(df).sum())

df.dropna(inplace=True)
print("Null Values in Dataset after using Dropna:\n",pd.isnull(df).sum())
df['Amount']=df['Amount'].astype(int)
print(df['Amount'].dtypes)

print(df.columns)
print(df.describe())
print(df[['Age','Orders','Amount']].describe())

g_sns=sns.countplot(x='Gender',data=df)
for bars in g_sns.containers:
    g_sns.bar_label(bars)
plt.title("Purchases Made by Females Vs Males")
plt.savefig("Purchases Made by Females Vs Males")
plt.show()
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Gender',y='Amount', data=sales_gen)
plt.title("Amount Spent by Female and Male Consumers")
plt.savefig("Amount Spent by Female and Male Consumers")
plt.show()

a_sns=sns.countplot(data=df,x='Age Group',hue='Gender')
for bars in a_sns.containers:
    a_sns.bar_label(bars)
plt.savefig("Agewise Customers(Females Vs Males)")
plt.title("Agewise Customers(Females Vs Males)")
plt.show()
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group',y='Amount', data=sales_age)
plt.savefig("Agewise Customers")
plt.title("Agewise Customers")
plt.show()

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(18,6)})
sns.barplot(x='State',y='Orders', data=sales_state)
plt.title("Statewise Orders")
plt.savefig("Statewise Orders")
plt.show()

sales_state_amount = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(18,6)})
sns.barplot(x='State',y='Amount', data=sales_state_amount)
plt.title("Statewise Purchases Made")
plt.savefig("Statewise Purchases Made")
plt.show()

m_sns=sns.countplot(data=df,x='Marital_Status')
for bars in m_sns.containers:
    m_sns.bar_label(bars)
sns.set(rc={'figure.figsize':(8,6)})
plt.title("Purchases Made by Married Vs Singles")
plt.savefig("Purchases Made by Married Vs Singles")
plt.show()

sales_status = df.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.barplot(x='Marital_Status',y='Amount',hue='Gender', data=sales_status)
sns.set(rc={'figure.figsize':(8,6)})
plt.savefig("Marital Status based Customers")
plt.title("Marital Status based Customers")
plt.show()

o_sns=sns.countplot(x='Occupation',data=df)
for bars in o_sns.containers:
    o_sns.bar_label(bars)
sns.set(rc={'figure.figsize':(30,6)})
plt.savefig("Occupation based Customers")
plt.title("Occupation based Customers")
plt.show()

sales_Occupation = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Occupation',y='Amount', data=sales_Occupation)
sns.set(rc={'figure.figsize':(20,6)})
plt.savefig("Occupation wise Customers")
plt.title("Occupation wise Customers")
plt.show()

product_sns=sns.countplot(data=df,x='Product_Category')
for bars in product_sns.containers:
    product_sns.bar_label(bars)
sns.set(rc={'figure.figsize':(30,8)})
plt.savefig("Product Category wise Sales")
plt.title("Product Category wise Sales")
plt.show()

sales_product = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.barplot(x='Product_Category',y='Amount', data=sales_product)
sns.set(rc={'figure.figsize':(24,8)})
plt.savefig("Product Category wise Amount Spent")
plt.title("Product Category wise Amount Spent")
plt.show()

sales_productid = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False)
sns.barplot(x='Product_ID',y='Orders', data=sales_productid)
sns.set(rc={'figure.figsize':(18,6)})
plt.savefig("Product ID wise Sales")
plt.title("Product ID wise Sales")
plt.show()


#Conclusion
'''Married women age group 26-35 yrs from UP,  Maharastra and Karnataka working in IT, Healthcare
 and Aviation are more likely to buy products from Food, Clothing and Electronics category'''