#!/usr/bin/python3


import numpy as np
import pandas as pd
from numpy.random import randn
from pprint import pprint

np.random.seed(101)

# DataFrames
""" using DataFrame is necessary ship a dictionary with all the data inside, 
    the labels gonna be the marks in the rows.
"""


def main():
    exam_data = {'name':
                     ['Anastasia', 'Diana', 'Katherine', 'James',
                      'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    new_data = pd.DataFrame(exam_data, labels)

    pprint(new_data)
    print(type(new_data))
    print(new_data.info)


if __name__ == '__main__':
    main()
