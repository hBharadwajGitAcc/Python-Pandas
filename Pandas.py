import pandas as pd
import numpy as np

data = pd.read_csv("C:\\Users\\user\\Downloads\\insurance.csv")

data.head(5)
data.tail(5)


data.shape
data.info()


data.describe()


data.columns
data = data.rename(columns={"bmi": "Body_Mass_Index"})
data.columns


data1 = data[["age","children","charges"]]
data1.corr()
np.corrcoef(data1)


data.index
insurance_random_set = data.iloc[500:1001, [1,3,5]]
insurance_random_set2 = data.loc[500:1001, ['sex','children', 'region']]


insurance = data.sort_values(ascending = False, by = 'age')

