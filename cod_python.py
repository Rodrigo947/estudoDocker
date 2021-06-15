import os
import psycopg2

host = os.environ.get("IP_POSTGRES")
dbname = os.environ.get("POSTGRES_DB")
user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
stringConnection = ( "host=%s dbname=%s user=%s password=%s" % (host,dbname,user,password) )

# Connect to your postgres DB
conn = psycopg2.connect(stringConnection)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM usuario")

# Retrieve query results
records = cur.fetchall()

print(records)
