import sqlite3
import os

conn = sqlite3.connect("image.db")

cur = conn.cursor()


# Read the SQL file
with open('init.sql', 'r') as f :
	sql_script = f.read()

# Execute the SQL script
cur.executescript(sql_script)

# Commit the changes and close the connection
conn.commit()