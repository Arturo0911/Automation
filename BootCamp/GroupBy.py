#!/usr/bin/python3

import pandas as pd
import numpy as np
from pprint import pprint

data = {'Company': ['Google', 'Google', 'Microsoft', 'Microsoft', 'Facebook', 'Facebook'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}
df = pd.DataFrame(data)
print("\n")
pprint(data)
print("\n")
print(df)

grouped = df.groupby("Company")
print(grouped)
print("\n")
print(grouped.mean())
print('\n')
print(grouped.std())
print("\n")
print(grouped.sum())

print("\n", grouped.describe().transpose())

