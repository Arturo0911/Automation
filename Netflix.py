#!/usr/bin/python3

import numpy as np
import pandas as pd



"""
@author Arturo Negreiros Samanez
"""

PATH = "practices/netflix_titles.csv"



def main():
    





    """
    The headeres =>
        ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description']
    """
    netflix = pd.read_csv(PATH)
    headers = list()
    rating = list()
    for x in netflix:
        headers.append(x)
    


    for y in netflix['rating']:

        if y not in rating:
            rating.append(y)


    print("""
    Rating information =>
    \n
    ['TV-PG', 'NR', 'TV-G', 'TV-Y', nan, 'TV-Y7','TV-Y7-FV', 'UR']

    G               General Audience
    TV-G            General Audience 
    PG              Parental Guidance Suggested
    PG-13           Parents Strongly Cautioned
    R               Restricted
    NC-17           Adults Only
    TV-MA           Olders than 17
    TV-14           Olders than 14 Parental Guidance Suggested
    TV-Y7-FV        Chill audience with fiction violence and strongs emotions
    """)
    
    print(rating)
    print(netflix[(netflix['type'] == 'Movie') & (netflix['country'] == "United States")][['title', 'country', 'rating', 'duration']])




if __name__ == '__main__':

    main()
