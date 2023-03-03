import streamlit as st
import requests
from bs4 import BeautifulSoup

# Define the base URL for Spotify artists
base_url = "https://open.spotify.com/artist/"

# Define a function to scrape artist data from Spotify
def scrape_artist(artist_id):
    url = base_url + artist_id
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find('h1', class_='gl-heading').text
    image_url = soup.find('img', class_='artist-hero-image')['src']
    return name, image_url

# Define a list of Spotify artist IDs
artist_ids = ["2ye2Wgw4gimLv2eAKyk1NB", "6sFIWsNpZYqfXoTGm0inwz", "1dfeR4HaWDbWqFHLkxsg1d", "7vYbulKMT0S5ZGxPRLut0s", "04gDigrS5kc9YWfZHwBETP"]

# Define the layout of the Streamlit app
st.set_page_config(page_title="Spotify Artists Gallery", page_icon=":musical_note:")
st.title("Spotify Artists Gallery")

# Loop through the artist IDs and scrape the artist data
artists = []
for artist_id in artist_ids:
    name, image_url = scrape_artist(artist_id)
    artists.append({"name": name, "image_url": image_url})

# Display the artist data in a gallery format
col_width = st.session_state["col_width"] if "col_width" in st.session_state else None
col_width = st.slider("Column Width", 100, 500, col_width, 50)
num_columns = int(st.session_state["num_columns"]) if "num_columns" in st.session_state else 3
num_columns = st.slider("Number of Columns", 1, 6, num_columns)
st.session_state["col_width"] = col_width
st.session_state["num_columns"] = num_columns
for i in range(0, len(artists), num_columns):
    row = st.beta_columns(num_columns)
    for j in range(num_columns):
        if i + j < len(artists):
            with row[j]:
                st.image(artists[i+j]["image_url"], width=col_width, caption=artists[i+j]["name"])
