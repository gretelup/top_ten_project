# The Top Ten List

## Collaborators

* Mike Lygas
* Smita Sharma
* Arjun Subramaniam
* Gretel Uptegrove

## Quick Summary 

Our ETL project provides a pipline for entertainment fans to find the top ten movies and music for the year 2018. 
We used movies, from boxofficemjo, music (songs & albums) from Billboard and Amazon. We took the ratings from amazon and joined them with our other dataset. We checking the data sets to add the attribute to each of our records. For Example, you will see Black Panther ranked at #2 on the box office hits, with a rating of 5 stars.   

Our final dataest model reflects the cleaned top 10 movies defined by dox office sales,  music defined as number of albums sold.  We used Monogodb vs SQL to load the databases into a collection and synced up to our html page. The reason we chose to use Mongodb over SQL is for it's faster performance features, such as the read/write scanning for handling data.   

## Steps to run the pipeline:

*Systems requirements*  
Chromedriver must be installeda nd Mongodb installed to local

1. This script will only work for macs natively to work for windows you must change the config.yml file
2. Run `top_ten.py` to import the data to MongoDb
3. View your end result 


## Narrative / Motivation

* We are providing a Database of Movies and Music for consumers to visualize what is the top 10 for the year 2018. 


## Final Schema / Data Model / How to use the data

Explain what the final data model in your database is. 
Why did you make that decision and how do you expect people to use it. 
Entity-Relation diagrams would be great (https://dbdiagram.io/home or other online tools)

## Data Sources

We got Movie Box office rankings from Boxofficemojo.com, which allowed us to build and clean a data table of the Top 10 movies for 2018.
Boxofficemojo is a database of movie rankings based on box office sales the databse is affilated with IMDB and is available  for the general public. 

We got our Music data of Albums from Billboard.  Billboard is used to convey the popularity of music albums or artists in the music industry.  From Billbaord we got out top 10 albums and songs for 2018. 

We used Amazon to obtain the ratings for the movies and music.  We chose Amazon because it has the same rating system for movies and music so we keep everything consistent. 
 

## Transformation Steps

Explain how you got your raw data into the final model. 
In order to build our final tables, we had to:

* First we ran necessary pip installs for splinter, Beautiful soup, jinja,and pymongo
* After pip installs we created jupyter notebooks in order clean the data for the movies and music
* Once the data has been cleaned in the notebooks we converted the notebooks into python scripts with Mongodb connection in order to pipeline into the database
* After our three scripts were written we consolidated them into one working python script that pipelined the data into the database. 