#!/usr/bin/python3

import numpy as np
import pandas as pd

PATH = "practices/Salaries.csv"


data = pd.read_csv(PATH,low_memory=False)
#print(data.info())


# Calculating the base pay


print(data.head(2))

data.dropna(inplace= True)
print(data.info())

print(data['BasePay'])
print(data['BasePay'].mean())

"""
print("\n")
#print(data['BasePay'].std())
print("\n")
#print(data['BasePay'].sum())
"""