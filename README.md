# palhetadigital

This app defines a function called scrape_artist() that uses BeautifulSoup to scrape the name and image URL for a given artist ID from the Open Spotify website. It then loops through a list of Spotify artist IDs, scrapes the data for each artist, and stores it in a list of dictionaries.

The app then uses Streamlit to display the artist data in a gallery format, with the number of columns and column width customizable via sliders. The st.beta_columns() function is used to create a row of columns, and the st.image() function is used to display the artist image and name in each column.
