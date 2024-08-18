# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)

# Data loading and overview
file_path = "C:/Users/Firdevs/Downloads/analysistry2/Mental Health Dataset.csv"
df = pd.read_csv(file_path)

# Data exploration and cleaning
print(df.head())
print(df.tail())
print(df.dtypes)
print(df.info())
print(df["Gender"].value_counts())
print(df.describe(include="all"))
print("*********************")
missing_data=df.isnull().sum()
print(missing_data[missing_data>0])
print("*********************")

# Filling missing values in the 'self_employed' column
df["self_employed"].fillna("No",inplace=True)
print(df.isnull().sum())



# Creating a new column 'Stress_Level' based on 'Days_Indoors'
df["Stress_Level"]=df["Days_Indoors"].apply(lambda x:"High" if x>"7 days" else "Low" )
print(df["Stress_Level"].value_counts())


sns.set(style="whitegrid")

# Gender distribution visualization
sns.countplot(x="Gender", data=df)
plt.title("Gender distribution")
plt.show()

#Gender vs Stress Level visualization
plt.figure(figsize=(10,6))
sns.countplot(data=df,x="Gender", hue="Stress_Level")
plt.title("Gender vs Stress Level")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Self-employed vs Mental Health Treatment by Gender
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='self_employed', hue='Gender', palette='Set2', dodge=True)
plt.title('Self-employed vs Mental Health Treatment by Gender')
plt.xlabel('Self-employed Status')
plt.ylabel('Count')
plt.legend(title='Gender', loc='upper right')
plt.show()


