# The Top Ten List

## Collaborators

* Mike Lygas
* Smita Sharma
* Arjun Subramaniam
* Gretel Uptegrove

## Quick Summary 

Our ETL project provides a pipline for entertainment fans to find the top ten movies, music and books for the year 2018. 
We used movies, from boxofficemjo, music (songs & albums) from Billboard and books from amazon. We took the ratings from amazon and joined them with our other dataset. We checking the data sets to add the attribute to each of our records. For Example, you will see Black Panther ranked at #2 on the box office hits, with a rating of 5 stars.   

Our final dataest model reflects the cleaned top 10 movies, books and music.  We used Monogodb vs SQL to load the databases into a collection and synced up to our html page. The reason we chose to use Mongodb over SQL is for it's faster performance features, such as the read/write scanning for handling data.   


Example:

We provide an ETL pipeline that enables Business Inteligence Analysts at FryCorp Network to determine which shows to promote for 
advertisements. We used Historical TV Show ratings from tv guide, historical viewership metrics from Nielson ratings, 
and show production budgets from Wikipedia. We provide our data in a SQL database which exposes, for the most genres, 
KPIs to determine which genres are underrepresented and could deliver the most value to the FryCorp network if prioritized.

Example steps to run the pipeline:

*Systems requirements*  
Chromedriver must be installeda nd Mongodb installed to local

1. This script will only work for macs natively to work for windows you must change the config.yml file

2. Run `top_ten.py` to import the data to MongoDb
3. View your end result 


## Narrative / Motivation

* We are providing a Database of  Movies ,Music,  &books for consumers to visualize what is the top 10 for the year 2018. 


## Final Schema / Data Model / How to use the data

Explain what the final data model in your database is. 
Why did you make that decision and how do you expect people to use it. 
Entity-Relation diagrams would be great (https://dbdiagram.io/home or other online tools)

## Data Sources

Write a paragraph explaining where you got the data and why you decided to use it. How does it help you solve the problem
in your narrative? 
Dig into (1-2 sentences) into specifics about the data - eg: are there assumptions made in the data you are collecting? 

Example:
We got historical TV Ratings from TV Guide, which allowed us to build KPIs surrounding how popular a show was. 
TV Guide is an aggregation of critic raitings, so the general public is not represented. 
etc. 

## Transformation Step

Explain how you got your raw data into the final model. 
What were the specific steps you had to take to get the data into the final data model. 

Example:
In order to build our final tables, we had to:
* Group the TV Guide ratings by genre and year
* Aggregated on the mean and media rating for each group
* etc. 