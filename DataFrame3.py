#!/usr/bin/python3


import numpy as np
import pandas as pd


def main():
    # Index Levels
    outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
    inside = [1, 2, 3, 1, 2, 3]
    her_index = list(zip(outside, inside))
    print(her_index)
    her_index = pd.MultiIndex.from_tuples(her_index)
    print(her_index)


if __name__ == '__main__':
    main()
