import pandas as pd

COLUMNS = ['age', 'workclass', 'fnlwgt', 'education',
           'education_num', 'marital', 'occupation', 'relationship',
           'race', 'sex', 'capital_gain', 'capital_loss', 'hours_week',
           'native_country', 'label']

features = ['age', 'workclass', 'fnlwgt', 'education',
            'education_num', 'marital', 'occupation', 'relationship',
            'race', 'sex', 'capital_gain', 'capital_loss', 'hours_week',
            'native_country']

PATH = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

df_train = pd.read_csv(PATH, skipinitialspace=True,
                       names=COLUMNS, index_col=False)

#List continuous features

CONTI_FEATURES = df_train._get_numeric_data()
# print(CONTI_FEATURES)

"""
       age  fnlwgt  education_num  capital_gain  capital_loss  hours_week
0       39   77516             13          2174             0          40
1       50   83311             13             0             0          13
2       38  215646              9             0             0          40
3       53  234721              7             0             0          40
4       28  338409             13             0             0          40
...    ...     ...            ...           ...           ...         ...
32556   27  257302             12             0             0          38
32557   40  154374              9             0             0          40
32558   58  151910              9             0             0          40
32559   22  201490              9             0             0          20
32560   52  287927              9         15024             0          40

 """

df_train[CONTI_FEATURES.columns] = df_train[CONTI_FEATURES.columns].astype('float64')

print(df_train.describe())

"""
                age        fnlwgt  education_num  capital_gain  capital_loss    hours_week
count  32561.000000  3.256100e+04   32561.000000  32561.000000  32561.000000  32561.000000
mean      38.581647  1.897784e+05      10.080679   1077.648844     87.303830     40.437456
std       13.640433  1.055500e+05       2.572720   7385.292085    402.960219     12.347429
min       17.000000  1.228500e+04       1.000000      0.000000      0.000000      1.000000
25%       28.000000  1.178270e+05       9.000000      0.000000      0.000000     40.000000
50%       37.000000  1.783560e+05      10.000000      0.000000      0.000000     40.000000
75%       48.000000  2.370510e+05      12.000000      0.000000      0.000000     45.000000
max       90.000000  1.484705e+06      16.000000  99999.000000   4356.000000     99.000000
"""

print(df_train.describe(include='all'))

"""
 age workclass        fnlwgt education  ...  capital_loss    hours_week native_country  label
count   32561.000000     32561  3.256100e+04     32561  ...  32561.000000  32561.000000          32561  32561
unique           NaN         9           NaN        16  ...           NaN           NaN             42      2
top              NaN   Private           NaN   HS-grad  ...           NaN           NaN  United-States  <=50K
freq             NaN     22696           NaN     10501  ...           NaN           NaN          29170  24720
mean       38.581647       NaN  1.897784e+05       NaN  ...     87.303830     40.437456            NaN    NaN
std        13.640433       NaN  1.055500e+05       NaN  ...    402.960219     12.347429            NaN    NaN
min        17.000000       NaN  1.228500e+04       NaN  ...      0.000000      1.000000            NaN    NaN
25%        28.000000       NaN  1.178270e+05       NaN  ...      0.000000     40.000000            NaN    NaN
50%        37.000000       NaN  1.783560e+05       NaN  ...      0.000000     40.000000            NaN    NaN
75%        48.000000       NaN  2.370510e+05       NaN  ...      0.000000     45.000000            NaN    NaN
max        90.000000       NaN  1.484705e+06       NaN  ...   4356.000000     99.000000            NaN    NaN
 """

conti_features = []
for i in CONTI_FEATURES:
    position = df_train.columns.get_loc(i)
    conti_features.append(position)
print(conti_features)

"""
[0, 2, 4, 10, 11, 12]
 """
