# Import Dependencies
import re
from datetime import datetime
from splinter import Browser
import yaml
import pymongo
import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup as bs
import numpy as np


def movie_scraper(year):
    """Scrapes www.boxofficemojo.com for the top ten movies for
    given year based on revenue.
    Returns a list of dictionaries with year, rank, movie title, and studio.
    """

    # Get webpage data using requests
    response = requests.get(
        "https://www.boxofficemojo.com/yearly/chart/?view2=worldwide&yr=%s&p=.htm"
        % year)

    # Parse HTML using Beautiful Soup
    soup = bs(response.text, "html.parser")

    # Find location of necessary data in soup object
    soup_tables = soup.find_all("table")
    soup_elements = soup_tables[3].find_all("td")

    # For each td element, find and store data in a list
    movie_data = []

    for i in soup_elements:
        if i.find("a") is not None:
            movie_data.append(i.find("a").contents[0])
        elif i.find("font") is not None:
            movie_data.append(i.find("font").contents[0])
        elif i.find("b") is not None:
            movie_data.append(i.find("b").contents[0])

    # Clean Data:

    # Remove extraneous tags
    movie_data = [a.contents[0] if not isinstance(
        a, bs4.element.NavigableString) else a for a in movie_data]

    # Strip special characters
    movie_data = [re.sub("[^A-Za-z0-9-. ]+", "", a) for a in movie_data]

    # Fill NaNs
    movie_data = [np.nan if a == "na" else a for a in movie_data]

    # Set first 6 elements as column headers
    to_df = movie_data[6:]

    # Define the column names
    columns = ["rank", "title", "studio", "", "", "", "", ""]

    # Convert to dataframe
    nrow = int(len(to_df) / len(columns))
    dirty_movies_df = pd.DataFrame(
        np.array(to_df).reshape(
            nrow, 8), columns=columns)

    # Clean dataframe
    dirty_movies_df = dirty_movies_df.iloc[:, 0:3]
    dirty_movies_df["rank"] = dirty_movies_df["rank"].apply(int)
    dirty_movies_df["year"] = year
    movies_df = dirty_movies_df.loc[dirty_movies_df["rank"] <= 10, :]

    # Convert dataframe to list of dictionaries
    movie_dicts = movies_df.to_dict(orient="records")

    print("Movies Scraped from BoxOfficeMojo.")

    return movie_dicts


def process_chart(data, year):
    """ Use the Python package for parsing HTML.
    Calls and receives HTML as strings to process for artists.
    """

    # Create soup object to parse the html
    soup = bs(data, "html5lib")

    # Create a list to return
    list_albums = []

    # Inspect parsed html
    # For each article item, loop and identify tags to extract from.
    # For each entry, add a dictionary to the album list

    for item in soup.select("article"):
        rank = int(item.select_one(".ye-chart-item__rank").string.strip())
        title = item.select_one(".ye-chart-item__title").string.strip()
        artist = item.select_one(
            ".ye-chart-item__artist").text.replace("\n", "")
        list_albums.append({"rank": rank, "title": title,
                            "artist": artist, "year": year})

    return list_albums


def album_scraper(year):
    """Scrapes www.billboard.com for the top ten albums for given year
    based on album revenue.
    Returns a list of dictionaries with rank, album title, artist name,
    and year.
    """

    all_albums = []

    # Use requests library to get HTML
    url = requests.get(
        "https://www.billboard.com/charts/year-end/" +
        str(year) +
        "/top-billboard-200-albums")

    # Parse content and create list of dictionaries using process_chart
    # function
    data = url.content
    all_albums = process_chart(data, year)

    # Filter just the top 10 albums and insert into final list of dictionaries
    album_dicts = []
    for album in all_albums:
        if album["rank"] < 11:
            album_dicts.append(album)

    print("Albums Scraped from Billboard.")

    return album_dicts


def metacritic_movie_scraper(url):
    """Scrapes given metacritic.com url for the movie review information.
    Returns a dictionary with number of user reviews, average user review,
    number of critic reviews, and critic score
    """

    # Use splinter to get website information
    with Browser("chrome", **executable_path, headless=True) as browser:
        browser.visit(url)

        # Create a timestamp
        now = datetime.now()
        scrape_time = now.strftime("%Y-%m-%d %H:%M:%S")

        # Use beautiful soup to parse html
        soup = bs(browser.html, "html.parser")

    try:
        # Find number of reviews from users and critics
        rev_count_strings = soup.find_all("span", class_="based_on")
        user_rev_count = int(rev_count_strings[1].text.split(" ")[2])
        critic_rev_count = int(rev_count_strings[0].text.split(" ")[2])

        # Find review average from users and rating score from critics
        review_soup = soup.find_all("a", class_="metascore_anchor")
        user_rev_avg = float(review_soup[1].text)
        critic_rev_score = float(review_soup[0].text)

    # If page does note have review information, population review information
    # with None values
    except (IndexError, AttributeError):
        user_rev_count = None
        critic_rev_count = None
        user_rev_avg = None
        critic_rev_score = None

    # Return dictionary of book information
    movie_dict = {
        "user_rev_count": user_rev_count,
        "user_rev_avg": user_rev_avg,
        "critic_rev_count": critic_rev_count,
        "critic_rev_score": critic_rev_score,
        "scrape_time": scrape_time}
    return movie_dict


def metacritic_album_scraper(url):
    """Scrapes given metacritic.com url for the album review information.
    Returns a dictionary with number of user reviews, average user review,
    number of critic reviews, and critic score
    """

    # Use splinter to get website information
    with Browser("chrome", **executable_path, headless=True) as browser:
        browser.visit(url)

        # Create a timestamp
        now = datetime.now()
        scrape_time = now.strftime("%Y-%m-%d %H:%M:%S")

        # Use beautiful soup to parse html
        soup = bs(browser.html, "html.parser")

    try:
        # Find number of reviews from users and critics
        rev_count_strings = soup.find_all("span", class_="count")
        user_rev_count_string = rev_count_strings[1].find(
            "a").text.replace("\n", "")
        user_rev_count = int(
            " ".join(
                user_rev_count_string.split()).split(" ")[0])
        critic_rev_count_string = rev_count_strings[0].find(
            "a").text.replace("\n", "")
        critic_rev_count = int(
            " ".join(
                critic_rev_count_string.split()).split(" ")[0])

        # Find review average from users and rating score from critics
        review_soup = soup.find_all("a", class_="metascore_anchor")
        user_rev_avg = float(review_soup[1].text)
        critic_rev_score = float(review_soup[0].text)

    # If page does note have review information, population review information
    # with None values
    except (IndexError, AttributeError):
        user_rev_count = None
        critic_rev_count = None
        user_rev_avg = None
        critic_rev_score = None

    # Return dictionary of album information
    album_dict = {
        "user_rev_count": user_rev_count,
        "user_rev_avg": user_rev_avg,
        "critic_rev_count": critic_rev_count,
        "critic_rev_score": critic_rev_score,
        "scrape_time": scrape_time}
    return album_dict


def make_url_string(string):
    """Takes a string and returns a string to be inserted in url"""

    url_string = string.replace("(", "").replace(")", "").replace("÷", "")\
        .replace("&", "").replace("-", "").    replace("  ", " ")\
        .replace(" ", "-").lower()
    if url_string.startswith("-"):
        url_string = url_string[1:]
    if url_string.endswith("-"):
        url_string = url_string[: -1]

    return url_string


def valid_year(year):
    """Takes a string "year" as a parameter.
    Returns boolean True if it is a valid year from 2008-2018.
    Prints error message and returns boolean False if it is not.
    """

    if not str.isdigit(year):
        print(f"Oops! {year} is not a number!")
        return False
    elif int(year) < 2008 or int(year) > 2018:
        print(f"Oops! {year} is not a year between 2008-2018!")
        return False
    else:
        return True


def user_query():
    """Queries user for year they would like to scrape"""

    year = (
        input("Please enter the year from 2008-2018 you would like to get data for: "))

    # Check to make sure year is valid
    while not valid_year(year):
        year = (
            input("Please enter the year from 2008-2018 you would like to get data for: "))

    year = int(year)
    return year

##############################################################################
#  Main Function
##############################################################################


# Set up path for chromedriver
with open("config.yml", "r") as ymlpath:
    config = yaml.safe_load(ymlpath)
    executable_path = {"executable_path": config["config-key"]}

# Connect to mongo using pymongo to create local database
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)


# Connect to Top 10 database
db = client.top_10_db

# Connect to movies and albums collection
movies = db.movies
albums = db.albums

# Query user for year they would like to get data for
year = user_query()

# Check to see if year has already been scraped
movie_doc = db.movies.find_one({"year": year})
while movie_doc is not None:
    print(f"Data already scraped for {year}.")
    year = user_query()
    movie_doc = db.movies.find_one({"year": year})

print(f"Scraping data for year {year}...")

# Scrape BoxOfficeMojo and Billboard Music for a list of dictionaries of
# the top 10 movies for given year
movie_BOM_dicts = movie_scraper(year)
album_Bill_dicts = album_scraper(year)

# Add review information from Metacritic to new list of dictionaries for
# top movies
movie_dicts = []
print("Scraping movie reviews...")
for movie in movie_BOM_dicts:

    # Create query url from dictionary values
    movie_query = make_url_string(movie["title"])
    movie_url = f"https://www.metacritic.com/movie/{movie_query}/details"

    # Add review information to dictionary
    movie_dicts.append({**movie, **metacritic_movie_scraper(movie_url)})
    print(f"{movie['title']} scraped.")

# Add review information from Metacritic to new list of dictionaries for
# top music albums
album_dicts = []
print("Scraping album reviews...")
for album in album_Bill_dicts:
    # Create query url from dictionary values
    title_query = make_url_string(album["title"])
    artist_query = make_url_string(album["artist"])
    album_url = f"https://www.metacritic.com/music/{title_query}/{artist_query}"

    # Add review information to dictionary
    album_dicts.append({**album, **metacritic_album_scraper(album_url)})
    print(f"{album['title']} scraped.")

# Insert movies and albums into database
movies = db.movies.insert_many(movie_dicts)
print(f"Movies for {year} entered into database.")
albums = db.albums.insert_many(album_dicts)
print(f"Albums for {year} entered into database.")
print(f"Huzzah!")
