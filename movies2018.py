#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '../../../top_ten_project'))
	print(os.getcwd())
except:
	pass

#%%
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


#%%
def convdollar(x):
    """
    Just a parsing function converting 2.5k to 2500, 1mil to 1000000
    """
    if 'k' in x:
        return float(x.replace('k',''))*1000
    else:
        return float(x)*1000000


#%%
millnames = ['',' Thousand',' Million',' Billion',' Trillion']

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])


#%%
def scrape():
    """
    Gets all box office data from 2018 to present from boxofficemojo.com
    """
    years=[str(a) for a in range(2018,2019)]
    df_list=[]
    for year in years:
        r=rq.get('https://www.boxofficemojo.com/yearly/chart/?view2=worldwide&yr=%s&p=.htm' % year)
        print('Box Office data for %s scraped' % year)
        p=BeautifulSoup(r.text,'html.parser')
            ### Look for the table ### 
        b=p.find_all('table')
        
        ### Usually the fourth table object on page ### 
        tb=b[3].find_all('td')
         ## Each data field is found in a <td> element in the fourth table. Store all data in a list ## 
        data=[]
        for i in tb:
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
        
        ### Define the feature names ###
        columns=['bo_year_rank','title','studio','worldwide-gross','domestic-gross','domestic-pct','overseas-gross','overseas-pct']
        
        ### First 6 elements are column headers # 
        to_df=data[6:]
        
        ### Escape clause in case the layout changes from year to year ### 
        if len(to_df)%len(columns) != 0:
            print('Possible table misalignment in table for year %s' % year)
            break
            
            ### Convert to pandas dataframe ### 
        
        nrow=int(len(to_df)/len(columns))
        df=pd.DataFrame(np.array(to_df).reshape(nrow,8),columns=columns)
        df[['worldwide-gross','domestic-gross','overseas-gross']]=df[['worldwide-gross','domestic-gross','overseas-gross']].applymap(lambda x:convdollar(x))
        df['bo_year']=int(year)
        df_list.append(df)

        main=pd.concat(df_list)
    
        # Store data into csv # 
        #main.to_csv(os.path.join("output","current_boxoffice_mojo.csv"))
        return (main)
        print (main)
  


#%%
if __name__ == "__main__": 

    dirtymovies_df=scrape()


#%%
dirtymovies_df


#%%
## Cleaning data by dropping the unessery rows (10-87) drops the bottom 78 trows
dirtymovies_df[:-295]


#%%
#create new dataframe for top 10 
toptenmovies_df = dirtymovies_df[:-295]


#%%
toptenmovies_df


#%%
##clean new dataframe for top 10 by removing rows domestic-pct, overseas-pct
toptenmovies_df.drop("domestic-pct", axis=1).drop("overseas-pct", axis=1)


#%%
Cleanedtoptenmovies_df= toptenmovies_df.drop("domestic-pct", axis=1).drop("overseas-pct", axis=1) 


#%%
Cleanedtoptenmovies_df

#%% [markdown]
#   if x is >= 1000000000 then convert to "1.xx billion"  to make more readable we are going from float to string 
#   else convert to xxxmillion 
#   
#   Next steps for arjun figure out function above then put finished dataframe into mongodbcollection 
#   

#%%
# Connect to mongo
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Connect to Top 10 database
db = client.top_10_db

# If collection books exists, drop it so the new top 10 information will replace it
db.movies.drop()

#Create new empty books collection
movies = db.movies

# Insert top 10 books/movies/music into database
data = Cleanedtoptenmovies_df.to_dict(orient='records')
db.movies.insert_many(data)


#%%



