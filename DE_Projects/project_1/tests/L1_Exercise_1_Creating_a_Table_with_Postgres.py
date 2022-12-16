#Create a table in PostgreSQL,
#Insert rows of data
#Run a simple SQL query to validate the information.

import psycopg2

try: 
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=postgres password=Nate1617#")
except psycopg2.Error as e: 
    print("Error: Could not make connection to the Postgres database")
    print(e)

try: 
    cur = conn.cursor()
except psycopg2.Error as e: 
    print("Error: Could not get curser to the Database")
    print(e)

# TO-DO: set automatic commit to be true

conn.set_session(autocommit=True)

## TO-DO: Add the database name within the CREATE DATABASE statement. You can choose your own db name.
try: 
    cur.execute("create database natesSongs")
except psycopg2.Error as e:
    print(e)

## TO-DO: Add the database name within the connect statement
try: 
    conn.close()
except psycopg2.Error as e:
    print(e)
    
try: 
    conn = psycopg2.connect("host=127.0.0.1 dbname=natessongs user=postgres password=Nate1617#")
except psycopg2.Error as e: 
    print("Error: Could not make connection to the Postgres database")
    print(e)
    
try: 
    cur = conn.cursor()
except psycopg2.Error as e: 
    print("Error: Could not get curser to the Database")
    print(e)

conn.set_session(autocommit=True)

## TO-DO: Finish writing the CREATE TABLE statement with the correct arguments
try: 
    cur.execute("CREATE TABLE IF NOT EXISTS songlib (song_title varchar, artist_name varchar, year int, album_name varchar, single varchar);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

## TO-DO: Finish the INSERT INTO statement with the correct arguments

try: 
    cur.execute("INSERT INTO songlib (song_title, artist_name,year,album_name,single) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 ("Across The Universe", "The Beatles", "1970", "Let It Be", "False"))

except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO songlib (song_title, artist_name,year,album_name,single) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 ("Think For Yourself", "The Beatles", "1965", "Rubber Soul", "False"))

except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)


## TO-DO: Finish the SELECT * Statement 
try: 
    cur.execute("SELECT * FROM songlib;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()

cur.close()
conn.close()