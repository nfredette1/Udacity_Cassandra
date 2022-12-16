import psycopg2


try: 
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=postgres password=Nate1617#")
except psycopg2.Error as e: 
    print("Error: Could not make connection to the Postgres database")
    print(e)


# ### Next use that connect to get a cursor that we will use to execute queries.


try: 
    cur = conn.cursor()
except psycopg2.Error as e: 
    print("Error: Could not get cursor to the Database")
    print(e)


# #### For this demo we will use automactic commit so that each action is commited without having to call conn.commit() after each command. The ability to rollback and commit transactions is a feature of Relational Databases. 


conn.set_session(autocommit=True)


# ### Imagine you work at an online Music Store. There will be many tables in our database,
#  but let's just focus on 4 tables around customer purchases. 
# 
# <img src="images/starSchema.png" width="750" height="750">
# 
# ### From this representation you can start to see the makings of a "STAR". 
# You will have one fact table (the center of the star) and 
# 3  dimension tables that are coming from it.

# ### TO-DO: Create the Fact table and insert the data into the table


try: 
    cur.execute("CREATE TABLE IF NOT EXISTS customer_transactions (cid int, stid int, spent numeric);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
#Insert into all tables 
try: 
    cur.execute("INSERT INTO customer_transactions (cid, stid, spent) \
                 VALUES (%s, %s, %s)", \
                 (1, 1, 30.30 ))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
try: 
    cur.execute("INSERT INTO customer_transactions (cid, stid, spent) \
                 VALUES (%s, %s, %s)", \
                 (2, 2, 50.30 ))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)


# ### TO-DO: Create the Dimension tables and insert data into those tables.

try: 
        cur.execute("CREATE TABLE IF NOT EXISTS customer(cid int, name varchar, rewards boolean);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
try: 
   cur.execute("INSERT INTO customer (cid, name, rewards) \
                 VALUES (%s, %s, %s)", \
                 (1, 'Joe', True))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO customer (cid, name, rewards) \
                 VALUES (%s, %s, %s)", \
                 (2, 'Karen', True))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
        cur.execute("CREATE TABLE IF NOT EXISTS store ( stid int, state varchar);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
try: 
    cur.execute("INSERT INTO store (stid, state) \
                 VALUES (%s, %s)", \
                 (1, 'NH'))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
try: 
   cur.execute("INSERT INTO store (stid, state) \
                 VALUES (%s, %s)", \
                 (2, 'MA'))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
        cur.execute("CREATE TABLE IF NOT EXISTS purchase (eid int, itemid int, item varchar);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
try: 
    cur.execute("INSERT INTO purchase (eid,itemid,item)\
        VALUES(%s,%s,%s)",\
            (1,3,"STUFF"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO purchase (eid,itemid,item)\
        VALUES(%s,%s,%s)",\
            (2,4,"fruit"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)


# ### Now run the following queries on this data easily because of 
# utilizing the Fact/ Dimension and Star Schema
#  
# #### Query 1: Find all the customers that spent more than 30 dollars, 
# who are they, which store they bought it from, location of the store, 
# what they bought and if they are a rewards member.
# 
# #### Query 2: How much did Customer 2 spend?

# ### Query 1:

try: 
    cur.execute("""SELECT ct.cid, c.name, c.rewards, s.stid, s.state, p.item , ct.spent
    FROM ((customer_transactions ct JOIN customer c ON ct.cid = c.cid) 
        JOIN purchase p ON ct.cid = p.eid )
            JOIN store s ON s.stid = ct.stid
            WHERE ct.spent >= 30 """)
    
    
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()


# ### Your output from the above cell should look like this:
# ('Toby', 1, 'CA', 'Let It Be', False)

# ### Query 2: 

try: 
    cur.execute("""SELECT ct.cid, ct.spent
    FROM customer_transactions ct 
            WHERE ct.cid = 2 """)
    
    
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()


# ### Your output from the above cell should include Customer 2 and the amount: 
# (2, 35.21)

# ### Summary: You can see here from this elegant schema that we were: 1) able to get "facts/metrics" from our fact table (how much each store sold), and 2) information about our customers that will allow us to do more indepth analytics to get answers to business questions by utilizing our fact and dimension tables. 

# ### TO-DO: Drop the tables

try: 
    cur.execute("DROP table customer_transactions")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table purchase")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table customer")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
try: 
    cur.execute("DROP table store")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)


# ### And finally close your cursor and connection. 

cur.close()
conn.close()

