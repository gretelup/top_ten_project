# Dependencies and Setup
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pymongo

def book_scraper(url):
    
    """Scrapes given Amazon url for the book review information.
    Returns a dictionary with full title, boolean indicating if reviews are available, 
    and review number and rating if so. If reviews are not available, review number and rating are set to None.
    
    N.B. Must use splinter as requests returns a 504 error"""
    
    # Open Amazon book url using Splinter  
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    
    with Browser("chrome", **executable_path, headless=True) as browser:
        browser.visit(url)

        # Create Beautiful soup object
        soup = bs(browser.html, "html.parser")
        
        # Get full title
        title = soup.find("span", id="ebooksProductTitle").text.replace("\n","").replace("  ", "")
        
        # Determine if Review information is available. 
        # If not, set rev_available to False and enter None for review information
        # If yes, set rev_available to True and enter review information
        rev_count_string = soup.find("span", id="acrCustomerReviewText")
        if (rev_count_string == None):
            rev_available = False
            rev_count = None
            rev_avg = None
        else:
            rev_available = True
            rev_count = int(rev_count_string.text.split(" ")[0].replace(",", ""))
            rev_avg_string = soup.find("span", class_="arp-rating-out-of-text a-color-base").text
            rev_avg = float(rev_avg_string.split(" ")[0])
            
        # Return dictionary of book information
        book_dict = {"title": title, "rev_available": rev_available, "rev_count": rev_count, "rev_avg": rev_avg}
        return(book_dict)

def az_scraper(x):

    """Scrapes Amazon.com website for the book rated x on the Amazon Top 50 
    best selling paid ebooks, updated hourly.
    Returns dictionary of book information with title, primary author, amazon book url, 
    whether reviews are available, total number of reviews, a review score, and link to book image"""
    
    # Set rank of book
    rank = x+1
    
    # Use requests to get HTML from amazon
    url = 'https://www.amazon.com/Best-Sellers-Kindle-Store-eBooks/zgbs/digital-text/154606011/ref=zg_bs_unv_kstore_2_3511261011_1'
    response = requests.get(url)
    content = response.content

    # Create Beautiful soup object
    soup = bs(content, "html.parser")

    # Create Beautiful soup object for specified book
    book_soup = soup.find_all("span", class_="aok-inline-block zg-item")[x]

    # Get book author (note: only primary author is listed)

    try:
        author = book_soup.find("a", class_="a-size-small a-link-child").text
    except AttributeError:
        author = book_soup.find("div", class_="a-row a-size-small").find("span").text

    # Get book url
    book_href = book_soup.find("a")["href"]
    url = f"https://www.amazon.com{book_href}"

    # Get URL for book image
    img_url = book_soup.find("img")["src"]

    # Return dictionary of book information
    book_dict = {**book_scraper(url), **{"rank": rank, "author": author, "url": url, "img_url": img_url}}
    return(book_dict)

def top_book_scraper():

    """Scrapes Amazon.com website for top 10 bestselling paid ebooks, updated hourly. 
    Creates collection "books" in top 10 database with title, primary author, amazon url, 
    whether reviews are available, total number of reviews, review score, 
    and link to book image for each book
    
    Notes: Includes pre-orders which mostly do not have reviews.
    Includes only primary author if book has multiple authors"""

    # Connect to mongo
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # Connect to Top 10 database
    db = client.top_10_db
    
    # If collection books exists, drop it so the new top 10 information will replace it
    db.books.drop()
    
    #Create new empty books collection
    books = db.books
    
    # Insert top 10 books into database
    for x in range(10):
        db.books.insert_one(az_scraper(x))

top_book_scraper()