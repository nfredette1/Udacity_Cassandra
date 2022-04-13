# Sparkify Database project

*** extracting song data from files in order to insert into a database.

## Purpose:

The purpose of this database is to allow the Sparkify to quickly analyze data across millions of rows in their song database.

## Database design: 
Star Schema 
Fact table: songplays has a record of each song played
Dimension tables:
    1. users - customer details
    2. artists - artists specifics
    3. songs - song details
    4. time - time intervals

## ETL Process: 
Extracting the json log and song files.  Filtering by only played songs and loading all the related details into tables for analytical queries.

How to run scripts in order:

1. create_tables.py
2. etl.py

Explanation of files:

create_tables.py initiates the DB structure for loading.
etl.py performs transformations then loads the data into the DB.
test.ipynb checks tables for accuracy of structure and content
etl.ipynb checks on a small amount of data loading successfully into the DB.

Justification:

The star schema allows for data modeling and easier to read queries.

