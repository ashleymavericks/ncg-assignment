import sqlite3
import requests
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from dotenv import load_dotenv
import os

load_dotenv()

conn = sqlite3.connect('gdp_data.db')

# Retrieve GDP data
query = "SELECT year, gdp_usd_billion FROM gdp_data"
df = pd.read_sql(query, conn)

# Retrieve the conversion rate from external API
response = requests.get(
    f"https://api.currencyfreaks.com/latest?apikey={os.getenv('API_KEY')}")
data = response.json()
conversion_rate = data['rates']['INR']

# Display the Chart with GDP data
fig, ax = plt.subplots()
ax.plot(df['year'], df['gdp_usd_billion'])
ax.set_title('India GDP in USD Billions')
ax.set_xlabel('Year')
ax.set_ylabel('GDP in USD Billions')
plt.xticks(rotation=90)
ax.set_xticks(df['year'])
plt.show()

# Converts the GDP data from USD to INR
def convert_to_inr():
    df['gdp_inr_billion'] = df['gdp_usd_billion'].astype(float) * float(conversion_rate)
    fig, ax = plt.subplots()
    ax.plot(df['year'], df['gdp_inr_billion'])
    ax.set_title('India GDP in INR Billions')
    ax.set_xlabel('Year')
    ax.set_ylabel('GDP in INR Billions')
    plt.xticks(rotation=90)
    ax.set_xticks(df['year']) 
    plt.show()


# Render GUI to display the bar chart in INR
root = Tk()
convert_button = Button(root, text="Convert to INR", command=convert_to_inr)
convert_button.pack()
root.mainloop()
