#Declare Dependencies
from bs4 import BeautifulSoup
import jinja2
import requests
import pymongo
import pandas as pd
from datetime import datetime

#Setting variable for time
current_time = datetime.now()

#Inspect Billboard web.  Capture specific years and artists as lists.
years = [2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]

all_songs = []
all_songs_objects = []

#Use the Python package for parsing HTML.  Calls and receives HTML as strings to process for artists.
def process_chart(htmldata, year):
    soup = BeautifulSoup(data,"html5lib")
    list_songs = []

#Inspect document and for each item in article loop and identify tags to extract from. 
    for item in soup.select('article'):
        rank = item.select_one(".ye-chart-item__rank").string.strip()
        image = item.select_one(".ye-chart-item__image").find("img").get("src")
        title = item.select_one(".ye-chart-item__title").string.strip()
        artist = item.select_one(".ye-chart-item__artist").text
        list_songs.append({'rank':rank,'image':image,'title':title, 'artist':artist, 'year':year, 'current_time':current_time})
        all_songs_objects.append({'rank':rank,'image':image,'title':title, 'artist':artist,'year':year,'current_time':current_time })
    return list_songs
   
#For each item in the Year list, loop thru, append to url and create records by year
for year in years:

    url = requests.get("https://www.billboard.com/charts/year-end/"+str(year)+"/hot-100-songs")
    data = url.content
    all_songs.append(process_chart(data,year))

# Connect to mongo
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Connect to Top 10 database
db = client.top_10_db

# If collection music exists, drop it so the new top 10 information will replace it
db.songs.drop()

# #Create new empty music-artists collection
db.create_collection("songs")
mycol = db["songs"]

#List Top10
top_ten = []
for rank10 in all_songs_objects:
   if int(rank10.get("rank")) < 11:
       top_ten.append(rank10)

x = mycol.insert_many(top_ten)
