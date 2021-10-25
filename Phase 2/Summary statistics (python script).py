import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt


# Read the data and display it
df = pd.read_excel('Diabete Cleaned data set2.xlsx', sheet_name = 0, index_col = 0)
print(df.head())
print("--------------------------------------")

# Summary statistics
df_new = df.describe().rename(index = {"50%": "median"}).drop('count')
print(df_new)
print("--------------------------------------")

# Export the table to an excel file
df_new.to_excel('summary statistics data set 2.xlsx')

# Calculate the coordinates and display the table
corrMatrix = df.corr()
print(corrMatrix.head())
print("--------------------------------------")

# Drop the "Under 65 from diabetes (2019)", "Age-adjusted Hospitalizations From Or With Diabetes (2019)", and "Age-adjusted Deaths from Diabetes, Rate Per 100,000 Population, 2019 from Diabetes count(2019)" columns
new_corrMatrix = corrMatrix.drop(corrMatrix.columns[[11, 12, 13]], axis = 1)
new_corrMatrix.drop(new_corrMatrix.index[[11, 12, 13]], inplace = True)

print(new_corrMatrix.head())
print("--------------------------------------")

# Using Heat map to display the correlation between the variables
plt.figure(figsize=(16, 16))
sn.heatmap(corrMatrix, annot = True)
plt.show()





