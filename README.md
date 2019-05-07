# The Top Ten List

## Collaborators

* Mike Lygas
* Smita Sharma
* Arjun Subramaniam
* Gretel Uptegrove

## Summary 

<<<<<<< HEAD
Our ETL project provides a pipline for entertainment fans to find the top ten movies, based on gross box office sales, and music albums based on number sold. The user can query based on year for 2008-2018. Rating information from critics and users is also provided for each item. For example, a single record will show you that the movie Black Panther from BV studio is ranked at #2 in 2018 based on box office gross with a user review average of 6.5 out of 10 and a critic score of 88 out of 100 based on 55 reviews. A timestamp reflecting when reviews were scraped is included.

## System Requirements
* Chrome Web Browsr
* Chromedriver
* MongoDB
* Python environment running Python 3.7 with the following installations:
    * beatufiulsoup4
    * numpy
    * pandas
    * pymongo
    * requests
    * splinter
    * yaml
||||||| merged common ancestors
Our ETL project provides a pipline for entertainment fans to find the top ten movies, based on gross box office sales, and music--both top albums and top songs--based on number sold. Rating information from critics and users is also provided for each item. For example, a single record will show you that the movie Black Panther is ranked at #2 in 2018 based on box office gross with a a critic rating of [] out of 100 based on [] critical reviews and a user rating of [insert user rating] out of 10 based on [insert number of reviews].
#[Gretelnote: make sure to insert appropriate rating information in above and to change as appropriate if we decide not to include multiple years and critical review information]
=======
Our ETL project provides a pipline for entertainment fans to find the top ten movies, based on gross box office sales, and top albums--based on units sold. Rating information from critics and users is also provided for each item. For example, a single record will show you that the movie Black Panther is ranked at #2 in 2018 based on box office gross with a a critic rating of [] out of 100 based on [] critical reviews and a user rating of [insert user rating] out of 10 based on [insert number of reviews].
#[Gretelnote: make sure to insert appropriate rating information in above and to change as appropriate if we decide not to include multiple years and critical review information]
>>>>>>> ba101a4060a5cff443d26c9e253dcc06b8079239

## Steps to run the pipeline:

1. If running on MacOS, no configuration changes are needed. To run on Windows, change the chromedriver path in the config.yml file.
2. Run mongod to open a local connection.
3. Run `top_ten.py`.
4. At the prompt, enter the year between 2008-2018 you would like to scrape data for.
5. A mongo database for the provided year will now be available on a local connection. 

## Narrative

We wanted to create a database that reflects entertainment in popular culture over the last decade. We focused on music and movies, as those forms of entertainment create large amounts of revenue, and we included rating information to show both popular and critical opinions on entertainment culture.

## How to use the data

<<<<<<< HEAD
Each item is entered as a document in two different collections--movie and music album--in a mongo database. Each document in the collection includes year, rank in that year, title, studio name/artist name, user rating, number of user reviews, critic rating, number of critical reviews, and the time the review data was scraped. If review information was not available, review values were populated with null values.
||||||| merged common ancestors
Each item is entered as a document in three different collections--movie, music album, and song--in a mongo database. Each document in the collection includes year, rank in that year, title, studio name/artist name, user rating, number of user reviews, critic rating, and number of critical reviews.
=======
Each item is entered as a document in different collections--movie and music album--in a mongo database. Each document in the collection includes year, rank in that year, title, studio name/artist name, user rating, number of user reviews, critic rating, and number of critical reviews.
>>>>>>> ba101a4060a5cff443d26c9e253dcc06b8079239

<<<<<<< HEAD
The reason we chose to use Mongo over SQL is for it's faster performance features, such as the read/write scanning for handling data, and flexibility for adding additional data at a later date. MongoDB handles unstructured data and has integration with analytical tools such as Spark and Power BI.
||||||| merged common ancestors
The reason we chose to use Mongo over SQL is for it's faster performance features, such as the read/write scanning for handling data, and flexibility for adding additional data at a later date.
# [Gretelnote: I feel like the above is a little weak, but I can't really think of anything better to say] .  MongoDB handles unstructured data and has integration with analytical tools such as Spark and Power BI.

This database can be used to see what sorts of entertainment are popular and profitable over time and how both users and critics feel about them.
# [Gretelnote: I feel like the above is a little weak and could be more robust]
=======
The reason we chose to use Mongo over SQL is for it's faster performance features, such as the read/write scanning for handling data, and flexibility for adding additional data at a later date.
# [Gretelnote: MongoDB benefits include handling unstructured data and integrating with analytical tools such as Spark and BI.

This database can be used to see what sorts of entertainment are popular and profitable over time and how both users and critics feel about them.
# [Gretelnote: I feel like the above is a little weak and could be more robust]
>>>>>>> ba101a4060a5cff443d26c9e253dcc06b8079239

## Schema

```
top_10_db.movies:
{
	_id: int # Unique ObjectID assigned by mongodb
    rank: int # Rank of movie in given year
    title: string # Title of movie
	studio: string # Studio that produced movie
    year: int # Year movie was released
    user_rev_count: int # Number of user reviews
	user_rev_avg: float # Average user review (on scale 0-10)
    critic_rev_count: int # Number of critical reviews score is based on
    critic_rev_score: float # Critic score (on scale 0-100)
    scrape_time: string # Timestamp of when review data was scraped from metacritic
}

top_10_db.albums:
{
<<<<<<< HEAD
	_id: int # Unique ObjectID assigned by mongodb
    rank: int # Rank of album in given year
    title: string # Title of album
    artist: string # Album's artist
	year: int # Year movie was released
    user_rev_count: int # Number of user reviews
	user_rev_avg: float # Average user review (on scale 0-10)
    critic_rev_count: int # Number of critical reviews score is based on
    critic_rev_score: float # Critic score (on scale 0-100)
    scrape_time: string # Timestamp of when review data was scraped from metacritic
{
```

||||||| merged common ancestors
	_id: int # unique ObjectID assigned by mongodb
	album_year: int # Year album was released
	rank: int # Rank of album
	album_title: string # Title of movie
	etc.
{

top_10_db.songs:
{
	_id: int # unique ObjectID assigned by mongodb
	song_year: int # Year album was released
	rank: int # Rank of song
	song_title: string # Title of movie
	etc.
{
```



=======
	_id: int # unique ObjectID assigned by mongodb
	album_year: int # Year album was released
	rank: int # Rank of album
	album_title: string # Title of movie
	etc.
{



>>>>>>> ba101a4060a5cff443d26c9e253dcc06b8079239
## Data Sources

We gathered movie ranking data from Boxofficemojo.com, which reports box-office revenue. It is affiliated with IMDb and is available for general public use.
 
<<<<<<< HEAD
We gathered music ranking data for albums from Billboard.com, which reports popularity of music albums and songs based on sales.
||||||| merged common ancestors
We gathered music ranking data for albums and songs from Billboard.com, which reports popularity of music albums or artists in the music industry based on sales.
=======
We gathered music ranking data for albums from Billboard.com, which reports popularity of music albums in the music industry based on sales.
>>>>>>> ba101a4060a5cff443d26c9e253dcc06b8079239

<<<<<<< HEAD
For each movie and album, we gathered rating information from Metacritic.com. Metacritic aggregates critical reviews for various types of entertainment and summarizes them into a single score, called a metascore, from 0-100. Information on how score is calculated can be viewed at: [https://www.metacritic.com/about-metascores]. It also provides a platform for users to provide ratings from 0-10. We decided to use metacritic as it provides consistent review information across movies and music. Metacritic gathers data from multiple sources, which can be viewed at: [https://www.metacritic.com/faq#item12].
||||||| merged common ancestors
For each movie, album, and song, we gathered rating information from Metacritic.com. Metacritic aggregates critical reviews for various types of entertainment and summarizes them into a single score from 0-100. It also provides a platform for users to provide ratings from 0-10 as well. We used this as it provides consistent review information across movies and music. Metacritic gathers data from multiple sources, which can be viewed at: [https://www.metacritic.com/faq#item12].
=======
For each movie and album we gathered rating information from Metacritic.com. Metacritic aggregates critical reviews for various types of entertainment and summarizes them into a single score from 0-100. It also provides a platform for users to provide ratings from 0-10 as well. We used this as it provides consistent review information across movies and music. Metacritic gathers data from multiple sources, which can be viewed at: [https://www.metacritic.com/faq#item12].
>>>>>>> ba101a4060a5cff443d26c9e253dcc06b8079239

## Transformation Steps

* We ran necessary pip installs.
* We created four separate jupyter notebooks to develop our python code and then converted each notebook into functions to be run by a single master script:
    * Movie scraping script (Arjun):
        * Used requests module to get content from boxofficemojo.com.
        * Used Beautiful Soup to parse content.
        * Cleaned data by stripping special characters.
        * Entered data into dataframe.
        * Added year column.
        * Dropped unnecessary columns and rows.
        * Converted dataframe into a list of dictionaries.
<<<<<<< HEAD
    * Album scraping script (Mike):
	    * Used requests module to get content from Billboard.com.
||||||| merged common ancestors
    * Music notebook (Mike):
	* Used requests module to get content from Billboard.com.
        * Used Beautiful Soup to parse content.
        * Filtered out unnecessary rows 
        * Added timestamp to each record
        * Created a list of dictionaries        * 
    * Metacritic notebook (Smita):
        * Takes a dictionary from the movie, album, or song list of dictionaries.
        * Used Splinter to create a browser object to gather content from associated metacritic page.
=======
    * Music notebook (Mike):
	* Used requests module to get content from Billboard.com.
        * Used Beautiful Soup to parse content.
        * Filtered out unnecessary rows based on rank
        * Added timestamp to each record
        * Created a list of dictionaries        * 
    * Metacritic notebook (Smita):
        * Takes a dictionary from the movie, album, or song list of dictionaries.
        * Used Splinter to create a browser object to gather content from associated metacritic page.
>>>>>>> ba101a4060a5cff443d26c9e253dcc06b8079239
        * Used Beautiful Soup to parse content.
<<<<<<< HEAD
        * Filtered out unnecessary rows. 
        * Created a list of dictionaries.
    * Metacritic scraping script (Smita):
        * For each movie/album dictionary in the provided list of dictionaries from the scraping scripts:
            * Created a url based on provided movie/album data.
            * Used Splinter to create a browser object for that url to gather content from associated metacritic page.
            * Used Beautiful Soup to parse content.
            * If review information was unavailable, populated review variables with null values.
            * Created timestamp reflecting time page was scraped.
            * Added rating data to provided dictionary.
    * Master script (Gretel):
        * Made necessary configurations.
        * Created local connection to MongoDB.
        * Used pymongo to create a new top_ten_db mongo database and movies and albums collections.
        * Created user prompt for year.
        * Checked if information for provided year was already entered into database.
        * Invoked each script to gather data, resulting in two lists of dictionaries.
        * Inserted a document into associated collection from each dictionary in the movies and albums list.
        * Inserted print statements with scraping progress.
    * YAML configuration file (Gretel):
        * Created configuration file specifying path used to connect to Chromedriver.
||||||| merged common ancestors
        * Added rating data to provided dictionary.
    * Final Script notebook (Gretel):
        * Copied python code from each notebook, creating separate functions for each notebook.
            * Used movie function from movie notebook to create a list of dictionaries of movies.
            * Used album function and song function from music notebook to create a list of dictionaries of albums and a list of dictionaries of songs.
            * Used metacritic functions to add rating information to each dictionary in the lists created by the previous functions.
        * After creating a finalized list of dictionaries for movies, albums, and songs, opened a connection to mongodb.
        * Used pymongo to create a new top_ten_db mongo database locally.
        * Created a collection for movies, albums, and songs.
        * Inserted a document in associated collection from each dictionary in the movies, albums, and songs list.
=======
        * Added rating data to provided dictionary.
    * Final Script notebook (Gretel):
        * Copied python code from each notebook, creating separate functions for each notebook.
            * Used movie function from movie notebook to create a list of dictionaries of movies.
            * Used album function and song function from music notebook to create a list of dictionaries of albums and a list of dictionaries of songs.
            * Used metacritic functions to add rating information to each dictionary in the lists created by the previous functions.
        * After creating a finalized list of dictionaries for movies, albums, and songs, opened a connection to mongodb.
        * Used pymongo to create a new top_ten_db mongo database locally.
        * Created a collection for movies and albums
        * Inserted a document in associated collection from each dictionary in movies and albums
>>>>>>> ba101a4060a5cff443d26c9e253dcc06b8079239
* After extensive testing, we exported the final script notebook into a single python script called top_ten.py.