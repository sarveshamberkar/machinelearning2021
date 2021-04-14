import numpy as np
import pandas as pd

# print(np.random.randn(100,200,8).shape)
# print(np.linspace(10,20,50,endpoint=True))
a = np.arange(0, 20, step=1).reshape((4, 5))
# print(a)

df = pd.DataFrame(data=np.arange(0, 20, step=1).reshape((4, 5)),
                  columns=['column' + str(i) for i in range(5)],
                  index=['row' + str(i) for i in range(4)])
# print(df)

# this give is complete row of the of data frame and return type is pandas dataframe series
# print(df.loc['row1'])
# this gives dataframe or series depending upon slicing this allows you to give the target data using slicing
# print(df.iloc[0:2, 1:])
#              ^   ^
#             row  column
# print(np.unique(df['column1'].unique(),return_counts=True)[1])
df = pd.read_csv('data/train.csv', nrows=100, index_col=2)  # index_col makes a particular column to row index
print(df.head())
print(df['X1'].value_counts())
