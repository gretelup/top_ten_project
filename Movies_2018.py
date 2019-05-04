import bs4
from bs4 import BeautifulSoup
import requests as rq
import re
import pandas as pd
import numpy as np
import datetime 
import os
import math
import pymongo



def movie_scrape():
    """
    Gets all box office data for 2018 from boxofficemojo.com
    """
    # Query webpage and create a soup object
    response = rq.get("https://www.boxofficemojo.com/yearly/chart/?yr=2018&p=.htm")
    soup = BeautifulSoup(response.text,'html.parser')
    
    #Get the table with box office data ### 
    soup_table = soup.find_all('table')[6]

    #Get the rows within that table
    soup_movies = soup_table.find_all("td")

    # Pull the data from the soup object and put into a list
    data = []
    for i in soup_movies:
        if i.find('a')!=None:
            data.append(i.find('a').contents[0])
        elif i.find('font')!=None:
            data.append(i.find('font').contents[0])
        elif i.find('b')!=None:
            data.append(i.find('b').contents[0])
            ### Still a <b> tag left for <font> tags ## 
    data=[a.contents[0] if type(a)!=bs4.element.NavigableString else a for a in data]
    
    ### Strip special characters ### 
    data=[re.sub('[^A-Za-z0-9-. ]+', '', a) for a in data]
    
    ### Fill NaNs ### 
    data=[np.nan if a =='na' else a for a in data]

    ##########HERE IS WHERE IT GETS MESSED UP
 #   return_df = pd.DataFrame(data, columns = ['bo_year_rank','title','studio'])

 #   return(return_df) 
#dirtymovies_df = movie_scrape()
#print(dirtymovies_df)


# #create new dataframe for top 10 
# toptenmovies_df = dirtymovies_df[:-295]

# ##clean new dataframe for top 10 by removing rows domestic-pct, overseas-pct
# toptenmovies_df.drop("domestic-pct", axis=1).drop("overseas-pct", axis=1)

# Cleanedtoptenmovies_df= toptenmovies_df.drop("domestic-pct", axis=1).drop("overseas-pct", axis=1) 

# Cleanedtoptenmovies_df.drop("worldwide-gross", axis=1).drop("domestic-gross", axis=1)

# Cleantopdata_df=Cleanedtoptenmovies_df.drop("worldwide-gross", axis=1).drop("domestic-gross", axis=1)

# Cleantopdata_df.drop("overseas-gross", axis=1).drop("bo_year", axis=1)

# Almostcleandata_df = Cleantopdata_df.drop("overseas-gross", axis=1).drop("bo_year", axis=1)

# Almostcleandata_df.rename(columns={'bo_year_rank':'Ranking'}, inplace=True)

# print(Almostcleandata_df)

# # Connect to mongo
# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)

# # Connect to Top 10 database
# db = client.top_10_db

# # If collection books exists, drop it so the new top 10 information will replace it
# db.movies.drop()

# #Create new empty books collection
# movies = db.movies

# # Insert top 10 books/movies/music into database
# data = Cleanedtoptenmovies_df.to_dict(orient='records')
# db.movies.insert_many(data)


