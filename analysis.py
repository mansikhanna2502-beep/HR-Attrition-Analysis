import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("hr_attrition.csv")
df.head()

df.info()
df.describe()

## Atrition count
sns.countplot(x='Attrition', data=df)
plt.title("Employee Attrition Count")
plt.show()

## Attrition by Gender
sns.countplot(x='Gender', hue='Attrition', data=df)
plt.title("Attrition by Gender")
plt.show()

## Atrition by Job Role
plt.figure(figsize=(10,5))
sns.countplot(y='JobRole', hue='Attrition', data=df)
plt.title("Attrition by Job Role")
plt.show()

## Salary distribution by attrition
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df)
plt.title("Salary vs Attrition")
plt.show()

## Correlation heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()