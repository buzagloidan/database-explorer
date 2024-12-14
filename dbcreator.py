import sqlite3
import csv

DB_PATH = 'records.db'
CSV_FILE = 'database.csv'

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Create a table structure according to your CSV columns.
# Adjust column names and types as needed.
cur.execute('''
    CREATE TABLE IF NOT EXISTS records (
        o TEXT,
        f TEXT,
        l TEXT,
        v TEXT,
        p TEXT,
        a TEXT,
        s TEXT,
        t TEXT,
        vo TEXT,
        ci TEXT
    )
''')

# Clear the table if needed
cur.execute('DELETE FROM records')

# Insert CSV data
with open(CSV_FILE, 'r', encoding='utf-8') as f:
    # Set delimiter and quotechar based on your CSV format
    # If your CSV uses commas as separators and single quotes around fields:
    reader = csv.reader(f, delimiter=',', quotechar="'")

    # If there's a header line, read and ignore it
    header = next(reader, None)

    for row in reader:
        # Ensure we have exactly 10 columns
        if len(row) == 10:
            cur.execute("INSERT INTO records VALUES (?,?,?,?,?,?,?,?,?,?)", row)
        else:
            # If rows are malformed (not 10 fields), handle accordingly
            # You can print them, skip them, or log them as errors
            # For now, let's just skip
            pass

conn.commit()
conn.close()
