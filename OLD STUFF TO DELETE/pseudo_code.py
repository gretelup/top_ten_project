# Import Dependencies

# Extract Data from Data Source

# Put Data in Pandas Dataframe

# Get rid of unnecessary rows and columns

# Take care of missing values, errant characters, etc.

# Convert/Transform data as is appropriate

# Extract data from dataframe and put into Mongo DB

    # Connect to mongo
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # Connect to Top 10 database
    db = client.top_10_db
    
    ### BELOW: Replace "books" w/ movies or music
    
    # If collection books/movies/music exists, drop it so the new top 10 information will replace it
    # If you don't do this step, when it refreshes, it will append the data instead of replacing it
    
    db.books.drop()
    
    #Create new empty books/movie/music collection
    books = db.books
    
    # Insert top 10 books/movies/music into database
    data = df.to_dict(orient='records')
    db.books.insert_many(data)

# FOR TESTING PURPOSES: Test cleaning the dataframes first and getting them to look right before trying to do anything w/ mongo db
# When you get the df looking good, run the code to insert into mongo and use MongoDB compass to verify it looks right.
# If this code is working correctly, you should be able to run it over and over again, refreshing w/ updated data each time without duplicates

# When you are done testing and the code looks correct, export notebook into a python script.
# Get rid of extra jupyter junk at top
# Make sure at the end, you have a single function called movie_ET or something that does this whole thing
# You can have multiple functions in your python script, but they should all be called by the one main function
# That function will be used in our app.py to do the L part of the ETL