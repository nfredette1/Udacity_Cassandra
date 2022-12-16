import cassandra
from cassandra.cluster import Cluster

try:
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
except Exception as e:
    print(e)

try:
    session.execute("""
     CREATE KEYSPACE IF NOT EXISTS udacity
    WITH REPLICATION =
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
)
except Exception as e:
    print(e)

session.shutdown()
cluster.shutdown()