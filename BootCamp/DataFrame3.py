#!/usr/bin/python3


import numpy as np
import pandas as pd
from numpy.random import randn


def main():
    # Index Levels
    outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
    inside = [1, 2, 3, 1, 2, 3]
    her_index = list(zip(outside, inside))
    her_index = pd.MultiIndex.from_tuples(her_index)
    df = pd.DataFrame(randn(6, 2), her_index, ['A', 'B'])
    print(df)

    print("\n")

    print(df.loc['G1'])
    print(df.loc['G1'].loc[1])

    df.index.names = ['Group', 'Name']
    print("\n")
    print(df)
    print("\n")

    d = {'A': [1, 2, np.nan], 'B': [2, np.nan, np.nan], 'C': [5, 6, 7]}

    data_frame = pd.DataFrame(d)
    print(data_frame)
    print()
    print("\n")

    print(data_frame.dropna(axis=0))
    print("\n")
    print(data_frame.dropna(axis=1))
    print("\n")
    print(data_frame.fillna("Arturo"))

    print(data_frame.dropna(axis=1))
    print(data_frame.dropna(axis=1).mean())



if __name__ == '__main__':
    main()
