#!/usr/bin/python3


import pandas as pd
import numpy as np


df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})

print("\n")
print(df)
print("\n")
print(df.head())