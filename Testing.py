#!/usr/bin/python3

import numpy as np
import pandas as pd

PATH = "practices/Salaries.csv"
data = pd.read_csv(PATH)

for i in data:
    print(i)

