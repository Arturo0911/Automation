#!/usr/bin/python3

import numpy as np
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import seaborn as sns




"""
@author Arturo Negreiros Samanez
"""

PATH = "practices/netflix_titles.csv"




def duration_filter(duration):

    return int(duration.split(" ")[0]) <= 100




def main():
    
    netflix = pd.read_csv(PATH)
    headers = list()
    rating = list()
    for x in netflix:
        headers.append(x)
    


    for y in netflix['rating']:

        if y not in rating:
            rating.append(y)


    print("""

        The headeres:

        'show_id'           'type'          'title'         'director'
        'cast'              'country'       'date_added'    'release_year'
        'rating'            'duration'      'listed_in'     'description'
        

        Rating or classification about the content:
                
        NR & UR         Not rated or Un rated, generally is
                            because, the content of the film
                            was not shiped with the classification propertly
                            and the actual content would be not propertly to
                            childrens

        TV-PG           Guidance Parental suggested
        TV-Y7           Children Public for 7 years old
        TV-Y            Children Public, under 6 years old
        G               General Audience
        TV-G            General Audience 
        PG              Parental Guidance Suggested
        PG-13           Parents Strongly Cautioned
        R               Restricted
        NC-17           Adults Only
        TV-MA           Olders than 17
        TV-14           Olders than 14 Parental Guidance Suggested
        TV-Y7-FV        Chill audience with fiction violence and strongs emotions

        Type:

        Tv-Show or Movie
    """)
    
    print("""
    Setting some filters about the rating for olders than 17 years old
    generating filters for the country => Unieted States
    Type movie""")

    print(netflix[(netflix['country'] == 'United States') & (netflix['type'] == 'Movie') & (netflix['rating'] == 'R') & (netflix['duration'].apply(lambda x: duration_filter(x)) )][['title','rating','duration']])



def review_data():

    netflix = pd.read_csv("practices/netflix_titles.csv")
    
    #sns.pairplot(netflix, hue="type")
    #plt.show()
    #print(netflix)
    
    def filter(title):

        return "murder" in title.lower().split(" ")



    data_frame = netflix[(netflix['title'].apply(lambda x:filter(x))) & (netflix['country'] =='United States')   ][['title', 'release_year', 'rating']]
    print(data_frame)
    #data_frame.plot(x = "release_year", y= "rating", kinkd= "scatter")
    #plt.show()












if __name__ == '__main__':

    #main()
    review_data()







