import sqlite3

DB_PATH = 'records.db'

# Connect to the database
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Select the first 10 records
cur.execute("SELECT * FROM records LIMIT 10;")

# Fetch all the results from the executed query
rows = cur.fetchall()

# Print each row for inspection
for i, row in enumerate(rows, start=1):
    print(f"Record {i}:", row)

conn.close()
