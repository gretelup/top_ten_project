# Import dependencies
from flask import Flask, render_template, redirect
import pymongo
import book_scraping
# ADD NAMES OF MOVIE AND MUSIC ET SCRIPTS


# Create an instance of Flask
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)
db = client.top_10_db

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Call each function to insert most recent top 10 data into mongo db

    # Extract data from database and render it in index.html


if __name__ == "__main__":
    app.run(debug=True)
