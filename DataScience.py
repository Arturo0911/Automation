#!/usr/bin/python3


import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)




#DataFrames




def main():
   

    df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W','X','Y','Z'])
    

    print(df)
    
    """
    print(df['W'])
    print("\n")
    print(df[['W','X']])
    
    df['new'] = df['W'] + df['X']
    
    print(df)
    # When you specify the axis, you truly saying this:
    # the axis 0 is for the 'x' and the axis 1 is for 'y'
    df.drop('new', axis=1, inplace=True)
    print(df)
    print(df.shape)
    

    print("Showing the rows")
    print(df.loc['A'])

    print("passing the numeric position")
    print(df.iloc[2])


    print("printing the intersection between the rows and column")
    print(df.loc['A', 'Z'])

    

    print("implementing the above information, we gonna print using two arguments")
    print(df.loc[['A','B'],['W','Z']])

    """

    
     










if __name__ == '__main__':
    main()
