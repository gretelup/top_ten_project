# The Top Ten List

## Collaborators

* Mike Lygas
* Smita Sharma
* Arjun Subramaniam
* Gretel Uptegrove

## Quick Summary 

3-sentance summary of the project, what datasources, and final data model. 
Then, provide the steps to run the pipeline. 

Example:

We provide an ETL pipeline that enables Business Inteligence Analysts at FryCorp Network to determine which shows to promote for 
advertisements. We used Historical TV Show ratings from tv guide, historical viewership metrics from Nielson ratings, 
and show production budgets from Wikipedia. We provide our data in a SQL database which exposes, for the most genres, 
KPIs to determine which genres are underrepresented and could deliver the most value to the FryCorp network if prioritized.

Example steps to run the pipeline: 
1. Start MySql
2. Run `mysql -u username -p database_name < seed.sql` to seed the database and tables
3. Run `python etl.py` to extract the data and put it into the Postgres database
4. ????
5. Profit


## Narrative / Motivation

Explain what problem you are trying to accomplish. Make something up that explains what use case you are trying to solve.

Examples: 
* We are providing a Database for a TV network to make decisions about what shows to promote for advertisement

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