#  use pip install pandas to run

import pandas as pd

# Cleaning the dining CSV
df = pd.read_csv("dining.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df['Rating'] = df['Rating'].fillna(2.5)
df['No of Reviews'] = df['No of Reviews'].fillna(1)
df['No of Reviews'] = df['No of Reviews'].str.replace(',', '')
df['Price Range'] = df['Price Range'].fillna("$$")
df['Address'] = df['Address'].fillna("")
df['Description'] = df['Description'].fillna("")
df.to_csv("dining_clean.csv", index=False)

# Cleaning the entertainment CSV
df = pd.read_csv("entertainment.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df['Rating'] = df['Rating'].fillna(2.5)
df['No of Reviews'] = df['No of Reviews'].fillna(1)
df['No of Reviews'] = df['No of Reviews'].str.replace(',', '')
df['Price Range'] = df['Price Range'].fillna("$$")
df['Address'] = df['Address'].fillna("")
df['Description'] = df['Description'].fillna("")
df.to_csv("entertainment_clean.csv", index=False)

# Cleaning the landmark CSV
df = pd.read_csv("landmark.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df['RATING'] = df['RATING'].fillna(2.5)
df['No Of Reviews'] = df['No Of Reviews'].fillna(1)
df['No Of Reviews'] = df['No Of Reviews'].str.replace(',', '')
df['Address'] = df['Address'].fillna("")
df['DESCRIPTION'] = df['DESCRIPTION'].fillna("")
df.to_csv("landmark_clean.csv", index=False)

# Cleaning the museum CSV
df = pd.read_csv("museum.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df['RATING'] = df['RATING'].fillna(2.5)
df['No OF Reviews'] = df['No OF Reviews'].fillna(1)
df['No OF Reviews'] = df['No OF Reviews'].str.replace(',', '')
df['ADDRESS'] = df['ADDRESS'].fillna("")
df['DESCRIPTION'] = df['DESCRIPTION'].fillna("")
df.to_csv("museum_clean.csv", index=False)

# Cleaning the park CSV
df = pd.read_csv("park.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df['Rating'] = df['Rating'].fillna(2.5)
df['No of Reviews'] = df['No of Reviews'].fillna(1)
df['No of Reviews'] = df['No of Reviews'].str.replace(',', '')
df['Address'] = df['Address'].fillna("")
df['Description'] = df['Description'].fillna("")
df.to_csv("park_clean.csv", index=False)
