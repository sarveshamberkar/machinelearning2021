import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading data and dividing according to categorical variable

df = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
# print(df.iloc[(df['species'] == 'setosa').values,:]) using iloc
df_setosa = df.loc[df['species'] == 'setosa']
df_virginica = df.loc[df['species'] == 'virginica']
df_versicolor = df.loc[df['species'] == 'versicolor']

# Univariant Analysis

plt.plot(df_setosa['sepal_length'], np.zeros_like(df_setosa['sepal_length']), 'o')
plt.plot(df_virginica['sepal_length'], np.zeros_like(df_virginica['sepal_length']), 'o')
plt.plot(df_versicolor['sepal_length'], np.zeros_like(df_versicolor['sepal_length']), 'o')

plt.savefig('plots/UnivariantExample.jpg')
print(df.columns.tolist())
# bivariant analysis
sns.FacetGrid(df, hue='species', height=5).map(plt.scatter, 'sepal_length', 'sepal_width')
plt.savefig('plots/BivariantExample.jpg')

# multivariant analysis
sns.pairplot(df, hue='species',height=3)
plt.savefig('plots/MultivariantExample.jpg')
