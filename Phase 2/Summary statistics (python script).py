import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt


# ## Read the data and display it
df = pd.read_excel('Diabete Cleaned data set2.xlsx', sheet_name = 0, index_col = 0)
print(df.head())
print("--------------------------------------")

# ## Summary statistics
df_new = df.describe().rename(index = {"50%": "median"}).drop('count')
print(df_new)
print("--------------------------------------")

# ## Export the table to an excel file
df_new.to_excel('summary statistics data set 2.xlsx')

# ## Calculate the coordinates and display it
corrMatrix = df.corr()
print(corrMatrix.head())
print("--------------------------------------")

plt.figure(figsize=(16, 16))
sn.heatmap(corrMatrix, annot = True)
plt.show()





