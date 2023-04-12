import sqlite3
import csv

conn = sqlite3.connect('gdp_data.db')
cursor = conn.cursor()

# Create the gdp_data table
cursor.execute('''CREATE TABLE IF NOT EXISTS gdp_data
                  (year INTEGER PRIMARY KEY, gdp_usd_billion REAL, gdp_inr_billion REAL)''')

with open('gdp_data_usd.csv', 'r') as file:
    rows = csv.reader(file)
    for i, gdp in enumerate(rows):
        i += 1987
        cursor.execute('INSERT INTO gdp_data VALUES (?, ?, ?)', (i, float(gdp[0]), float(gdp[0]) * float(gdp[1]) ))

conn.commit()
conn.close()
