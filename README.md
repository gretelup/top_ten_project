# The Top Ten List

## Collaborators

* Mike Lygas
* Smita Sharma
* Arjun Subramaniam
* Gretel Uptegrove

## Summary 

Our ETL project provides a pipline for entertainment fans to find the top ten movies, based on gross box office sales, and top albums--based on units sold. Rating information from critics and users is also provided for each item. For example, a single record will show you that the movie Black Panther is ranked at #2 in 2018 based on box office gross with a a critic rating of [] out of 100 based on [] critical reviews and a user rating of [insert user rating] out of 10 based on [insert number of reviews].
#[Gretelnote: make sure to insert appropriate rating information in above and to change as appropriate if we decide not to include multiple years and critical review information]

## Steps to run the pipeline:

1. Run mongod. The script will open a local connection.
2. If running on MacOS, no configuration changes are needed. To run on Windows, change the chromedriver path in the config.yml file.
2. Run `top_ten.py` to import the data to a local mongo database.
3. View your end result 

## Narrative

We wanted to create a database that reflects entertainment in popular culture over the last decade. We focused on music and movies, as those forms of entertainment create large amounts of revenue, and we included rating information to show both popular and critical opinions on entertainment culture.

## How to use the data

Each item is entered as a document in three different collections--movie, music album, and song--in a mongo database. Each document in the collection includes year, rank in that year, title, studio name/artist name, user rating, number of user reviews, critic rating, and number of critical reviews.

The reason we chose to use Mongo over SQL is for it's faster performance features, such as the read/write scanning for handling data, and flexibility for adding additional data at a later date.
# [Gretelnote: I feel like the above is a little weak, but I can't really think of anything better to say] .  MongoDB handles unstructured data and has integration with analytical tools such as Spark and Power BI.

This database can be used to see what sorts of entertainment are popular and profitable over time and how both users and critics feel about them.
# [Gretelnote: I feel like the above is a little weak and could be more robust]

## Schema

# [Gretelnotes: see how this looks when published. Needs to be populated and maybe add more words?]
```
top_10_db.movies:
{
	_id: int # unique ObjectID assigned by mongodb
	movie_year: int # Year movie was released
	rank: int # Rank of movie
	movie_title: string # Title of movie
	etc.
}

top_10_db.albums:
{
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



## Data Sources

We gathered movie ranking data from Boxofficemojo.com, which reports box-office revenue. It is affiliated with IMDb and is available for general public use.
 
We gathered music ranking data for albums and songs from Billboard.com, which reports popularity of music albums or artists in the music industry based on sales.

For each movie and album we gathered rating information from Metacritic.com. Metacritic aggregates critical reviews for various types of entertainment and summarizes them into a single score from 0-100. It also provides a platform for users to provide ratings from 0-10 as well. We used this as it provides consistent review information across movies and music. Metacritic gathers data from multiple sources, which can be viewed at: [https://www.metacritic.com/faq#item12].

## Transformation Steps
# GRETELNOTE- EVERYONE NEEDS TO UPDATE THE STEPS THEY USED; I used what I understand from Arjun's and Smita's script, but they need to be updated

* We ran necessary pip installs for splinter, Beautiful soup, and pymongo.
* We created four separate jupyter notebooks to develop our python code:
    * Movie notebook (Arjun):
        * Used requests module to get content from boxofficemojo.com.
        * Used Beautiful Soup to parse content.
        * Cleaned data by stripping special characters.
        * Entered data into dataframe.
        * Dropped unnecessary columns and rows.
        * Converted dataframe into a list of dictionaries.
    * Music notebook (Mike):
	* Used requests module to get content from Billboard.com.
        * Used Beautiful Soup to parse content.
        * Filtered out unnecessary rows 
        * Added timestamp to each record
        * Created a list of dictionaries        * 
    * Metacritic notebook (Smita):
        * Takes a dictionary from the movie, album, or song list of dictionaries.
        * Used Splinter to create a browser object to gather content from associated metacritic page.
        * Used Beautiful Soup to parse content.
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
* After extensive testing, we exported the final script notebook into a single python script called top_ten.py.